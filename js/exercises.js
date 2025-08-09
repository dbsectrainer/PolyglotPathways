/**
 * Interactive Exercises Controller
 * Manages drag-and-drop, fill-in-the-blank, and matching game exercises
 */

class ExerciseController {
    constructor() {
        this.exercises = [];
        this.currentExercise = null;
        this.exerciseProgress = JSON.parse(localStorage.getItem('exerciseProgress') || '{}');
        this.accessibility = {
            announceText: (text) => {
                const announcement = document.createElement('div');
                announcement.setAttribute('aria-live', 'polite');
                announcement.setAttribute('aria-atomic', 'true');
                announcement.className = 'sr-only';
                announcement.textContent = text;
                document.body.appendChild(announcement);
                setTimeout(() => document.body.removeChild(announcement), 1000);
            }
        };
    }

    /**
     * Initialize exercises for a specific day and language
     */
    async initializeExercises(day, language) {
        try {
            const exerciseData = await this.loadExerciseData(day, language);
            if (exerciseData && exerciseData.exercises) {
                this.exercises = exerciseData.exercises;
                this.renderExercisesContainer();
                this.exercises.forEach((exercise, index) => {
                    this.renderExercise(exercise, index);
                });
            }
        } catch (error) {
            console.log('No exercises available for this lesson:', error);
            // Graceful degradation - no exercises shown if data not available
        }
    }

    /**
     * Load exercise data from JSON file
     */
    async loadExerciseData(day, language) {
        const response = await fetch(`exercises/day${day}_${language}.json`);
        if (!response.ok) {
            throw new Error(`Exercise data not found: ${response.status}`);
        }
        return await response.json();
    }

    /**
     * Create the exercises container in the lesson page
     */
    renderExercisesContainer() {
        const textContent = document.getElementById('text-content');
        if (!textContent) return;

        // Check if exercises container already exists
        if (document.getElementById('exercises-container')) return;

        const exercisesContainer = document.createElement('div');
        exercisesContainer.id = 'exercises-container';
        exercisesContainer.className = 'exercises-container';
        exercisesContainer.innerHTML = `
            <div class="exercises-header">
                <h3><i class="fas fa-puzzle-piece"></i> Interactive Exercises</h3>
                <p>Practice what you've learned with these interactive activities!</p>
            </div>
            <div class="exercises-list" id="exercises-list"></div>
        `;

        // Insert after text content but before lesson actions
        const lessonActions = document.querySelector('.lesson-actions');
        if (lessonActions) {
            textContent.parentNode.insertBefore(exercisesContainer, lessonActions);
        } else {
            textContent.parentNode.appendChild(exercisesContainer);
        }
    }

    /**
     * Render an individual exercise
     */
    renderExercise(exercise, index) {
        const exercisesList = document.getElementById('exercises-list');
        if (!exercisesList) return;

        const exerciseElement = document.createElement('div');
        exerciseElement.className = 'exercise-item';
        exerciseElement.id = `exercise-${index}`;

        // Create exercise header
        const header = document.createElement('div');
        header.className = 'exercise-header';
        header.innerHTML = `
            <h4>
                <i class="fas ${this.getExerciseIcon(exercise.type)}"></i>
                ${exercise.title}
            </h4>
            <div class="exercise-status" id="status-${index}">
                ${this.getExerciseStatus(exercise, index)}
            </div>
        `;

        // Create exercise content
        const content = document.createElement('div');
        content.className = 'exercise-content';
        content.id = `content-${index}`;

        exerciseElement.appendChild(header);
        exerciseElement.appendChild(content);
        exercisesList.appendChild(exerciseElement);

        // Render specific exercise type
        this.renderExerciseContent(exercise, index);
    }

    /**
     * Get icon for exercise type
     */
    getExerciseIcon(type) {
        const icons = {
            'drag-drop': 'fa-arrows-alt',
            'fill-blank': 'fa-edit',
            'matching': 'fa-link'
        };
        return icons[type] || 'fa-puzzle-piece';
    }

    /**
     * Get exercise completion status
     */
    getExerciseStatus(exercise, index) {
        const key = this.getProgressKey(exercise, index);
        const isCompleted = this.exerciseProgress[key] || false;
        
        if (isCompleted) {
            return '<span class="status-completed"><i class="fas fa-check-circle"></i> Completed</span>';
        } else {
            return '<span class="status-pending"><i class="fas fa-circle"></i> Not Started</span>';
        }
    }

    /**
     * Render exercise content based on type
     */
    renderExerciseContent(exercise, index) {
        const content = document.getElementById(`content-${index}`);
        if (!content) return;

        switch (exercise.type) {
            case 'drag-drop':
                if (window.DragDropExercise) {
                    new window.DragDropExercise(content, exercise, index, this);
                }
                break;
            case 'fill-blank':
                if (window.FillBlankExercise) {
                    new window.FillBlankExercise(content, exercise, index, this);
                }
                break;
            case 'matching':
                if (window.MatchingExercise) {
                    new window.MatchingExercise(content, exercise, index, this);
                }
                break;
            default:
                content.innerHTML = `<p>Exercise type "${exercise.type}" not supported.</p>`;
        }
    }

    /**
     * Mark exercise as completed
     */
    markExerciseCompleted(exercise, index) {
        const key = this.getProgressKey(exercise, index);
        this.exerciseProgress[key] = true;
        localStorage.setItem('exerciseProgress', JSON.stringify(this.exerciseProgress));

        // Update status display
        const statusElement = document.getElementById(`status-${index}`);
        if (statusElement) {
            statusElement.innerHTML = '<span class="status-completed"><i class="fas fa-check-circle"></i> Completed</span>';
        }

        // Announce completion for accessibility
        this.accessibility.announceText(`Exercise "${exercise.title}" completed successfully!`);

        // Show completion animation
        const exerciseElement = document.getElementById(`exercise-${index}`);
        if (exerciseElement) {
            exerciseElement.classList.add('exercise-completed');
        }
    }

    /**
     * Generate progress key for localStorage
     */
    getProgressKey(exercise, index) {
        const urlParams = new URLSearchParams(window.location.search);
        const day = urlParams.get('day') || '1';
        const lang = urlParams.get('lang') || 'en';
        return `exercise_${day}_${lang}_${index}`;
    }

    /**
     * Check if all exercises are completed
     */
    areAllExercisesCompleted() {
        return this.exercises.every((exercise, index) => {
            const key = this.getProgressKey(exercise, index);
            return this.exerciseProgress[key] || false;
        });
    }

    /**
     * Get exercise completion count
     */
    getCompletedExerciseCount() {
        return this.exercises.filter((exercise, index) => {
            const key = this.getProgressKey(exercise, index);
            return this.exerciseProgress[key] || false;
        }).length;
    }
}

// Initialize global exercise controller
window.exerciseController = null;

// Auto-initialize exercises when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Wait for page to be fully loaded, then initialize exercises
    setTimeout(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const day = parseInt(urlParams.get('day')) || 1;
        const lang = urlParams.get('lang') || 'en';
        
        if (document.getElementById('text-content')) {
            window.exerciseController = new ExerciseController();
            window.exerciseController.initializeExercises(day, lang);
        }
    }, 500);
});