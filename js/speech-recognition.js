/**
 * Speech Recognition Module
 * Handles pronunciation practice with speech recognition
 */

class SpeechRecognitionManager {
  constructor(progressTracker) {
    this.progressTracker = progressTracker;
    this.recognition = null;
    this.isRecording = false;
    this.initializeRecognition();
  }

  initializeRecognition() {
    // Check if speech recognition is available
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      console.warn('Speech recognition not supported in this browser');
      return;
    }

    this.recognition = new SpeechRecognition();
    this.recognition.continuous = false;
    this.recognition.interimResults = false;
    this.recognition.maxAlternatives = 1;
  }

  setLanguage(languageCode) {
    if (!this.recognition) return;

    // Map language codes to speech recognition locales
    const languageMap = {
      'en': 'en-US',
      'es': 'es-ES',
      'pt': 'pt-BR',
      'fr': 'fr-FR',
      'de': 'de-DE'
    };

    this.recognition.lang = languageMap[languageCode] || 'en-US';
  }

  startRecording(exercise) {
    if (!this.recognition) {
      this.showError('Speech recognition not available');
      return;
    }

    if (this.isRecording) return;

    this.isRecording = true;
    this.updateRecordingUI(true);

    // Set language for the exercise
    this.setLanguage(exercise.language || 'es');

    this.recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      const confidence = event.results[0][0].confidence;

      this.handleRecognitionResult(transcript, confidence, exercise);
    };

    this.recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error);
      this.isRecording = false;
      this.updateRecordingUI(false);

      if (event.error === 'no-speech') {
        this.showError('No speech detected. Please try again.');
      } else if (event.error === 'not-allowed') {
        this.showError('Microphone access denied. Please allow microphone access.');
      } else {
        this.showError('Recognition error. Please try again.');
      }
    };

    this.recognition.onend = () => {
      this.isRecording = false;
      this.updateRecordingUI(false);
    };

    try {
      this.recognition.start();
    } catch (error) {
      console.error('Error starting recognition:', error);
      this.isRecording = false;
      this.updateRecordingUI(false);
      this.showError('Could not start recording. Please try again.');
    }
  }

  handleRecognitionResult(transcript, confidence, exercise) {
    const targetPhrase = exercise.text.toLowerCase().trim();
    const spokenPhrase = transcript.toLowerCase().trim();

    // Calculate accuracy using multiple metrics
    const accuracy = this.calculateAccuracy(targetPhrase, spokenPhrase, confidence);

    // Display results
    this.displayPronunciationScore(accuracy, transcript, targetPhrase);

    // Award XP and badges
    if (accuracy >= 85) {
      this.progressTracker.completeExercise(exercise.id, accuracy);
      this.progressTracker.checkPronunciationBadges(accuracy);
    } else {
      // Award partial credit
      this.progressTracker.addXP(5);
    }

    // Provide feedback
    this.provideFeedback(accuracy, targetPhrase, spokenPhrase);
  }

  calculateAccuracy(target, spoken, confidence) {
    // Weighted scoring system
    const confidenceScore = confidence * 100;

    // Calculate word overlap
    const targetWords = target.split(' ');
    const spokenWords = spoken.split(' ');

    let matchedWords = 0;
    targetWords.forEach(targetWord => {
      if (spokenWords.some(spokenWord => this.wordsMatch(targetWord, spokenWord))) {
        matchedWords++;
      }
    });

    const wordAccuracy = (matchedWords / targetWords.length) * 100;

    // Calculate Levenshtein distance for string similarity
    const similarity = this.calculateSimilarity(target, spoken);

    // Weighted average: 40% confidence, 30% word accuracy, 30% similarity
    const finalScore = (confidenceScore * 0.4) + (wordAccuracy * 0.3) + (similarity * 0.3);

    return Math.round(Math.min(finalScore, 100));
  }

  wordsMatch(word1, word2) {
    // Simple matching with some tolerance for pronunciation variations
    if (word1 === word2) return true;

    // Check if one word contains the other (for prefixes/suffixes)
    if (word1.includes(word2) || word2.includes(word1)) {
      return word1.length > 3 && word2.length > 3;
    }

    // Levenshtein distance for similar words
    const distance = this.levenshteinDistance(word1, word2);
    const maxLength = Math.max(word1.length, word2.length);

    return distance / maxLength <= 0.3; // 30% tolerance
  }

  calculateSimilarity(str1, str2) {
    const distance = this.levenshteinDistance(str1, str2);
    const maxLength = Math.max(str1.length, str2.length);
    const similarity = ((maxLength - distance) / maxLength) * 100;
    return Math.max(0, similarity);
  }

  levenshteinDistance(str1, str2) {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
      matrix[i] = [i];
    }

    for (let j = 0; j <= str1.length; j++) {
      matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
      for (let j = 1; j <= str1.length; j++) {
        if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
          matrix[i][j] = matrix[i - 1][j - 1];
        } else {
          matrix[i][j] = Math.min(
            matrix[i - 1][j - 1] + 1,
            matrix[i][j - 1] + 1,
            matrix[i - 1][j] + 1
          );
        }
      }
    }

    return matrix[str2.length][str1.length];
  }

  displayPronunciationScore(score, transcript, target) {
    const resultDiv = document.getElementById('pronunciation-result');
    const scoreValue = document.getElementById('score-value');
    const scoreBar = document.getElementById('score-bar');

    if (resultDiv) {
      resultDiv.style.display = 'block';
    }

    if (scoreValue) {
      // Animate score counting up
      this.animateScore(scoreValue, 0, score, 1000);
    }

    if (scoreBar) {
      scoreBar.style.width = `${score}%`;
      scoreBar.className = `score-bar ${this.getScoreClass(score)}`;
    }

    // Show transcript comparison
    const feedback = document.getElementById('feedback');
    if (feedback && transcript.toLowerCase() !== target.toLowerCase()) {
      feedback.innerHTML += `
        <div class="transcript-comparison">
          <p><strong>You said:</strong> "${transcript}"</p>
          <p><strong>Target:</strong> "${target}"</p>
        </div>
      `;
    }
  }

  animateScore(element, start, end, duration) {
    const startTime = performance.now();

    const updateScore = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      const currentScore = Math.floor(start + (end - start) * progress);
      element.textContent = currentScore;

      if (progress < 1) {
        requestAnimationFrame(updateScore);
      }
    };

    requestAnimationFrame(updateScore);
  }

  getScoreClass(score) {
    if (score >= 90) return 'excellent';
    if (score >= 75) return 'good';
    if (score >= 60) return 'fair';
    return 'needs-improvement';
  }

  provideFeedback(accuracy, target, spoken) {
    const feedback = document.getElementById('feedback');
    if (!feedback) return;

    let message = '';
    let icon = '';
    let className = '';

    if (accuracy >= 95) {
      icon = '<i class="fas fa-star"></i>';
      message = 'Perfect pronunciation! Outstanding!';
      className = 'feedback correct excellent';
    } else if (accuracy >= 85) {
      icon = '<i class="fas fa-check-circle"></i>';
      message = 'Excellent pronunciation! Keep it up!';
      className = 'feedback correct';
    } else if (accuracy >= 70) {
      icon = '<i class="fas fa-thumbs-up"></i>';
      message = 'Good effort! Try to match the pronunciation more closely.';
      className = 'feedback partial';
    } else {
      icon = '<i class="fas fa-redo"></i>';
      message = 'Keep practicing! Listen carefully and try again.';
      className = 'feedback incorrect';
    }

    feedback.className = className;
    feedback.innerHTML = `${icon} ${message}` + (feedback.innerHTML.includes('transcript-comparison') ? feedback.innerHTML.split('</div>')[1] || '' : '');
  }

  updateRecordingUI(isRecording) {
    const recordBtn = document.getElementById('record-btn');
    if (!recordBtn) return;

    if (isRecording) {
      recordBtn.classList.add('recording');
      recordBtn.innerHTML = '<i class="fas fa-stop"></i> Listening...';
      recordBtn.disabled = true;
    } else {
      recordBtn.classList.remove('recording');
      recordBtn.innerHTML = '<i class="fas fa-microphone"></i> Click to Record';
      recordBtn.disabled = false;
    }
  }

  showError(message) {
    const feedback = document.getElementById('feedback');
    if (feedback) {
      feedback.className = 'feedback incorrect';
      feedback.innerHTML = `<i class="fas fa-exclamation-triangle"></i> ${message}`;
      feedback.style.display = 'block';
    }
  }

  stopRecording() {
    if (this.recognition && this.isRecording) {
      this.recognition.stop();
      this.isRecording = false;
      this.updateRecordingUI(false);
    }
  }
}

// Export for use in other modules
if (typeof window !== 'undefined') {
  window.SpeechRecognitionManager = SpeechRecognitionManager;
}
