import 'package:flutter/material.dart';

class CourseStructure extends StatelessWidget {
  const CourseStructure({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Course Structure',
              style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 16),
            _buildPhase(
              context,
              'Days 1-7',
              'Basic Vocabulary & Essential Phrases',
              'Learn fundamental vocabulary and essential phrases for beginners',
              Colors.blue,
            ),
            const SizedBox(height: 12),
            _buildPhase(
              context,
              'Days 8-15',
              'Advanced Communication',
              'More complex conversations and vocabulary for intermediate learners',
              Colors.green,
            ),
            const SizedBox(height: 12),
            _buildPhase(
              context,
              'Days 16-26',
              'International Living & Working',
              'Practical phrases for global living and professional environments',
              Colors.orange,
            ),
            const SizedBox(height: 12),
            _buildPhase(
              context,
              'Days 27-31',
              'Tech Professional Content',
              'Specialized content for software engineers and tech professionals',
              Colors.purple,
            ),
            const SizedBox(height: 12),
            _buildPhase(
              context,
              'Days 32-50',
              'Advanced Academic & Professional',
              'Advanced language skills for academic and professional settings',
              Colors.red,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildPhase(
    BuildContext context,
    String days,
    String title,
    String description,
    Color color,
  ) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: color.withOpacity(0.3)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 8,
                  vertical: 4,
                ),
                decoration: BoxDecoration(
                  color: color,
                  borderRadius: BorderRadius.circular(4),
                ),
                child: Text(
                  days,
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 12,
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  title,
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Text(
            description,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Colors.grey[700],
                ),
          ),
        ],
      ),
    );
  }
}
