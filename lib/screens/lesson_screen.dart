import 'dart:async';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../models/language.dart';
import '../models/lesson.dart';
import '../services/progress_service.dart';
import '../services/gamification_service.dart';
import '../utils/app_localizations.dart';
import '../theme/app_theme.dart';
import 'practice_screen.dart';

class LessonScreen extends StatefulWidget {
  final Language language;
  final int initialDay;

  const LessonScreen({
    super.key,
    required this.language,
    required this.initialDay,
  });

  @override
  State<LessonScreen> createState() => _LessonScreenState();
}

class _LessonScreenState extends State<LessonScreen> {
  late int _currentDay;
  late Lesson _currentLesson;
  final AudioPlayer _audioPlayer = AudioPlayer();
  bool _isPlaying = false;
  Duration _duration = Duration.zero;
  Duration _position = Duration.zero;
  String _lessonText = '';
  double _playbackSpeed = 1.0;
  bool _isLooping = false;

  bool _showTranslations = false;
  bool _isLoadingContent = false;

  // Stream subscriptions for audio player
  StreamSubscription<Duration>? _durationSubscription;
  StreamSubscription<Duration>? _positionSubscription;
  StreamSubscription<PlayerState>? _playerStateSubscription;
  StreamSubscription<void>? _playerCompleteSubscription;

  @override
  void initState() {
    super.initState();
    _currentDay = widget.initialDay;
    _currentLesson = Lesson.create(_currentDay, widget.language);
    _setupAudioPlayer();
    _loadLessonContent();
  }

  Future<void> _loadLessonContent() async {
    if (!mounted) return;

    setState(() {
      _isLoadingContent = true;
    });

    final text = await _currentLesson.loadTextContent();
    await _currentLesson.loadExercises();
    await _currentLesson.loadVocabulary();

    if (!mounted) return;

    setState(() {
      _lessonText = text;
      _isLoadingContent = false;
    });
  }

  void _setupAudioPlayer() {
    _durationSubscription = _audioPlayer.onDurationChanged.listen((duration) {
      if (mounted) {
        setState(() {
          _duration = duration;
        });
      }
    });

    _positionSubscription = _audioPlayer.onPositionChanged.listen((position) {
      if (mounted) {
        setState(() {
          _position = position;
        });
      }
    });

    _playerStateSubscription = _audioPlayer.onPlayerStateChanged.listen((state) {
      if (mounted) {
        setState(() {
          _isPlaying = state == PlayerState.playing;
        });
      }
    });

    _playerCompleteSubscription = _audioPlayer.onPlayerComplete.listen((_) {
      if (_isLooping) {
        _audioPlayer.seek(Duration.zero);
        _audioPlayer.resume();
      } else {
        if (mounted) {
          setState(() {
            _isPlaying = false;
            _position = Duration.zero;
          });
        }
      }
    });
  }

  Future<void> _setPlaybackSpeed(double speed) async {
    await _audioPlayer.setPlaybackRate(speed);
    setState(() {
      _playbackSpeed = speed;
    });
  }

  void _toggleLoop() {
    setState(() {
      _isLooping = !_isLooping;
    });
  }

  @override
  void dispose() {
    // Cancel all stream subscriptions before disposing the audio player
    _durationSubscription?.cancel();
    _positionSubscription?.cancel();
    _playerStateSubscription?.cancel();
    _playerCompleteSubscription?.cancel();

    // Dispose the audio player
    _audioPlayer.dispose();

    super.dispose();
  }

  Future<void> _playPauseAudio() async {
    if (_isPlaying) {
      await _audioPlayer.pause();
    } else {
      await _audioPlayer.play(AssetSource(_currentLesson.audioPath.replaceFirst('assets/', '')));
    }
  }

  void _changeDay(int newDay) {
    if (newDay < 1 || newDay > 50) return;

    setState(() {
      _currentDay = newDay;
      _currentLesson = Lesson.create(_currentDay, widget.language);
      _position = Duration.zero;
      _isPlaying = false;
      _showTranslations = false;
    });

    _audioPlayer.stop();
    _loadLessonContent();
  }

  String _formatDuration(Duration duration) {
    String twoDigits(int n) => n.toString().padLeft(2, '0');
    final minutes = twoDigits(duration.inMinutes.remainder(60));
    final seconds = twoDigits(duration.inSeconds.remainder(60));
    return '$minutes:$seconds';
  }

  @override
  Widget build(BuildContext context) {
    final progressService = Provider.of<ProgressService>(context);
    final gamificationService = Provider.of<GamificationService>(context);
    final loc = AppLocalizations.of(context);
    final isCompleted = progressService.isLessonCompleted(widget.language, _currentDay);

    return Scaffold(
      appBar: AppBar(
        title: Text('${loc.translate('lesson.day')} $_currentDay'),
        actions: [
          // Language flag indicator
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Chip(
              avatar: Text(
                widget.language.flag,
                style: const TextStyle(fontSize: 20),
              ),
              label: Text(widget.language.name),
              backgroundColor: Colors.white.withValues(alpha: 0.2),
              labelStyle: const TextStyle(color: Colors.white),
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    // Lesson Title & Description
                    Card(
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              _currentLesson.title,
                              style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                  ),
                            ),
                            const SizedBox(height: 8),
                            Text(
                              _currentLesson.description,
                              style: Theme.of(context).textTheme.titleMedium,
                            ),
                            const SizedBox(height: 8),
                            Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 12,
                                vertical: 6,
                              ),
                              decoration: BoxDecoration(
                                color: Theme.of(context).colorScheme.primaryContainer,
                                borderRadius: BorderRadius.circular(20),
                              ),
                              child: Text(
                                _currentLesson.phase,
                                style: TextStyle(
                                  fontSize: 12,
                                  color: Theme.of(context).colorScheme.onPrimaryContainer,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Audio Player
                    Card(
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Column(
                          children: [
                            // Main playback controls
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                IconButton(
                                  icon: const Icon(Icons.replay_10),
                                  onPressed: () {
                                    final newPosition = _position - const Duration(seconds: 10);
                                    _audioPlayer.seek(
                                      newPosition < Duration.zero ? Duration.zero : newPosition,
                                    );
                                  },
                                  iconSize: 32,
                                ),
                                const SizedBox(width: 16),
                                Container(
                                  decoration: BoxDecoration(
                                    color: Theme.of(context).colorScheme.primary,
                                    shape: BoxShape.circle,
                                  ),
                                  child: IconButton(
                                    icon: Icon(
                                      _isPlaying ? Icons.pause : Icons.play_arrow,
                                      color: Colors.white,
                                    ),
                                    onPressed: _playPauseAudio,
                                    iconSize: 48,
                                  ),
                                ),
                                const SizedBox(width: 16),
                                IconButton(
                                  icon: const Icon(Icons.forward_10),
                                  onPressed: () {
                                    final newPosition = _position + const Duration(seconds: 10);
                                    _audioPlayer.seek(
                                      newPosition > _duration ? _duration : newPosition,
                                    );
                                  },
                                  iconSize: 32,
                                ),
                              ],
                            ),
                            const SizedBox(height: 16),

                            // Progress slider
                            Slider(
                              value: _position.inSeconds.toDouble(),
                              max: _duration.inSeconds.toDouble() > 0
                                  ? _duration.inSeconds.toDouble()
                                  : 1.0,
                              onChanged: (value) {
                                _audioPlayer.seek(Duration(seconds: value.toInt()));
                              },
                            ),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Text(_formatDuration(_position)),
                                Text(_formatDuration(_duration)),
                              ],
                            ),

                            const SizedBox(height: 16),
                            const Divider(),
                            const SizedBox(height: 8),

                            // Advanced controls
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                              children: [
                                // Speed control
                                PopupMenuButton<double>(
                                  icon: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      const Icon(Icons.speed, size: 20),
                                      const SizedBox(width: 4),
                                      Text(
                                        '${_playbackSpeed}x',
                                        style: const TextStyle(fontSize: 12),
                                      ),
                                    ],
                                  ),
                                  onSelected: _setPlaybackSpeed,
                                  itemBuilder: (context) => [
                                    const PopupMenuItem(value: 0.5, child: Text('0.5x - Slow')),
                                    const PopupMenuItem(value: 0.75, child: Text('0.75x')),
                                    const PopupMenuItem(value: 1.0, child: Text('1.0x - Normal')),
                                    const PopupMenuItem(value: 1.25, child: Text('1.25x')),
                                    const PopupMenuItem(value: 1.5, child: Text('1.5x - Fast')),
                                    const PopupMenuItem(value: 2.0, child: Text('2.0x - Very Fast')),
                                  ],
                                ),

                                // Loop toggle
                                IconButton(
                                  icon: Icon(
                                    _isLooping ? Icons.repeat_on : Icons.repeat,
                                    color: _isLooping ? AppTheme.primaryBlue : null,
                                  ),
                                  onPressed: _toggleLoop,
                                  tooltip: 'Repeat',
                                ),

                                // Restart button
                                IconButton(
                                  icon: const Icon(Icons.restart_alt),
                                  onPressed: () {
                                    _audioPlayer.seek(Duration.zero);
                                  },
                                  tooltip: 'Restart',
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Lesson Text Content
                    if (_lessonText.isNotEmpty)
                      Card(
                        child: Padding(
                          padding: const EdgeInsets.all(16),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  Icon(
                                    Icons.text_fields,
                                    color: Theme.of(context).colorScheme.primary,
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    'Lesson Content',
                                    style: Theme.of(context).textTheme.titleLarge?.copyWith(
                                          fontWeight: FontWeight.bold,
                                        ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 16),
                              Container(
                                constraints: const BoxConstraints(maxHeight: 400),
                                child: SingleChildScrollView(
                                  child: Text(
                                    _lessonText,
                                    style: Theme.of(context).textTheme.bodyLarge,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),

                    const SizedBox(height: 16),

                    // Practice Section
                    if (_currentLesson.hasExercises)
                      Card(
                        child: Padding(
                          padding: const EdgeInsets.all(16),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              Row(
                                children: [
                                  Icon(
                                    Icons.quiz,
                                    color: Theme.of(context).colorScheme.primary,
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    'Interactive Practice',
                                    style: Theme.of(context).textTheme.titleLarge?.copyWith(
                                          fontWeight: FontWeight.bold,
                                        ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 16),
                              Consumer<ProgressService>(
                                builder: (context, progressService, child) {
                                  final completedCount = progressService.getCompletedExercisesCount(
                                    widget.language,
                                    _currentDay,
                                  );
                                  final totalCount = _currentLesson.totalExercises;
                                  final progress = totalCount > 0 ? completedCount / totalCount : 0.0;

                                  return Column(
                                    crossAxisAlignment: CrossAxisAlignment.stretch,
                                    children: [
                                      Row(
                                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                        children: [
                                          Text(
                                            'Progress:',
                                            style: Theme.of(context).textTheme.titleMedium,
                                          ),
                                          Text(
                                            '$completedCount / $totalCount exercises',
                                            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                                  color: Theme.of(context).colorScheme.primary,
                                                  fontWeight: FontWeight.bold,
                                                ),
                                          ),
                                        ],
                                      ),
                                      const SizedBox(height: 8),
                                      LinearProgressIndicator(
                                        value: progress,
                                        minHeight: 8,
                                        borderRadius: BorderRadius.circular(4),
                                      ),
                                      const SizedBox(height: 16),
                                      ElevatedButton.icon(
                                        onPressed: () {
                                          Navigator.push(
                                            context,
                                            MaterialPageRoute(
                                              builder: (context) => PracticeScreen(
                                                lesson: _currentLesson,
                                                language: widget.language,
                                              ),
                                            ),
                                          );
                                        },
                                        icon: const Icon(Icons.play_arrow),
                                        label: Text(
                                          completedCount == 0
                                              ? 'Start Practice'
                                              : completedCount == totalCount
                                                  ? 'Review Exercises'
                                                  : 'Continue Practice',
                                        ),
                                        style: ElevatedButton.styleFrom(
                                          padding: const EdgeInsets.all(16),
                                          backgroundColor: Theme.of(context).colorScheme.secondary,
                                          foregroundColor: Colors.white,
                                        ),
                                      ),
                                    ],
                                  );
                                },
                              ),
                            ],
                          ),
                        ),
                      ),

                    if (_currentLesson.hasExercises) const SizedBox(height: 16),

                    // Vocabulary Section
                    if (_currentLesson.hasVocabulary)
                      Card(
                        child: Padding(
                          padding: const EdgeInsets.all(16),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Row(
                                    children: [
                                      Icon(
                                        Icons.book,
                                        color: Theme.of(context).colorScheme.primary,
                                      ),
                                      const SizedBox(width: 8),
                                      Text(
                                        'Vocabulary',
                                        style: Theme.of(context).textTheme.titleLarge?.copyWith(
                                              fontWeight: FontWeight.bold,
                                            ),
                                      ),
                                    ],
                                  ),
                                  TextButton.icon(
                                    onPressed: () {
                                      setState(() {
                                        _showTranslations = !_showTranslations;
                                      });
                                    },
                                    icon: Icon(_showTranslations ? Icons.visibility_off : Icons.visibility),
                                    label: Text(_showTranslations ? 'Hide' : 'Show'),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 16),
                              ..._currentLesson.vocabulary!.map((vocab) {
                                return Padding(
                                  padding: const EdgeInsets.only(bottom: 12),
                                  child: Container(
                                    padding: const EdgeInsets.all(12),
                                    decoration: BoxDecoration(
                                      border: Border.all(color: Colors.grey.shade300),
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: Column(
                                      crossAxisAlignment: CrossAxisAlignment.start,
                                      children: [
                                        Row(
                                          children: [
                                            Expanded(
                                              child: Text(
                                                vocab.word,
                                                style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                                      fontWeight: FontWeight.bold,
                                                    ),
                                              ),
                                            ),
                                            if (vocab.phonetic != null)
                                              Text(
                                                vocab.phonetic!,
                                                style: TextStyle(
                                                  color: Colors.grey.shade600,
                                                  fontStyle: FontStyle.italic,
                                                ),
                                              ),
                                          ],
                                        ),
                                        if (_showTranslations) ...[
                                          const SizedBox(height: 8),
                                          Text(
                                            vocab.translation,
                                            style: TextStyle(
                                              color: Theme.of(context).colorScheme.primary,
                                            ),
                                          ),
                                        ],
                                        if (vocab.example != null && _showTranslations) ...[
                                          const SizedBox(height: 8),
                                          Container(
                                            padding: const EdgeInsets.all(8),
                                            decoration: BoxDecoration(
                                              color: Colors.grey.shade100,
                                              borderRadius: BorderRadius.circular(4),
                                            ),
                                            child: Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              children: [
                                                Text(
                                                  vocab.example!,
                                                  style: const TextStyle(fontStyle: FontStyle.italic),
                                                ),
                                                if (vocab.exampleTranslation != null) ...[
                                                  const SizedBox(height: 4),
                                                  Text(
                                                    vocab.exampleTranslation!,
                                                    style: TextStyle(
                                                      fontSize: 12,
                                                      color: Colors.grey.shade600,
                                                    ),
                                                  ),
                                                ],
                                              ],
                                            ),
                                          ),
                                        ],
                                      ],
                                    ),
                                  ),
                                );
                              }),
                            ],
                          ),
                        ),
                      ),

                    if (_currentLesson.hasVocabulary) const SizedBox(height: 16),

                    // Mark Complete Button
                    ElevatedButton.icon(
                      onPressed: () async {
                        if (isCompleted) {
                          await progressService.unmarkLessonComplete(
                            widget.language,
                            _currentDay,
                          );
                        } else {
                          await progressService.markLessonComplete(
                            widget.language,
                            _currentDay,
                          );
                          // Record in gamification service
                          await gamificationService.recordLessonCompletion(widget.language);

                          if (context.mounted) {
                            // Show completion message
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                content: Text(loc.dayMarkedComplete),
                                duration: const Duration(seconds: 2),
                                backgroundColor: Theme.of(context).colorScheme.secondary,
                              ),
                            );

                            // Show achievement notifications if any
                            if (gamificationService.recentlyUnlocked.isNotEmpty) {
                              for (var achievement in gamificationService.recentlyUnlocked) {
                                await Future.delayed(const Duration(milliseconds: 500));
                                if (context.mounted) {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    SnackBar(
                                      content: Row(
                                        children: [
                                          Icon(achievement.icon, color: Colors.white),
                                          const SizedBox(width: 12),
                                          Expanded(
                                            child: Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              mainAxisSize: MainAxisSize.min,
                                              children: [
                                                const Text(
                                                  'Achievement Unlocked!',
                                                  style: TextStyle(
                                                    fontWeight: FontWeight.bold,
                                                    color: Colors.white,
                                                  ),
                                                ),
                                                Text(
                                                  achievement.title,
                                                  style: const TextStyle(color: Colors.white),
                                                ),
                                              ],
                                            ),
                                          ),
                                        ],
                                      ),
                                      duration: const Duration(seconds: 3),
                                      backgroundColor: achievement.color,
                                    ),
                                  );
                                }
                              }
                            }
                          }
                        }
                      },
                      icon: Icon(isCompleted ? Icons.check_circle : Icons.check_circle_outline),
                      label: Text(isCompleted ? loc.completed : loc.markComplete),
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.all(16),
                        backgroundColor: isCompleted
                            ? Theme.of(context).colorScheme.secondary
                            : Theme.of(context).colorScheme.primary,
                        foregroundColor: Colors.white,
                      ),
                    ).animate().scale(delay: 100.ms),

                    const SizedBox(height: 24),

                    // Navigation Buttons
                    Row(
                      children: [
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: _currentDay > 1
                                ? () => _changeDay(_currentDay - 1)
                                : null,
                            icon: const Icon(Icons.arrow_back),
                            label: Text(loc.previousDay),
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: _currentDay < 50
                                ? () => _changeDay(_currentDay + 1)
                                : null,
                            icon: const Icon(Icons.arrow_forward),
                            label: Text(loc.nextDay),
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
