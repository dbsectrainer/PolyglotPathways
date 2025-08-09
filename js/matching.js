/**
 * Matching Exercise Component
 * Match words with translations, definitions, or images
 */

class MatchingExercise {
    constructor(container, exerciseData, index, controller) {
        this.container = container;
        this.data = exerciseData;
        this.index = index;
        this.controller = controller;
        this.completed = false;
        this.selectedItems = { left: null, right: null };
        this.matches = [];
        this.keyboardSelectedItems = { left: null, right: null };
        
        this.render();
        this.bindEvents();
    }

    render() {
        // Shuffle the right column to make it challenging
        const shuffledRightItems = this.shuffleArray([...this.data.rightItems]);

        this.container.innerHTML = `
            <div class="matching-exercise">
                <div class="exercise-instructions">
                    <p>${this.data.instructions || 'Match the items in the left column with their corresponding items in the right column.'}</p>
                </div>
                
                <div class="matching-content">
                    <div class="matching-columns">
                        <div class="matching-column left-column">
                            <h5><i class="fas fa-list"></i> ${this.data.leftTitle || 'Items'}</h5>
                            <div class="matching-items">
                                ${this.renderLeftColumn()}
                            </div>
                        </div>
                        
                        <div class="matching-column right-column">
                            <h5><i class="fas fa-list"></i> ${this.data.rightTitle || 'Matches'}</h5>
                            <div class="matching-items">
                                ${this.renderRightColumn(shuffledRightItems)}
                            </div>
                        </div>
                    </div>
                    
                    <div class="matches-display" id="matches-display-${this.index}">
                        <h5><i class="fas fa-link"></i> Your Matches</h5>
                        <div class="matches-list" id="matches-list-${this.index}"></div>
                    </div>
                </div>
                
                <div class="exercise-actions">
                    <button class="btn-secondary" onclick="window.matchingExercises[${this.index}].clearMatches()">
                        <i class="fas fa-trash"></i> Clear All
                    </button>
                    <button class="btn-secondary" onclick="window.matchingExercises[${this.index}].reset()">
                        <i class="fas fa-redo"></i> Reset
                    </button>
                    <button class="btn-primary" onclick="window.matchingExercises[${this.index}].checkAnswers()">
                        <i class="fas fa-check"></i> Check Answers
                    </button>
                </div>
                
                <div class="exercise-feedback" id="feedback-${this.index}"></div>
            </div>
        `;

        // Store reference for global access
        if (!window.matchingExercises) {
            window.matchingExercises = {};
        }
        window.matchingExercises[this.index] = this;
    }

    renderLeftColumn() {
        return this.data.leftItems.map((item, index) => `
            <div class="matching-item left-item" 
                 data-id="${item.id}"
                 data-index="${index}"
                 tabindex="0"
                 role="button"
                 aria-label="${this.getItemLabel(item)}"
                 aria-describedby="matching-instruction-${this.index}">
                ${this.renderItemContent(item)}
            </div>
        `).join('');
    }

    renderRightColumn(shuffledItems) {
        return shuffledItems.map((item, index) => `
            <div class="matching-item right-item" 
                 data-id="${item.id}"
                 data-index="${index}"
                 tabindex="0"
                 role="button"
                 aria-label="${this.getItemLabel(item)}"
                 aria-describedby="matching-instruction-${this.index}">
                ${this.renderItemContent(item)}
            </div>
        `).join('');
    }

    renderItemContent(item) {
        if (item.type === 'image') {
            return `
                <div class="item-image">
                    <img src="${item.src}" alt="${item.alt || item.text}" />
                    ${item.text ? `<span class="item-text">${item.text}</span>` : ''}
                </div>
            `;
        } else {
            return `<span class="item-text">${item.text}</span>`;
        }
    }

    getItemLabel(item) {
        if (item.type === 'image') {
            return `Image: ${item.alt || item.text || 'Image item'}`;
        }
        return item.text;
    }

    bindEvents() {
        // Add instruction element for screen readers
        const instructionElement = document.createElement('div');
        instructionElement.id = `matching-instruction-${this.index}`;
        instructionElement.className = 'sr-only';
        instructionElement.textContent = 'Click to select items to match. Use keyboard: Tab to navigate, Enter to select, Escape to deselect.';
        this.container.appendChild(instructionElement);

        // Bind click events
        this.bindClickEvents();
        // Bind keyboard events for accessibility
        this.bindKeyboardEvents();
        // Bind touch events for mobile
        this.bindTouchEvents();
    }

    bindClickEvents() {
        const leftItems = this.container.querySelectorAll('.left-item');
        const rightItems = this.container.querySelectorAll('.right-item');

        leftItems.forEach(item => {
            item.addEventListener('click', () => {
                this.selectLeftItem(item);
            });
        });

        rightItems.forEach(item => {
            item.addEventListener('click', () => {
                this.selectRightItem(item);
            });
        });
    }

    bindKeyboardEvents() {
        this.container.addEventListener('keydown', (e) => {
            const item = e.target;
            
            if (!item.classList.contains('matching-item')) return;

            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                if (item.classList.contains('left-item')) {
                    this.selectLeftItem(item);
                } else if (item.classList.contains('right-item')) {
                    this.selectRightItem(item);
                }
            } else if (e.key === 'Escape') {
                e.preventDefault();
                this.clearSelection();
            } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                this.navigateItem(item, 'down');
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                this.navigateItem(item, 'up');
            } else if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
                e.preventDefault();
                this.navigateToOppositeColumn(item);
            }
        });
    }

    bindTouchEvents() {
        // Enhanced touch handling for mobile devices
        this.container.addEventListener('touchstart', (e) => {
            if (e.target.closest('.matching-item')) {
                e.target.closest('.matching-item').classList.add('touch-highlight');
            }
        });

        this.container.addEventListener('touchend', (e) => {
            const item = e.target.closest('.matching-item');
            if (item) {
                item.classList.remove('touch-highlight');
                // Simulate click
                item.click();
            }
        });
    }

    selectLeftItem(item) {
        // Clear previous left selection
        if (this.selectedItems.left) {
            this.selectedItems.left.classList.remove('selected');
        }

        // Check if item is already matched
        if (item.classList.contains('matched')) {
            this.controller.accessibility.announceText('This item is already matched');
            return;
        }

        this.selectedItems.left = item;
        item.classList.add('selected');
        
        const itemText = this.getItemLabel(this.getItemData(item.dataset.id, 'left'));
        this.controller.accessibility.announceText(`Selected left item: ${itemText}`);

        // If both items are selected, create match
        if (this.selectedItems.right) {
            this.createMatch();
        }
    }

    selectRightItem(item) {
        // Clear previous right selection
        if (this.selectedItems.right) {
            this.selectedItems.right.classList.remove('selected');
        }

        // Check if item is already matched
        if (item.classList.contains('matched')) {
            this.controller.accessibility.announceText('This item is already matched');
            return;
        }

        this.selectedItems.right = item;
        item.classList.add('selected');
        
        const itemText = this.getItemLabel(this.getItemData(item.dataset.id, 'right'));
        this.controller.accessibility.announceText(`Selected right item: ${itemText}`);

        // If both items are selected, create match
        if (this.selectedItems.left) {
            this.createMatch();
        }
    }

    createMatch() {
        const leftItem = this.selectedItems.left;
        const rightItem = this.selectedItems.right;
        
        if (!leftItem || !rightItem) return;

        const leftData = this.getItemData(leftItem.dataset.id, 'left');
        const rightData = this.getItemData(rightItem.dataset.id, 'right');

        // Create match object
        const match = {
            leftId: leftItem.dataset.id,
            rightId: rightItem.dataset.id,
            leftText: this.getItemLabel(leftData),
            rightText: this.getItemLabel(rightData),
            leftElement: leftItem,
            rightElement: rightItem
        };

        this.matches.push(match);

        // Mark items as matched
        leftItem.classList.add('matched');
        rightItem.classList.add('matched');
        leftItem.classList.remove('selected');
        rightItem.classList.remove('selected');

        // Clear selections
        this.selectedItems.left = null;
        this.selectedItems.right = null;

        // Update matches display
        this.updateMatchesDisplay();

        // Announce match creation
        this.controller.accessibility.announceText(`Created match: ${match.leftText} with ${match.rightText}`);
    }

    updateMatchesDisplay() {
        const matchesList = document.getElementById(`matches-list-${this.index}`);
        
        if (this.matches.length === 0) {
            matchesList.innerHTML = '<p class="no-matches">No matches yet. Select items from both columns to create matches.</p>';
            return;
        }

        matchesList.innerHTML = this.matches.map((match, index) => `
            <div class="match-item" data-match-index="${index}">
                <span class="match-content">
                    <span class="match-left">${match.leftText}</span>
                    <i class="fas fa-arrow-right match-arrow"></i>
                    <span class="match-right">${match.rightText}</span>
                </span>
                <button class="remove-match-btn" 
                        onclick="window.matchingExercises[${this.index}].removeMatch(${index})"
                        aria-label="Remove this match"
                        title="Remove this match">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `).join('');
    }

    removeMatch(matchIndex) {
        if (matchIndex < 0 || matchIndex >= this.matches.length) return;

        const match = this.matches[matchIndex];
        
        // Unmark items
        match.leftElement.classList.remove('matched');
        match.rightElement.classList.remove('matched');

        // Remove match from array
        this.matches.splice(matchIndex, 1);

        // Update display
        this.updateMatchesDisplay();

        // Announce removal
        this.controller.accessibility.announceText(`Removed match: ${match.leftText} with ${match.rightText}`);
    }

    clearSelection() {
        if (this.selectedItems.left) {
            this.selectedItems.left.classList.remove('selected');
            this.selectedItems.left = null;
        }
        if (this.selectedItems.right) {
            this.selectedItems.right.classList.remove('selected');
            this.selectedItems.right = null;
        }
        this.controller.accessibility.announceText('Selection cleared');
    }

    navigateItem(currentItem, direction) {
        const column = currentItem.classList.contains('left-item') ? 'left' : 'right';
        const items = this.container.querySelectorAll(`.${column}-item`);
        const itemsArray = Array.from(items);
        const currentIndex = itemsArray.indexOf(currentItem);
        
        let nextIndex;
        if (direction === 'down') {
            nextIndex = currentIndex + 1;
            if (nextIndex >= itemsArray.length) nextIndex = 0;
        } else {
            nextIndex = currentIndex - 1;
            if (nextIndex < 0) nextIndex = itemsArray.length - 1;
        }
        
        itemsArray[nextIndex].focus();
    }

    navigateToOppositeColumn(currentItem) {
        const isLeftColumn = currentItem.classList.contains('left-item');
        const targetColumn = isLeftColumn ? '.right-item' : '.left-item';
        const targetItems = this.container.querySelectorAll(targetColumn);
        
        if (targetItems.length > 0) {
            targetItems[0].focus();
        }
    }

    clearMatches() {
        // Remove all matches
        this.matches.forEach(match => {
            match.leftElement.classList.remove('matched');
            match.rightElement.classList.remove('matched');
        });

        this.matches = [];
        this.clearSelection();
        this.updateMatchesDisplay();
        
        this.controller.accessibility.announceText('All matches cleared');
    }

    checkAnswers() {
        let correct = 0;
        let total = this.data.correctPairs.length;
        const feedback = document.getElementById(`feedback-${this.index}`);
        const results = [];
        
        // Check each match against correct pairs
        this.matches.forEach(match => {
            const isCorrect = this.data.correctPairs.some(pair => 
                pair.leftId === match.leftId && pair.rightId === match.rightId
            );
            
            if (isCorrect) {
                correct++;
                match.leftElement.classList.add('correct-match');
                match.rightElement.classList.add('correct-match');
                results.push({ match, correct: true });
            } else {
                match.leftElement.classList.add('incorrect-match');
                match.rightElement.classList.add('incorrect-match');
                results.push({ match, correct: false });
            }
        });

        const percentage = total > 0 ? Math.round((correct / total) * 100) : 0;
        const missedPairs = this.data.correctPairs.length - this.matches.length;
        
        if (percentage >= 80 && missedPairs === 0) {
            feedback.innerHTML = `
                <div class="feedback-success">
                    <i class="fas fa-check-circle"></i>
                    Excellent! You got ${correct} out of ${total} matches correct (${percentage}%).
                    ${this.generateMatchFeedback(results, true)}
                </div>
            `;
            this.completed = true;
            this.controller.markExerciseCompleted(this.data, this.index);
        } else {
            feedback.innerHTML = `
                <div class="feedback-partial">
                    <i class="fas fa-exclamation-circle"></i>
                    Good try! You got ${correct} out of ${total} matches correct (${percentage}%).
                    ${missedPairs > 0 ? `You missed ${missedPairs} pair(s).` : ''}
                    Try again to get at least 80% with all pairs matched.
                    ${this.generateMatchFeedback(results, false)}
                </div>
            `;
        }

        // Announce result
        this.controller.accessibility.announceText(`Exercise results: ${correct} out of ${total} correct matches, ${percentage} percent`);
    }

    generateMatchFeedback(results, isSuccess) {
        if (isSuccess) {
            return '<p>All matches are correct!</p>';
        }

        const incorrectResults = results.filter(result => !result.correct);
        if (incorrectResults.length === 0) {
            return '<p>All current matches are correct, but you may have missed some pairs.</p>';
        }

        return `
            <div class="detailed-feedback">
                <h6>Review these matches:</h6>
                <ul>
                    ${incorrectResults.map(result => `
                        <li>${result.match.leftText} ↔ ${result.match.rightText} (incorrect)</li>
                    `).join('')}
                </ul>
            </div>
        `;
    }

    reset() {
        // Clear all matches and selections
        this.clearMatches();
        
        // Remove all styling
        const allItems = this.container.querySelectorAll('.matching-item');
        allItems.forEach(item => {
            item.classList.remove('selected', 'matched', 'correct-match', 'incorrect-match');
        });

        // Clear feedback
        const feedback = document.getElementById(`feedback-${this.index}`);
        feedback.innerHTML = '';

        this.completed = false;
        this.controller.accessibility.announceText('Exercise reset');
    }

    getItemData(id, column) {
        const items = column === 'left' ? this.data.leftItems : this.data.rightItems;
        return items.find(item => item.id === id);
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
window.MatchingExercise = MatchingExercise;