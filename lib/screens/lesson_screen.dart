import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:audioplayers/audioplayers.dart';
import '../models/language.dart';
import '../models/lesson.dart';
import '../services/progress_service.dart';
import '../utils/app_localizations.dart';

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

  @override
  void initState() {
    super.initState();
    _currentDay = widget.initialDay;
    _currentLesson = Lesson.create(_currentDay, widget.language);
    _setupAudioPlayer();
    _loadLessonText();
  }

  Future<void> _loadLessonText() async {
    final text = await _currentLesson.loadTextContent();
    setState(() {
      _lessonText = text;
    });
  }

  void _setupAudioPlayer() {
    _audioPlayer.onDurationChanged.listen((duration) {
      setState(() {
        _duration = duration;
      });
    });

    _audioPlayer.onPositionChanged.listen((position) {
      setState(() {
        _position = position;
      });
    });

    _audioPlayer.onPlayerStateChanged.listen((state) {
      setState(() {
        _isPlaying = state == PlayerState.playing;
      });
    });

    _audioPlayer.onPlayerComplete.listen((_) {
      setState(() {
        _isPlaying = false;
        _position = Duration.zero;
      });
    });
  }

  @override
  void dispose() {
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
    });

    _audioPlayer.stop();
    _loadLessonText();
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
                          if (context.mounted) {
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                content: Text(loc.dayMarkedComplete),
                                duration: const Duration(seconds: 2),
                                backgroundColor: Theme.of(context).colorScheme.secondary,
                              ),
                            );
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
                    ),

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
