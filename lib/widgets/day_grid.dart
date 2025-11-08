import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/language.dart';
import '../services/progress_service.dart';

class DayGrid extends StatefulWidget {
  final Language language;
  final Function(int) onDaySelected;

  const DayGrid({
    super.key,
    required this.language,
    required this.onDaySelected,
  });

  @override
  State<DayGrid> createState() => _DayGridState();
}

class _DayGridState extends State<DayGrid> {
  int _currentPage = 0;
  final int _daysPerPage = 10;

  @override
  Widget build(BuildContext context) {
    final progressService = Provider.of<ProgressService>(context);
    final startDay = _currentPage * _daysPerPage + 1;
    final endDay = (startDay + _daysPerPage - 1).clamp(1, 50);

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Daily Lessons',
                  style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
                Text(
                  'Days $startDay-$endDay',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        color: Colors.grey[600],
                      ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            GridView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 5,
                crossAxisSpacing: 8,
                mainAxisSpacing: 8,
                childAspectRatio: 1,
              ),
              itemCount: endDay - startDay + 1,
              itemBuilder: (context, index) {
                final day = startDay + index;
                final isCompleted = progressService.isLessonCompleted(widget.language, day);
                final isCurrent = day == progressService.getCurrentDay(widget.language);

                return InkWell(
                  onTap: () => widget.onDaySelected(day),
                  borderRadius: BorderRadius.circular(8),
                  child: Container(
                    decoration: BoxDecoration(
                      color: isCompleted
                          ? Theme.of(context).colorScheme.secondary
                          : isCurrent
                              ? Theme.of(context).colorScheme.primaryContainer
                              : Colors.grey[200],
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(
                        color: isCurrent
                            ? Theme.of(context).colorScheme.primary
                            : Colors.transparent,
                        width: 2,
                      ),
                    ),
                    child: Stack(
                      children: [
                        Center(
                          child: Text(
                            '$day',
                            style: TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                              color: isCompleted
                                  ? Colors.white
                                  : isCurrent
                                      ? Theme.of(context).colorScheme.primary
                                      : Colors.grey[700],
                            ),
                          ),
                        ),
                        if (isCompleted)
                          const Positioned(
                            top: 2,
                            right: 2,
                            child: Icon(
                              Icons.check_circle,
                              size: 16,
                              color: Colors.white,
                            ),
                          ),
                      ],
                    ),
                  ),
                );
              },
            ),
            const SizedBox(height: 16),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                OutlinedButton.icon(
                  onPressed: _currentPage > 0
                      ? () {
                          setState(() {
                            _currentPage--;
                          });
                        }
                      : null,
                  icon: const Icon(Icons.arrow_back),
                  label: const Text('Previous'),
                ),
                Text(
                  'Page ${_currentPage + 1}/5',
                  style: Theme.of(context).textTheme.bodyMedium,
                ),
                OutlinedButton.icon(
                  onPressed: _currentPage < 4
                      ? () {
                          setState(() {
                            _currentPage++;
                          });
                        }
                      : null,
                  icon: const Icon(Icons.arrow_forward),
                  label: const Text('Next'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
