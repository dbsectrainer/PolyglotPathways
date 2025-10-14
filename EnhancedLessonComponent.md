import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, Mic, MicOff, Trophy, Star, Target, Clock } from 'lucide-react';

const EnhancedLessonComponent = () => {
// State management for enhanced features
const [currentExercise, setCurrentExercise] = useState(0);
const [userProgress, setUserProgress] = useState({
xp: 1250,
streak: 7,
level: 5,
badges: ['first-lesson', 'week-streak', 'perfect-pronunciation']
});
const [isRecording, setIsRecording] = useState(false);
const [pronunciationScore, setPronunciationScore] = useState(null);
const [exerciseType, setExerciseType] = useState('listening');
const [userAnswer, setUserAnswer] = useState('');
const [feedback, setFeedback] = useState('');
const [isCorrect, setIsCorrect] = useState(null);

// Audio and speech recognition refs
const audioRef = useRef(null);
const recognitionRef = useRef(null);

// Sample lesson data with multiple exercise types
const lessonData = {
day: 15,
topic: "Business Meeting Vocabulary",
language: "Spanish",
exercises: [
{
type: 'listening',
audio: '/audio/business_meeting.mp3',
text: "La reunión comenzará a las nueve en punto.",
translation: "The meeting will start at nine o'clock sharp.",
question: "¿A qué hora comenzará la reunión?",
options: ["A las ocho", "A las nueve", "A las diez", "A las once"],
correct: 1
},
{
type: 'pronunciation',
text: "La reunión comenzará a las nueve en punto",
phonetic: "[la re.u'njon ko.men.sa'ɾa a las 'nwe.βe en 'pun.to]",
targetAccuracy: 85
},
{
type: 'fill-blank',
sentence: "La **\_** comenzará a las nueve en punto.",
options: ["reunión", "comida", "fiesta", "clase"],
correct: "reunión"
},
{
type: 'translation',
text: "The meeting will start at nine o'clock sharp.",
correctAnswer: "La reunión comenzará a las nueve en punto."
}
]
};

const currentEx = lessonData.exercises[currentExercise];

// Gamification functions
const awardXP = (amount) => {
setUserProgress(prev => ({
...prev,
xp: prev.xp + amount,
level: Math.floor((prev.xp + amount) / 250) + 1
}));
};

const checkBadge = (type) => {
const newBadges = [...userProgress.badges];
if (type === 'perfect-pronunciation' && pronunciationScore >= 95) {
if (!newBadges.includes('pronunciation-master')) {
newBadges.push('pronunciation-master');
setUserProgress(prev => ({ ...prev, badges: newBadges }));
}
}
};

// Speech recognition for pronunciation practice
const startSpeechRecognition = () => {
if ('webkitSpeechRecognition' in window) {
setIsRecording(true);
const recognition = new window.webkitSpeechRecognition();
recognition.lang = 'es-ES';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        const confidence = event.results[0][0].confidence;

        // Simple pronunciation scoring (in real app, use advanced algorithms)
        const score = Math.round(confidence * 100);
        setPronunciationScore(score);

        if (score >= currentEx.targetAccuracy) {
          setFeedback('¡Excelente pronunciación!');
          awardXP(20);
          checkBadge('perfect-pronunciation');
        } else {
          setFeedback('Buena pronunciación. ¡Inténtalo de nuevo!');
          awardXP(10);
        }
        setIsRecording(false);
      };

      recognition.onerror = () => {
        setIsRecording(false);
        setFeedback('Error de reconocimiento. Inténtalo de nuevo.');
      };

      recognition.start();
      recognitionRef.current = recognition;
    }

};

// Handle different exercise types
const handleAnswer = (answer) => {
setUserAnswer(answer);
let correct = false;

    switch (currentEx.type) {
      case 'listening':
        correct = answer === currentEx.options[currentEx.correct];
        break;
      case 'fill-blank':
        correct = answer === currentEx.correct;
        break;
      case 'translation':
        // Simple similarity check (in real app, use NLP)
        correct = answer.toLowerCase().includes(currentEx.correctAnswer.toLowerCase().slice(0, 10));
        break;
    }

    setIsCorrect(correct);
    if (correct) {
      setFeedback('¡Correcto! ¡Excelente trabajo!');
      awardXP(15);
    } else {
      setFeedback('No es correcto. ¡Inténtalo de nuevo!');
    }

};

const nextExercise = () => {
if (currentExercise < lessonData.exercises.length - 1) {
setCurrentExercise(prev => prev + 1);
setUserAnswer('');
setFeedback('');
setIsCorrect(null);
setPronunciationScore(null);
}
};

const playAudio = () => {
if (audioRef.current) {
audioRef.current.play();
}
};

return (
<div className="max-w-4xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen">
{/_ Header with Progress _/}
<div className="bg-white rounded-xl shadow-lg p-6 mb-6">
<div className="flex justify-between items-center mb-4">
<div>
<h1 className="text-2xl font-bold text-gray-800">Day {lessonData.day}: {lessonData.topic}</h1>
<p className="text-gray-600">{lessonData.language} • Exercise {currentExercise + 1} of {lessonData.exercises.length}</p>
</div>
<div className="flex items-center space-x-4">
<div className="flex items-center space-x-2">
<Star className="text-yellow-500" size={20} />
<span className="font-semibold">{userProgress.xp} XP</span>
</div>
<div className="flex items-center space-x-2">
<Target className="text-orange-500" size={20} />
<span className="font-semibold">Level {userProgress.level}</span>
</div>
<div className="flex items-center space-x-2">
<Trophy className="text-blue-500" size={20} />
<span className="font-semibold">{userProgress.streak} day streak</span>
</div>
</div>
</div>

        {/* Progress Bar */}
        {% raw %}
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div
            className="bg-gradient-to-r from-blue-500 to-indigo-600 h-3 rounded-full transition-all duration-300"
            style={{ width: `${((currentExercise + 1) / lessonData.exercises.length) * 100}%` }}
          ></div>
        </div>
        {% endraw %}
      </div>

      {/* Exercise Content */}
      <div className="bg-white rounded-xl shadow-lg p-8">
        {/* Listening Exercise */}
        {currentEx.type === 'listening' && (
          <div className="text-center">
            <h2 className="text-xl font-semibold mb-6">Listen and Answer</h2>

            {/* Audio Player */}
            <div className="mb-6">
              <audio ref={audioRef} src={currentEx.audio} />
              <button
                onClick={playAudio}
                className="bg-blue-500 hover:bg-blue-600 text-white rounded-full p-4 transition-colors"
              >
                <Play size={24} />
              </button>
            </div>

            <p className="text-lg mb-4 font-medium">{currentEx.text}</p>
            <p className="text-gray-600 mb-6">{currentEx.translation}</p>
            <p className="text-lg mb-6">{currentEx.question}</p>

            {/* Multiple Choice Options */}
            <div className="grid grid-cols-2 gap-4">
              {currentEx.options.map((option, index) => (
                <button
                  key={index}
                  onClick={() => handleAnswer(option)}
                  className={`p-4 rounded-lg border-2 transition-all ${
                    userAnswer === option
                      ? isCorrect === true
                        ? 'border-green-500 bg-green-50'
                        : isCorrect === false
                        ? 'border-red-500 bg-red-50'
                        : 'border-blue-500 bg-blue-50'
                      : 'border-gray-300 hover:border-blue-300'
                  }`}
                >
                  {option}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Pronunciation Exercise */}
        {currentEx.type === 'pronunciation' && (
          <div className="text-center">
            <h2 className="text-xl font-semibold mb-6">Pronunciation Practice</h2>

            <div className="mb-6">
              <p className="text-2xl font-semibold mb-2">{currentEx.text}</p>
              <p className="text-gray-600 mb-4">{currentEx.phonetic}</p>

              {/* Microphone Button */}
              <button
                onClick={startSpeechRecognition}
                className={`rounded-full p-6 transition-all ${
                  isRecording
                    ? 'bg-red-500 hover:bg-red-600 animate-pulse'
                    : 'bg-green-500 hover:bg-green-600'
                } text-white`}
                disabled={isRecording}
              >
                {isRecording ? <MicOff size={32} /> : <Mic size={32} />}
              </button>

              <p className="mt-4 text-gray-600">
                {isRecording ? 'Listening...' : 'Click to record your pronunciation'}
              </p>
            </div>

            {/* Pronunciation Score */}
            {% raw %}
            {pronunciationScore !== null && (
              <div className="mb-6">
                <div className="text-3xl font-bold mb-2">
                  <span className={pronunciationScore >= 85 ? 'text-green-500' : 'text-orange-500'}>
                    {pronunciationScore}%
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className={`h-3 rounded-full transition-all duration-500 ${
                      pronunciationScore >= 85 ? 'bg-green-500' : 'bg-orange-500'
                    }`}
                    style={{ width: `${pronunciationScore}%` }}
                  ></div>
                </div>
              </div>
            )}
            {% endraw %}
          </div>
        )}

        {/* Fill in the Blank Exercise */}
        {currentEx.type === 'fill-blank' && (
          <div className="text-center">
            <h2 className="text-xl font-semibold mb-6">Fill in the Blank</h2>

            <p className="text-xl mb-6">{currentEx.sentence}</p>

            <div className="grid grid-cols-2 gap-4 max-w-md mx-auto">
              {currentEx.options.map((option, index) => (
                <button
                  key={index}
                  onClick={() => handleAnswer(option)}
                  className={`p-3 rounded-lg border-2 transition-all ${
                    userAnswer === option
                      ? isCorrect === true
                        ? 'border-green-500 bg-green-50'
                        : isCorrect === false
                        ? 'border-red-500 bg-red-50'
                        : 'border-blue-500 bg-blue-50'
                      : 'border-gray-300 hover:border-blue-300'
                  }`}
                >
                  {option}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Translation Exercise */}
        {currentEx.type === 'translation' && (
          <div className="text-center">
            <h2 className="text-xl font-semibold mb-6">Translation</h2>

            <p className="text-xl mb-6">{currentEx.text}</p>

            <textarea
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="Type your translation here..."
              className="w-full max-w-lg p-4 border-2 border-gray-300 rounded-lg resize-none focus:border-blue-500 focus:outline-none"
              rows="3"
            />

            <div className="mt-4">
              <button
                onClick={() => handleAnswer(userAnswer)}
                className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-lg transition-colors"
              >
                Check Answer
              </button>
            </div>
          </div>
        )}

        {/* Feedback */}
        {feedback && (
          <div className={`mt-6 p-4 rounded-lg text-center ${
            isCorrect === true ? 'bg-green-100 text-green-800' :
            isCorrect === false ? 'bg-red-100 text-red-800' :
            'bg-blue-100 text-blue-800'
          }`}>
            <p className="font-semibold">{feedback}</p>
          </div>
        )}

        {/* Navigation */}
        <div className="flex justify-between items-center mt-8">
          <button
            onClick={() => setCurrentExercise(Math.max(0, currentExercise - 1))}
            disabled={currentExercise === 0}
            className="px-6 py-3 bg-gray-300 text-gray-700 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-400 transition-colors"
          >
            Previous
          </button>

          <span className="text-gray-600">
            {currentExercise + 1} / {lessonData.exercises.length}
          </span>

          <button
            onClick={nextExercise}
            disabled={currentExercise === lessonData.exercises.length - 1}
            className="px-6 py-3 bg-blue-500 text-white rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:bg-blue-600 transition-colors"
          >
            {currentExercise === lessonData.exercises.length - 1 ? 'Complete' : 'Next'}
          </button>
        </div>
      </div>

      {/* Achievement Badges */}
      <div className="mt-6 bg-white rounded-xl shadow-lg p-6">
        <h3 className="text-lg font-semibold mb-4">Your Achievements</h3>
        <div className="flex space-x-4">
          {userProgress.badges.map((badge, index) => (
            <div key={index} className="flex flex-col items-center">
              <div className="w-12 h-12 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center">
                <Trophy className="text-white" size={20} />
              </div>
              <span className="text-xs mt-1 text-gray-600 capitalize">
                {badge.replace('-', ' ')}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>

);
};

export default EnhancedLessonComponent;
