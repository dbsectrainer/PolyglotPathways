/**
 * Fill in the Blank Exercise Component
 * Interactive text inputs for missing words in sentences
 */

class FillBlankExercise {
    constructor(container, exerciseData, index, controller) {
        this.container = container;
        this.data = exerciseData;
        this.index = index;
        this.controller = controller;
        this.completed = false;
        this.inputs = [];
        
        this.render();
        this.bindEvents();
    }

    render() {
        this.container.innerHTML = `
            <div class="fill-blank-exercise">
                <div class="exercise-instructions">
                    <p>${this.data.instructions || 'Fill in the blanks with the correct words or phrases.'}</p>
                </div>
                
                <div class="fill-blank-content">
                    <div class="sentences-container">
                        ${this.renderSentences()}
                    </div>
                    
                    ${this.data.wordBank ? this.renderWordBank() : ''}
                </div>
                
                <div class="exercise-actions">
                    <button class="btn-secondary" onclick="window.fillBlankExercises[${this.index}].showHints()">
                        <i class="fas fa-lightbulb"></i> Hints
                    </button>
                    <button class="btn-secondary" onclick="window.fillBlankExercises[${this.index}].reset()">
                        <i class="fas fa-redo"></i> Reset
                    </button>
                    <button class="btn-primary" onclick="window.fillBlankExercises[${this.index}].checkAnswers()">
                        <i class="fas fa-check"></i> Check Answers
                    </button>
                </div>
                
                <div class="exercise-feedback" id="feedback-${this.index}"></div>
                <div class="hints-container" id="hints-${this.index}" style="display: none;"></div>
            </div>
        `;

        // Store reference for global access
        if (!window.fillBlankExercises) {
            window.fillBlankExercises = {};
        }
        window.fillBlankExercises[this.index] = this;
    }

    renderSentences() {
        return this.data.sentences.map((sentence, sentenceIndex) => {
            let html = sentence.text;
            let inputIndex = 0;

            // Replace blanks with input fields
            sentence.blanks.forEach((blank, blankIndex) => {
                const placeholder = `[${blank.placeholder || 'blank'}]`;
                const inputId = `input-${this.index}-${sentenceIndex}-${blankIndex}`;
                const globalInputIndex = this.inputs.length;
                
                // Store input info for later reference
                this.inputs.push({
                    id: inputId,
                    correct: Array.isArray(blank.correct) ? blank.correct : [blank.correct],
                    hint: blank.hint || '',
                    sentenceIndex,
                    blankIndex
                });

                html = html.replace(placeholder, 
                    `<input type="text" 
                           class="fill-blank-input" 
                           id="${inputId}"
                           data-input-index="${globalInputIndex}"
                           placeholder="${blank.placeholder || 'Type here...'}"
                           aria-label="Fill in the blank ${blankIndex + 1}"
                           aria-describedby="hint-${inputId}"
                           autocomplete="off"
                           spellcheck="false">`
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
        if (!this.data.wordBank || this.data.wordBank.length === 0) {
            return '';
        }

        // Shuffle word bank
        const shuffledWords = this.shuffleArray([...this.data.wordBank]);

        return `
            <div class="word-bank">
                <h5><i class="fas fa-list"></i> Word Bank</h5>
                <div class="word-bank-items">
                    ${shuffledWords.map(word => `
                        <span class="word-bank-item" 
                              onclick="window.fillBlankExercises[${this.index}].insertWord('${word}')"
                              tabindex="0"
                              role="button"
                              aria-label="Insert word: ${word}">
                            ${word}
                        </span>
                    `).join('')}
                </div>
                <p class="word-bank-instruction">Click on words to insert them into the focused input field.</p>
            </div>
        `;
    }

    bindEvents() {
        // Add real-time feedback
        this.inputs.forEach((inputInfo, index) => {
            const input = document.getElementById(inputInfo.id);
            if (input) {
                input.addEventListener('input', () => {
                    this.validateInput(input, inputInfo);
                });

                input.addEventListener('blur', () => {
                    this.validateInput(input, inputInfo, true);
                });

                // Enhanced keyboard navigation
                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Tab') {
                        // Natural tab navigation
                        return;
                    } else if (e.key === 'Enter') {
                        e.preventDefault();
                        this.focusNextInput(index);
                    } else if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                        e.preventDefault();
                        this.focusNextInput(index);
                    } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                        e.preventDefault();
                        this.focusPrevInput(index);
                    }
                });
            }
        });

        // Word bank click events
        const wordBankItems = this.container.querySelectorAll('.word-bank-item');
        wordBankItems.forEach(item => {
            item.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.insertWord(item.textContent.trim());
                }
            });
        });
    }

    validateInput(input, inputInfo, showFeedback = false) {
        const userAnswer = input.value.trim().toLowerCase();
        const correctAnswers = inputInfo.correct.map(answer => answer.toLowerCase());
        
        // Remove previous styling
        input.classList.remove('correct', 'incorrect', 'partial');
        
        if (userAnswer === '') {
            // Empty input
            return;
        }

        // Check for exact matches
        if (correctAnswers.includes(userAnswer)) {
            input.classList.add('correct');
            if (showFeedback) {
                this.showInputFeedback(input, 'Correct!', 'success');
            }
        } else {
            // Check for partial matches
            const hasPartialMatch = correctAnswers.some(answer => 
                answer.includes(userAnswer) || userAnswer.includes(answer)
            );
            
            if (hasPartialMatch) {
                input.classList.add('partial');
                if (showFeedback) {
                    this.showInputFeedback(input, 'Close! Keep trying.', 'warning');
                }
            } else {
                input.classList.add('incorrect');
                if (showFeedback) {
                    this.showInputFeedback(input, 'Try again.', 'error');
                }
            }
        }
    }

    showInputFeedback(input, message, type) {
        // Remove existing feedback
        const existingFeedback = input.parentElement.querySelector('.input-feedback');
        if (existingFeedback) {
            existingFeedback.remove();
        }

        // Create feedback element
        const feedback = document.createElement('span');
        feedback.className = `input-feedback feedback-${type}`;
        feedback.textContent = message;
        feedback.setAttribute('role', 'status');
        feedback.setAttribute('aria-live', 'polite');
        
        // Position feedback
        input.parentElement.style.position = 'relative';
        feedback.style.position = 'absolute';
        feedback.style.top = '100%';
        feedback.style.left = '0';
        feedback.style.fontSize = '0.8em';
        feedback.style.marginTop = '2px';
        
        input.parentElement.appendChild(feedback);
        
        // Remove feedback after delay
        setTimeout(() => {
            if (feedback.parentElement) {
                feedback.remove();
            }
        }, 2000);
    }

    insertWord(word) {
        const focusedInput = document.activeElement;
        if (focusedInput && focusedInput.classList.contains('fill-blank-input')) {
            focusedInput.value = word;
            focusedInput.dispatchEvent(new Event('input'));
            this.controller.accessibility.announceText(`Inserted word: ${word}`);
        } else {
            // Find first empty input
            const emptyInput = this.container.querySelector('.fill-blank-input[value=""], .fill-blank-input:not([value])');
            if (emptyInput) {
                emptyInput.value = word;
                emptyInput.focus();
                emptyInput.dispatchEvent(new Event('input'));
                this.controller.accessibility.announceText(`Inserted word: ${word}`);
            }
        }
    }

    focusNextInput(currentIndex) {
        const nextIndex = currentIndex + 1;
        if (nextIndex < this.inputs.length) {
            const nextInput = document.getElementById(this.inputs[nextIndex].id);
            if (nextInput) {
                nextInput.focus();
            }
        }
    }

    focusPrevInput(currentIndex) {
        const prevIndex = currentIndex - 1;
        if (prevIndex >= 0) {
            const prevInput = document.getElementById(this.inputs[prevIndex].id);
            if (prevInput) {
                prevInput.focus();
            }
        }
    }

    showHints() {
        const hintsContainer = document.getElementById(`hints-${this.index}`);
        const isVisible = hintsContainer.style.display !== 'none';
        
        if (isVisible) {
            hintsContainer.style.display = 'none';
            this.controller.accessibility.announceText('Hints hidden');
        } else {
            hintsContainer.innerHTML = `
                <div class="hints-content">
                    <h5><i class="fas fa-lightbulb"></i> Hints</h5>
                    <ul>
                        ${this.inputs.map((inputInfo, index) => {
                            if (inputInfo.hint) {
                                return `<li><strong>Blank ${index + 1}:</strong> ${inputInfo.hint}</li>`;
                            }
                            return '';
                        }).filter(hint => hint).join('')}
                    </ul>
                </div>
            `;
            hintsContainer.style.display = 'block';
            this.controller.accessibility.announceText('Hints shown');
        }
    }

    checkAnswers() {
        let correct = 0;
        let total = this.inputs.length;
        const feedback = document.getElementById(`feedback-${this.index}`);
        const results = [];
        
        this.inputs.forEach((inputInfo, index) => {
            const input = document.getElementById(inputInfo.id);
            const userAnswer = input.value.trim().toLowerCase();
            const correctAnswers = inputInfo.correct.map(answer => answer.toLowerCase());
            
            if (correctAnswers.includes(userAnswer)) {
                input.classList.remove('incorrect', 'partial');
                input.classList.add('correct');
                correct++;
                results.push({ index, correct: true, answer: userAnswer });
            } else {
                input.classList.remove('correct', 'partial');
                input.classList.add('incorrect');
                results.push({ 
                    index, 
                    correct: false, 
                    answer: userAnswer,
                    expected: inputInfo.correct[0] // Show first correct answer
                });
            }
        });

        const percentage = Math.round((correct / total) * 100);
        
        if (percentage >= 80) {
            feedback.innerHTML = `
                <div class="feedback-success">
                    <i class="fas fa-check-circle"></i>
                    Excellent! You got ${correct} out of ${total} correct (${percentage}%).
                    ${this.generateDetailedFeedback(results, true)}
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
                    ${this.generateDetailedFeedback(results, false)}
                </div>
            `;
        }

        // Announce result for accessibility
        this.controller.accessibility.announceText(`Exercise results: ${correct} out of ${total} correct, ${percentage} percent`);
    }

    generateDetailedFeedback(results, isSuccess) {
        if (isSuccess) {
            return '<p>All answers are correct!</p>';
        }

        const incorrectResults = results.filter(result => !result.correct);
        if (incorrectResults.length === 0) {
            return '';
        }

        return `
            <div class="detailed-feedback">
                <h6>Review these answers:</h6>
                <ul>
                    ${incorrectResults.map(result => `
                        <li>
                            Blank ${result.index + 1}: 
                            You entered "<strong>${result.answer || '(empty)'}</strong>", 
                            correct answer is "<strong>${result.expected}</strong>"
                        </li>
                    `).join('')}
                </ul>
            </div>
        `;
    }

    reset() {
        // Clear all inputs
        this.inputs.forEach(inputInfo => {
            const input = document.getElementById(inputInfo.id);
            if (input) {
                input.value = '';
                input.classList.remove('correct', 'incorrect', 'partial');
            }
        });

        // Clear feedback
        const feedback = document.getElementById(`feedback-${this.index}`);
        feedback.innerHTML = '';

        // Hide hints
        const hintsContainer = document.getElementById(`hints-${this.index}`);
        hintsContainer.style.display = 'none';

        // Remove input feedback elements
        const inputFeedbacks = this.container.querySelectorAll('.input-feedback');
        inputFeedbacks.forEach(fb => fb.remove());

        this.completed = false;
        this.controller.accessibility.announceText('Exercise reset');
        
        // Focus first input
        if (this.inputs.length > 0) {
            const firstInput = document.getElementById(this.inputs[0].id);
            if (firstInput) {
                firstInput.focus();
            }
        }
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
window.FillBlankExercise = FillBlankExercise;