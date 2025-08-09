/**
 * Drag and Drop Exercise Component
 * Allows users to drag words/phrases to correct positions
 */

class DragDropExercise {
    constructor(container, exerciseData, index, controller) {
        this.container = container;
        this.data = exerciseData;
        this.index = index;
        this.controller = controller;
        this.completed = false;
        this.draggedElement = null;
        this.touchItem = null;
        this.touchOffset = { x: 0, y: 0 };
        
        this.render();
        this.bindEvents();
    }

    render() {
        this.container.innerHTML = `
            <div class="drag-drop-exercise">
                <div class="exercise-instructions">
                    <p>${this.data.instructions || 'Drag the words to complete the sentences correctly.'}</p>
                </div>
                
                <div class="drag-drop-content">
                    <div class="sentence-area" id="sentence-area-${this.index}">
                        ${this.renderSentences()}
                    </div>
                    
                    <div class="word-bank" id="word-bank-${this.index}">
                        <h5><i class="fas fa-grip-vertical"></i> Word Bank</h5>
                        <div class="words-container">
                            ${this.renderWordBank()}
                        </div>
                    </div>
                </div>
                
                <div class="exercise-actions">
                    <button class="btn-secondary" onclick="window.dragDropExercises[${this.index}].reset()">
                        <i class="fas fa-redo"></i> Reset
                    </button>
                    <button class="btn-primary" onclick="window.dragDropExercises[${this.index}].checkAnswers()">
                        <i class="fas fa-check"></i> Check Answers
                    </button>
                </div>
                
                <div class="exercise-feedback" id="feedback-${this.index}"></div>
            </div>
        `;

        // Store reference for global access
        if (!window.dragDropExercises) {
            window.dragDropExercises = {};
        }
        window.dragDropExercises[this.index] = this;
    }

    renderSentences() {
        return this.data.sentences.map((sentence, sentenceIndex) => {
            // Replace blanks with drop zones
            let html = sentence.text;
            sentence.blanks.forEach((blank, blankIndex) => {
                const dropZoneId = `drop-${this.index}-${sentenceIndex}-${blankIndex}`;
                const placeholder = `[${blank.placeholder || 'blank'}]`;
                html = html.replace(placeholder, 
                    `<span class="drop-zone" 
                           id="${dropZoneId}"
                           data-correct="${blank.correct}"
                           data-sentence="${sentenceIndex}"
                           data-blank="${blankIndex}"
                           tabindex="0"
                           role="button"
                           aria-label="Drop zone for ${blank.correct}"
                           aria-describedby="drop-instruction-${this.index}">
                        <span class="drop-zone-placeholder">Drop here</span>
                    </span>`
                );
            });
            return `
                <div class="sentence-item" data-sentence="${sentenceIndex}">
                    <p>${html}</p>
                </div>
            `;
        }).join('');
    }

    renderWordBank() {
        // Collect all words and shuffle them
        const allWords = [];
        this.data.sentences.forEach(sentence => {
            sentence.blanks.forEach(blank => {
                allWords.push(blank.correct);
            });
        });
        
        // Add extra words if provided
        if (this.data.extraWords) {
            allWords.push(...this.data.extraWords);
        }

        // Shuffle array
        const shuffledWords = this.shuffleArray([...allWords]);

        return shuffledWords.map((word, wordIndex) => `
            <div class="draggable-word" 
                 draggable="true"
                 id="word-${this.index}-${wordIndex}"
                 data-word="${word}"
                 tabindex="0"
                 role="button"
                 aria-label="Draggable word: ${word}"
                 aria-describedby="drag-instruction-${this.index}">
                ${word}
            </div>
        `).join('');
    }

    bindEvents() {
        // Add instruction elements for screen readers
        const instructionElement = document.createElement('div');
        instructionElement.id = `drag-instruction-${this.index}`;
        instructionElement.className = 'sr-only';
        instructionElement.textContent = 'Use mouse to drag or use keyboard: Tab to navigate, Enter to select/deselect, arrow keys to move selected items.';
        this.container.appendChild(instructionElement);

        const dropInstructionElement = document.createElement('div');
        dropInstructionElement.id = `drop-instruction-${this.index}`;
        dropInstructionElement.className = 'sr-only';
        dropInstructionElement.textContent = 'Drop zone: Press Enter to place selected word here.';
        this.container.appendChild(dropInstructionElement);

        // Bind drag events
        this.bindDragEvents();
        // Bind keyboard events for accessibility
        this.bindKeyboardEvents();
        // Bind touch events for mobile
        this.bindTouchEvents();
    }

    bindDragEvents() {
        const wordBank = this.container.querySelector('.words-container');
        const sentenceArea = this.container.querySelector('.sentence-area');

        // Draggable events
        wordBank.addEventListener('dragstart', (e) => {
            if (e.target.classList.contains('draggable-word')) {
                this.draggedElement = e.target;
                e.target.classList.add('dragging');
                e.dataTransfer.effectAllowed = 'move';
                e.dataTransfer.setData('text/html', e.target.outerHTML);
            }
        });

        wordBank.addEventListener('dragend', (e) => {
            if (e.target.classList.contains('draggable-word')) {
                e.target.classList.remove('dragging');
                this.draggedElement = null;
            }
        });

        // Drop zone events
        sentenceArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            
            if (e.target.classList.contains('drop-zone')) {
                e.target.classList.add('drag-over');
            }
        });

        sentenceArea.addEventListener('dragleave', (e) => {
            if (e.target.classList.contains('drop-zone')) {
                e.target.classList.remove('drag-over');
            }
        });

        sentenceArea.addEventListener('drop', (e) => {
            e.preventDefault();
            
            if (e.target.classList.contains('drop-zone') && this.draggedElement) {
                e.target.classList.remove('drag-over');
                this.placeWordInDropZone(this.draggedElement, e.target);
            }
        });

        // Allow dropping back to word bank
        wordBank.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
        });

        wordBank.addEventListener('drop', (e) => {
            e.preventDefault();
            if (this.draggedElement && this.draggedElement.parentElement.classList.contains('drop-zone')) {
                this.returnWordToBank(this.draggedElement);
            }
        });
    }

    bindKeyboardEvents() {
        let selectedWord = null;

        this.container.addEventListener('keydown', (e) => {
            if (e.target.classList.contains('draggable-word')) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    if (selectedWord === e.target) {
                        // Deselect
                        selectedWord.classList.remove('selected');
                        selectedWord = null;
                        this.controller.accessibility.announceText('Word deselected');
                    } else {
                        // Select new word
                        if (selectedWord) {
                            selectedWord.classList.remove('selected');
                        }
                        selectedWord = e.target;
                        selectedWord.classList.add('selected');
                        this.controller.accessibility.announceText(`Selected word: ${e.target.textContent}`);
                    }
                }
            } else if (e.target.classList.contains('drop-zone') && selectedWord) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.placeWordInDropZone(selectedWord, e.target);
                    selectedWord.classList.remove('selected');
                    selectedWord = null;
                }
            }
        });
    }

    bindTouchEvents() {
        this.container.addEventListener('touchstart', (e) => {
            if (e.target.classList.contains('draggable-word')) {
                this.touchItem = e.target;
                const touch = e.touches[0];
                const rect = e.target.getBoundingClientRect();
                this.touchOffset.x = touch.clientX - rect.left;
                this.touchOffset.y = touch.clientY - rect.top;
                e.target.classList.add('touch-dragging');
                e.preventDefault();
            }
        });

        this.container.addEventListener('touchmove', (e) => {
            if (this.touchItem) {
                const touch = e.touches[0];
                this.touchItem.style.position = 'fixed';
                this.touchItem.style.left = (touch.clientX - this.touchOffset.x) + 'px';
                this.touchItem.style.top = (touch.clientY - this.touchOffset.y) + 'px';
                this.touchItem.style.zIndex = '1000';
                e.preventDefault();
            }
        });

        this.container.addEventListener('touchend', (e) => {
            if (this.touchItem) {
                const touch = e.changedTouches[0];
                const elementBelow = document.elementFromPoint(touch.clientX, touch.clientY);
                
                this.touchItem.style.position = '';
                this.touchItem.style.left = '';
                this.touchItem.style.top = '';
                this.touchItem.style.zIndex = '';
                this.touchItem.classList.remove('touch-dragging');

                if (elementBelow && elementBelow.classList.contains('drop-zone')) {
                    this.placeWordInDropZone(this.touchItem, elementBelow);
                }

                this.touchItem = null;
            }
        });
    }

    placeWordInDropZone(word, dropZone) {
        // Check if drop zone already has a word
        const existingWord = dropZone.querySelector('.draggable-word');
        if (existingWord) {
            this.returnWordToBank(existingWord);
        }

        // Remove placeholder
        const placeholder = dropZone.querySelector('.drop-zone-placeholder');
        if (placeholder) {
            placeholder.style.display = 'none';
        }

        // Move word to drop zone
        word.classList.remove('selected');
        dropZone.appendChild(word);
        
        // Announce for accessibility
        this.controller.accessibility.announceText(`Placed "${word.textContent}" in drop zone`);
    }

    returnWordToBank(word) {
        const wordBank = this.container.querySelector('.words-container');
        const dropZone = word.parentElement;
        
        if (dropZone && dropZone.classList.contains('drop-zone')) {
            // Show placeholder again
            const placeholder = dropZone.querySelector('.drop-zone-placeholder');
            if (placeholder) {
                placeholder.style.display = 'inline';
            }
        }
        
        wordBank.appendChild(word);
        this.controller.accessibility.announceText(`Returned "${word.textContent}" to word bank`);
    }

    checkAnswers() {
        let correct = 0;
        let total = 0;
        const feedback = document.getElementById(`feedback-${this.index}`);
        
        this.data.sentences.forEach((sentence, sentenceIndex) => {
            sentence.blanks.forEach((blank, blankIndex) => {
                total++;
                const dropZoneId = `drop-${this.index}-${sentenceIndex}-${blankIndex}`;
                const dropZone = document.getElementById(dropZoneId);
                const placedWord = dropZone.querySelector('.draggable-word');
                
                if (placedWord && placedWord.textContent.trim() === blank.correct) {
                    dropZone.classList.add('correct');
                    dropZone.classList.remove('incorrect');
                    correct++;
                } else {
                    dropZone.classList.add('incorrect');
                    dropZone.classList.remove('correct');
                }
            });
        });

        const percentage = Math.round((correct / total) * 100);
        
        if (percentage >= 80) {
            feedback.innerHTML = `
                <div class="feedback-success">
                    <i class="fas fa-check-circle"></i>
                    Excellent! You got ${correct} out of ${total} correct (${percentage}%).
                </div>
            `;
            this.completed = true;
            this.controller.markExerciseCompleted(this.data, this.index);
        } else {
            feedback.innerHTML = `
                <div class="feedback-partial">
                    <i class="fas fa-exclamation-circle"></i>
                    Good try! You got ${correct} out of ${total} correct (${percentage}%). 
                    Try again to get at least 80%.
                </div>
            `;
        }

        // Announce result for accessibility
        this.controller.accessibility.announceText(`Exercise results: ${correct} out of ${total} correct, ${percentage} percent`);
    }

    reset() {
        // Move all words back to word bank
        const placedWords = this.container.querySelectorAll('.drop-zone .draggable-word');
        placedWords.forEach(word => {
            this.returnWordToBank(word);
        });

        // Clear feedback
        const feedback = document.getElementById(`feedback-${this.index}`);
        feedback.innerHTML = '';

        // Remove correct/incorrect classes
        const dropZones = this.container.querySelectorAll('.drop-zone');
        dropZones.forEach(zone => {
            zone.classList.remove('correct', 'incorrect');
        });

        this.completed = false;
        this.controller.accessibility.announceText('Exercise reset');
    }

    shuffleArray(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }
}

// Export for global access
window.DragDropExercise = DragDropExercise;