import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/language.dart';
import '../models/lesson.dart';
import '../models/exercise.dart';
import '../services/progress_service.dart';
import '../utils/app_localizations.dart';

class PracticeScreen extends StatefulWidget {
  final Lesson lesson;
  final Language language;

  const PracticeScreen({
    super.key,
    required this.lesson,
    required this.language,
  });

  @override
  State<PracticeScreen> createState() => _PracticeScreenState();
}

class _PracticeScreenState extends State<PracticeScreen> {
  int _currentExerciseIndex = 0;
  Map<String, dynamic> _userAnswers = {};
  Map<String, bool> _exerciseResults = {};
  bool _showFeedback = false;
  bool _allExercisesCompleted = false;

  @override
  void initState() {
    super.initState();
    // Initialize with already completed exercises
    final progressService = Provider.of<ProgressService>(context, listen: false);
    final completedIds = progressService.getCompletedExerciseIds(
      widget.language,
      widget.lesson.day,
    );

    for (final exerciseId in completedIds) {
      _exerciseResults[exerciseId] = true;
    }
  }

  Exercise get _currentExercise => widget.lesson.exercises![_currentExerciseIndex];

  bool get _canProceed => _exerciseResults[_currentExercise.id] == true;

  int get _completedCount => _exerciseResults.values.where((v) => v == true).length;

  int get _totalExercises => widget.lesson.exercises?.length ?? 0;

  void _submitAnswer() {
    final answer = _userAnswers[_currentExercise.id];
    if (answer == null) return;

    final isCorrect = _currentExercise.checkAnswer(answer);

    setState(() {
      _exerciseResults[_currentExercise.id] = isCorrect;
      _showFeedback = true;
    });

    if (isCorrect) {
      final progressService = Provider.of<ProgressService>(context, listen: false);
      progressService.markExerciseComplete(
        widget.language,
        widget.lesson.day,
        _currentExercise.id,
      );
    }
  }

  void _nextExercise() {
    if (_currentExerciseIndex < _totalExercises - 1) {
      setState(() {
        _currentExerciseIndex++;
        _showFeedback = false;
      });
    } else {
      setState(() {
        _allExercisesCompleted = true;
      });
    }
  }

  void _previousExercise() {
    if (_currentExerciseIndex > 0) {
      setState(() {
        _currentExerciseIndex--;
        _showFeedback = false;
      });
    }
  }

  Widget _buildExerciseWidget() {
    final exercise = _currentExercise;

    if (exercise is MultipleChoiceExercise) {
      return _buildMultipleChoice(exercise);
    } else if (exercise is FillInBlankExercise) {
      return _buildFillInBlank(exercise);
    } else if (exercise is MatchingExercise) {
      return _buildMatching(exercise);
    } else if (exercise is TranslationExercise) {
      return _buildTranslation(exercise);
    }

    return const Text('Unknown exercise type');
  }

  Widget _buildMultipleChoice(MultipleChoiceExercise exercise) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          exercise.question,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        const SizedBox(height: 24),
        ...List.generate(exercise.options.length, (index) {
          final isSelected = _userAnswers[exercise.id] == index;
          final showResult = _showFeedback && isSelected;
          final isCorrect = index == exercise.correctOptionIndex;

          return Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: OutlinedButton(
              onPressed: _showFeedback
                  ? null
                  : () {
                      setState(() {
                        _userAnswers[exercise.id] = index;
                      });
                    },
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.all(16),
                backgroundColor: showResult
                    ? (_exerciseResults[exercise.id] == true
                        ? Colors.green.withValues(alpha: 0.1)
                        : Colors.red.withValues(alpha: 0.1))
                    : (isSelected
                        ? Theme.of(context).colorScheme.primaryContainer
                        : null),
                side: BorderSide(
                  color: showResult
                      ? (_exerciseResults[exercise.id] == true
                          ? Colors.green
                          : Colors.red)
                      : (isSelected
                          ? Theme.of(context).colorScheme.primary
                          : Colors.grey),
                  width: 2,
                ),
              ),
              child: Row(
                children: [
                  Expanded(
                    child: Text(
                      exercise.options[index],
                      style: TextStyle(
                        color: showResult
                            ? (_exerciseResults[exercise.id] == true
                                ? Colors.green.shade700
                                : Colors.red.shade700)
                            : null,
                      ),
                    ),
                  ),
                  if (showResult)
                    Icon(
                      _exerciseResults[exercise.id] == true
                          ? Icons.check_circle
                          : Icons.cancel,
                      color: _exerciseResults[exercise.id] == true
                          ? Colors.green
                          : Colors.red,
                    ),
                  if (_showFeedback && isCorrect && !isSelected)
                    const Icon(Icons.check_circle, color: Colors.green),
                ],
              ),
            ),
          );
        }),
      ],
    );
  }

  Widget _buildFillInBlank(FillInBlankExercise exercise) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          exercise.question,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        const SizedBox(height: 24),
        TextField(
          enabled: !_showFeedback,
          onChanged: (value) {
            setState(() {
              _userAnswers[exercise.id] = value;
            });
          },
          decoration: InputDecoration(
            hintText: 'Type your answer here...',
            border: const OutlineInputBorder(),
            suffixIcon: _showFeedback
                ? Icon(
                    _exerciseResults[exercise.id] == true
                        ? Icons.check_circle
                        : Icons.cancel,
                    color: _exerciseResults[exercise.id] == true
                        ? Colors.green
                        : Colors.red,
                  )
                : null,
          ),
        ),
        if (_showFeedback && _exerciseResults[exercise.id] == false)
          Padding(
            padding: const EdgeInsets.only(top: 12),
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.green.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: Colors.green),
              ),
              child: Text(
                'Correct answer: ${exercise.correctAnswer}',
                style: TextStyle(
                  color: Colors.green.shade700,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildMatching(MatchingExercise exercise) {
    final leftItems = exercise.pairs.map((p) => p.left).toList();
    final rightItems = exercise.pairs.map((p) => p.right).toList()..shuffle();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          exercise.question,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        const SizedBox(height: 24),
        const Text('Match the items (tap to select, then tap the matching item):'),
        const SizedBox(height: 16),
        // For simplicity, showing a message - full implementation would need drag-and-drop
        const Text(
          'Matching exercise UI - Tap items to connect them',
          style: TextStyle(fontStyle: FontStyle.italic),
        ),
        // Simplified version: display pairs
        ...exercise.pairs.map((pair) {
          return Card(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Row(
                children: [
                  Expanded(child: Text(pair.left)),
                  const Icon(Icons.arrow_forward),
                  Expanded(child: Text(pair.right)),
                ],
              ),
            ),
          );
        }),
      ],
    );
  }

  Widget _buildTranslation(TranslationExercise exercise) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          exercise.question,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        const SizedBox(height: 24),
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: Theme.of(context).colorScheme.primaryContainer,
            borderRadius: BorderRadius.circular(8),
          ),
          child: Text(
            exercise.targetText,
            style: Theme.of(context).textTheme.titleLarge,
            textAlign: TextAlign.center,
          ),
        ),
        const SizedBox(height: 24),
        TextField(
          enabled: !_showFeedback,
          onChanged: (value) {
            setState(() {
              _userAnswers[exercise.id] = value;
            });
          },
          decoration: InputDecoration(
            hintText: 'Type your translation...',
            border: const OutlineInputBorder(),
            suffixIcon: _showFeedback
                ? Icon(
                    _exerciseResults[exercise.id] == true
                        ? Icons.check_circle
                        : Icons.cancel,
                    color: _exerciseResults[exercise.id] == true
                        ? Colors.green
                        : Colors.red,
                  )
                : null,
          ),
          maxLines: 3,
        ),
        if (_showFeedback && _exerciseResults[exercise.id] == false)
          Padding(
            padding: const EdgeInsets.only(top: 12),
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.green.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: Colors.green),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Correct translation:',
                    style: TextStyle(
                      color: Colors.green.shade700,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    exercise.correctTranslation,
                    style: TextStyle(color: Colors.green.shade700),
                  ),
                ],
              ),
            ),
          ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    final loc = AppLocalizations.of(context);

    if (_allExercisesCompleted) {
      return Scaffold(
        appBar: AppBar(
          title: Text('Practice - ${loc.translate('lesson.day')} ${widget.lesson.day}'),
        ),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.celebration,
                  size: 100,
                  color: Theme.of(context).colorScheme.primary,
                ),
                const SizedBox(height: 24),
                Text(
                  'Congratulations!',
                  style: Theme.of(context).textTheme.headlineMedium,
                ),
                const SizedBox(height: 16),
                Text(
                  'You\'ve completed all exercises for this lesson!',
                  style: Theme.of(context).textTheme.titleMedium,
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 16),
                Text(
                  '$_completedCount / $_totalExercises exercises completed',
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                ),
                const SizedBox(height: 32),
                ElevatedButton.icon(
                  onPressed: () => Navigator.pop(context),
                  icon: const Icon(Icons.arrow_back),
                  label: const Text('Back to Lesson'),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 32,
                      vertical: 16,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('Practice - ${loc.translate('lesson.day')} ${widget.lesson.day}'),
        actions: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Chip(
              avatar: Text(
                widget.language.flag,
                style: const TextStyle(fontSize: 16),
              ),
              label: Text(
                '$_completedCount / $_totalExercises',
                style: const TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          // Progress indicator
          LinearProgressIndicator(
            value: _totalExercises > 0 ? _completedCount / _totalExercises : 0,
            minHeight: 8,
          ),
          Expanded(
            child: SingleChildScrollView(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    // Exercise counter
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(
                          'Exercise ${_currentExerciseIndex + 1} of $_totalExercises',
                          style: Theme.of(context).textTheme.titleMedium,
                        ),
                        if (_exerciseResults[_currentExercise.id] == true)
                          const Chip(
                            avatar: Icon(Icons.check, size: 16),
                            label: Text('Completed'),
                            backgroundColor: Colors.green,
                            labelStyle: TextStyle(color: Colors.white),
                          ),
                      ],
                    ),
                    const SizedBox(height: 24),

                    // Exercise content
                    _buildExerciseWidget(),

                    const SizedBox(height: 32),

                    // Feedback message
                    if (_showFeedback)
                      Container(
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: _exerciseResults[_currentExercise.id] == true
                              ? Colors.green.withValues(alpha: 0.1)
                              : Colors.red.withValues(alpha: 0.1),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(
                            color: _exerciseResults[_currentExercise.id] == true
                                ? Colors.green
                                : Colors.red,
                            width: 2,
                          ),
                        ),
                        child: Row(
                          children: [
                            Icon(
                              _exerciseResults[_currentExercise.id] == true
                                  ? Icons.check_circle
                                  : Icons.cancel,
                              color: _exerciseResults[_currentExercise.id] == true
                                  ? Colors.green
                                  : Colors.red,
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Text(
                                _exerciseResults[_currentExercise.id] == true
                                    ? 'Excellent! That\'s correct!'
                                    : 'Not quite right. Try reviewing the lesson content.',
                                style: TextStyle(
                                  color: _exerciseResults[_currentExercise.id] == true
                                      ? Colors.green.shade700
                                      : Colors.red.shade700,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),

                    const SizedBox(height: 24),

                    // Action buttons
                    if (!_showFeedback)
                      ElevatedButton(
                        onPressed: _userAnswers.containsKey(_currentExercise.id)
                            ? _submitAnswer
                            : null,
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.all(16),
                        ),
                        child: const Text('Submit Answer'),
                      ),

                    if (_showFeedback)
                      ElevatedButton(
                        onPressed: _canProceed ? _nextExercise : null,
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.all(16),
                        ),
                        child: Text(
                          _currentExerciseIndex < _totalExercises - 1
                              ? 'Next Exercise'
                              : 'Finish Practice',
                        ),
                      ),

                    const SizedBox(height: 16),

                    // Navigation buttons
                    Row(
                      children: [
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: _currentExerciseIndex > 0 ? _previousExercise : null,
                            icon: const Icon(Icons.arrow_back),
                            label: const Text('Previous'),
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: _currentExerciseIndex < _totalExercises - 1
                                ? _nextExercise
                                : null,
                            icon: const Icon(Icons.arrow_forward),
                            label: const Text('Skip'),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
