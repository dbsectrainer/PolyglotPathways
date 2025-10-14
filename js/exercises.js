/**
 * Interactive Exercises Module
 * Handles different types of learning exercises
 */

class ExerciseManager {
  constructor(progressTracker) {
    this.progressTracker = progressTracker;
    this.currentExercise = null;
    this.exerciseHistory = [];
  }

  /**
   * Exercise Types:
   * - listening: Listen and answer multiple choice
   * - pronunciation: Practice pronunciation with speech recognition
   * - fill-blank: Fill in the missing word
   * - translation: Translate a sentence
   * - matching: Match words with translations
   * - sentence-reconstruction: Rearrange words to form a sentence
   */

  loadExercise(exerciseData) {
    this.currentExercise = exerciseData;
    return this.renderExercise(exerciseData);
  }

  renderExercise(exercise) {
    switch (exercise.type) {
      case 'listening':
        return this.renderListeningExercise(exercise);
      case 'pronunciation':
        return this.renderPronunciationExercise(exercise);
      case 'fill-blank':
        return this.renderFillBlankExercise(exercise);
      case 'translation':
        return this.renderTranslationExercise(exercise);
      case 'matching':
        return this.renderMatchingExercise(exercise);
      case 'sentence-reconstruction':
        return this.renderSentenceReconstructionExercise(exercise);
      default:
        return '<p>Unknown exercise type</p>';
    }
  }

  renderListeningExercise(exercise) {
    return `
      <div class="exercise-container listening-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-headphones"></i> Listen and Answer
        </h3>
        <div class="audio-section">
          <audio id="exercise-audio" src="${exercise.audio}"></audio>
          <button class="play-audio-btn" onclick="exerciseManager.playAudio()">
            <i class="fas fa-play"></i> Play Audio
          </button>
        </div>
        <p class="exercise-text">${exercise.text}</p>
        <p class="exercise-translation">${exercise.translation}</p>
        <p class="exercise-question">${exercise.question}</p>
        <div class="options-grid">
          ${exercise.options.map((option, index) => `
            <button class="option-btn" data-index="${index}" onclick="exerciseManager.checkAnswer(${index})">
              ${option}
            </button>
          `).join('')}
        </div>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  renderPronunciationExercise(exercise) {
    return `
      <div class="exercise-container pronunciation-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-microphone"></i> Pronunciation Practice
        </h3>
        <div class="pronunciation-content">
          <p class="target-phrase">${exercise.text}</p>
          <p class="phonetic-text">${exercise.phonetic || ''}</p>
          <button class="record-btn" id="record-btn" onclick="exerciseManager.startRecording()">
            <i class="fas fa-microphone"></i> Click to Record
          </button>
          <p class="recording-hint">Click and speak the phrase above</p>
        </div>
        <div id="pronunciation-result" class="pronunciation-result" style="display: none;">
          <div class="score-display">
            <div class="score-circle">
              <span id="score-value">0</span>%
            </div>
            <p class="score-label">Accuracy</p>
          </div>
          <div class="score-bar-container">
            <div id="score-bar" class="score-bar"></div>
          </div>
        </div>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  renderFillBlankExercise(exercise) {
    const sentenceParts = exercise.sentence.split('__');
    return `
      <div class="exercise-container fill-blank-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-pen"></i> Fill in the Blank
        </h3>
        <div class="sentence-display">
          <p class="sentence-text">
            ${sentenceParts[0]}
            <span class="blank-space" id="blank-space">____</span>
            ${sentenceParts[1] || ''}
          </p>
        </div>
        <div class="options-grid">
          ${exercise.options.map((option, index) => `
            <button class="option-btn" data-index="${index}" onclick="exerciseManager.fillBlank('${option}')">
              ${option}
            </button>
          `).join('')}
        </div>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  renderTranslationExercise(exercise) {
    return `
      <div class="exercise-container translation-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-language"></i> Translation
        </h3>
        <p class="source-text">${exercise.text}</p>
        <textarea
          id="translation-input"
          class="translation-input"
          placeholder="Type your translation here..."
          rows="3"
        ></textarea>
        <button class="check-btn" onclick="exerciseManager.checkTranslation()">
          <i class="fas fa-check"></i> Check Answer
        </button>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  renderMatchingExercise(exercise) {
    return `
      <div class="exercise-container matching-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-link"></i> Match the Pairs
        </h3>
        <div class="matching-grid">
          <div class="column column-left">
            ${exercise.pairs.map((pair, index) => `
              <button class="match-btn" data-side="left" data-index="${index}"
                      onclick="exerciseManager.selectMatch('left', ${index})">
                ${pair.source}
              </button>
            `).join('')}
          </div>
          <div class="column column-right">
            ${exercise.pairs.sort(() => Math.random() - 0.5).map((pair, index) => `
              <button class="match-btn" data-side="right" data-value="${pair.target}"
                      onclick="exerciseManager.selectMatch('right', '${pair.target}')">
                ${pair.target}
              </button>
            `).join('')}
          </div>
        </div>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  renderSentenceReconstructionExercise(exercise) {
    const shuffledWords = [...exercise.words].sort(() => Math.random() - 0.5);
    return `
      <div class="exercise-container reconstruction-exercise">
        <h3 class="exercise-title">
          <i class="fas fa-puzzle-piece"></i> Reconstruct the Sentence
        </h3>
        <div class="target-translation">${exercise.translation}</div>
        <div id="sentence-area" class="sentence-area">
          <p class="instruction">Click words in order:</p>
          <div id="constructed-sentence" class="constructed-sentence"></div>
        </div>
        <div class="word-bank">
          ${shuffledWords.map((word, index) => `
            <button class="word-btn" data-word="${word}" data-index="${index}"
                    onclick="exerciseManager.addWord('${word}', ${index})">
              ${word}
            </button>
          `).join('')}
        </div>
        <button class="check-btn" onclick="exerciseManager.checkSentence()">
          <i class="fas fa-check"></i> Check Answer
        </button>
        <button class="reset-btn" onclick="exerciseManager.resetSentence()">
          <i class="fas fa-redo"></i> Reset
        </button>
        <div id="feedback" class="feedback"></div>
      </div>
    `;
  }

  // Exercise interaction methods
  playAudio() {
    const audio = document.getElementById('exercise-audio');
    if (audio) {
      audio.play();
    }
  }

  checkAnswer(selectedIndex) {
    const exercise = this.currentExercise;
    const isCorrect = selectedIndex === exercise.correct;
    const accuracy = isCorrect ? 100 : 0;

    this.showFeedback(isCorrect, exercise.correctAnswer || exercise.options[exercise.correct]);
    this.highlightAnswer(selectedIndex, isCorrect);

    if (isCorrect) {
      this.progressTracker.completeExercise(`${exercise.id}`, accuracy);
    }

    return isCorrect;
  }

  fillBlank(selectedWord) {
    const exercise = this.currentExercise;
    const isCorrect = selectedWord === exercise.correct;
    const blankSpace = document.getElementById('blank-space');

    if (blankSpace) {
      blankSpace.textContent = selectedWord;
      blankSpace.className = isCorrect ? 'blank-space correct' : 'blank-space incorrect';
    }

    this.showFeedback(isCorrect, exercise.correct);

    if (isCorrect) {
      this.progressTracker.completeExercise(`${exercise.id}`, 100);
    }
  }

  checkTranslation() {
    const input = document.getElementById('translation-input');
    const exercise = this.currentExercise;

    if (!input || !input.value.trim()) {
      this.showFeedback(false, 'Please enter a translation');
      return;
    }

    // Simple similarity check (in production, use more sophisticated NLP)
    const userAnswer = input.value.toLowerCase().trim();
    const correctAnswer = exercise.correctAnswer.toLowerCase();

    // Check if key words are present
    const keyWords = correctAnswer.split(' ').filter(w => w.length > 3);
    const matchedWords = keyWords.filter(word => userAnswer.includes(word));
    const accuracy = Math.round((matchedWords.length / keyWords.length) * 100);

    const isCorrect = accuracy >= 70; // 70% threshold

    this.showFeedback(isCorrect, exercise.correctAnswer, accuracy);

    this.progressTracker.completeExercise(`${exercise.id}`, accuracy);
  }

  // Matching exercise state
  selectedMatches = { left: null, right: null };
  matchedPairs = [];

  selectMatch(side, value) {
    this.selectedMatches[side] = value;

    // Highlight selected buttons
    document.querySelectorAll(`.match-btn[data-side="${side}"]`).forEach(btn => {
      btn.classList.remove('selected');
    });
    event.target.classList.add('selected');

    // Check if both sides are selected
    if (this.selectedMatches.left !== null && this.selectedMatches.right !== null) {
      this.checkMatch();
    }
  }

  checkMatch() {
    const exercise = this.currentExercise;
    const leftIndex = this.selectedMatches.left;
    const rightValue = this.selectedMatches.right;
    const correctPair = exercise.pairs[leftIndex];

    const isCorrect = correctPair.target === rightValue;

    if (isCorrect) {
      this.matchedPairs.push({ left: leftIndex, right: rightValue });

      // Remove matched buttons
      document.querySelectorAll('.match-btn.selected').forEach(btn => {
        btn.classList.add('matched');
        btn.disabled = true;
      });

      // Check if all matched
      if (this.matchedPairs.length === exercise.pairs.length) {
        this.showFeedback(true, 'All pairs matched!');
        this.progressTracker.completeExercise(`${exercise.id}`, 100);
      }
    } else {
      // Remove selection
      document.querySelectorAll('.match-btn.selected').forEach(btn => {
        btn.classList.remove('selected');
      });
    }

    this.selectedMatches = { left: null, right: null };
  }

  // Sentence reconstruction state
  constructedWords = [];

  addWord(word, index) {
    this.constructedWords.push(word);

    // Update display
    const constructed = document.getElementById('constructed-sentence');
    if (constructed) {
      constructed.innerHTML = this.constructedWords.map((w, i) => `
        <span class="added-word" onclick="exerciseManager.removeWord(${i})">${w}</span>
      `).join(' ');
    }

    // Disable button
    event.target.disabled = true;
    event.target.classList.add('used');
  }

  removeWord(index) {
    const word = this.constructedWords[index];
    this.constructedWords.splice(index, 1);

    // Update display
    const constructed = document.getElementById('constructed-sentence');
    if (constructed) {
      constructed.innerHTML = this.constructedWords.map((w, i) => `
        <span class="added-word" onclick="exerciseManager.removeWord(${i})">${w}</span>
      `).join(' ');
    }

    // Re-enable button
    document.querySelectorAll('.word-btn').forEach(btn => {
      if (btn.dataset.word === word && btn.disabled) {
        btn.disabled = false;
        btn.classList.remove('used');
        return;
      }
    });
  }

  resetSentence() {
    this.constructedWords = [];
    document.getElementById('constructed-sentence').innerHTML = '';
    document.querySelectorAll('.word-btn').forEach(btn => {
      btn.disabled = false;
      btn.classList.remove('used');
    });
  }

  checkSentence() {
    const exercise = this.currentExercise;
    const userSentence = this.constructedWords.join(' ');
    const correctSentence = exercise.words.join(' ');

    const isCorrect = userSentence === correctSentence;
    const accuracy = isCorrect ? 100 : 50;

    this.showFeedback(isCorrect, correctSentence);

    if (isCorrect) {
      this.progressTracker.completeExercise(`${exercise.id}`, accuracy);
    }
  }

  // Feedback and UI helpers
  showFeedback(isCorrect, correctAnswer, accuracy) {
    const feedback = document.getElementById('feedback');
    if (!feedback) return;

    feedback.className = `feedback ${isCorrect ? 'correct' : 'incorrect'}`;

    let message = isCorrect
      ? '<i class="fas fa-check-circle"></i> Correct! Excellent work!'
      : `<i class="fas fa-times-circle"></i> Not quite. The correct answer is: ${correctAnswer}`;

    if (accuracy !== undefined && accuracy < 100 && accuracy >= 70) {
      message = `<i class="fas fa-check-circle"></i> Good! Accuracy: ${accuracy}%<br>Correct answer: ${correctAnswer}`;
    }

    feedback.innerHTML = message;
    feedback.style.display = 'block';

    // Show XP gain
    if (isCorrect) {
      const xpGained = accuracy >= 90 ? 20 : 15;
      setTimeout(() => {
        window.showNotification && window.showNotification(`+${xpGained} XP`, 'xp');
      }, 500);
    }
  }

  highlightAnswer(selectedIndex, isCorrect) {
    const buttons = document.querySelectorAll('.option-btn');
    if (buttons.length > 0) {
      buttons[selectedIndex].classList.add(isCorrect ? 'correct' : 'incorrect');

      // Disable all buttons after answer
      buttons.forEach(btn => btn.disabled = true);
    }
  }

  // Speech recognition for pronunciation
  startRecording() {
    if (window.speechRecognition) {
      window.speechRecognition.startRecording(this.currentExercise);
    } else {
      this.showFeedback(false, 'Speech recognition not available in this browser');
    }
  }
}

// Export for use in other modules
if (typeof window !== 'undefined') {
  window.ExerciseManager = ExerciseManager;
}
