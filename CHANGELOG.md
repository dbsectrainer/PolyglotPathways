# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added - 2025-11-08
#### UI/UX Improvements
- **Modal Bottom Sheet for Daily Lessons**: Replaced two-step interaction (tap language → scroll → select day) with immediate modal bottom sheet presentation
  - Created `DailyLessonsSheet` widget with beautiful slide-up animation
  - Drag-to-dismiss functionality for natural mobile interaction
  - Shows language flag, name, and progress in header
  - Paginated day grid (5 pages of 10 days each, covering 50 lessons)
  - Eliminated need for scrolling to access daily lessons
  - Improved visual hierarchy with focused, distraction-free lesson selection

#### Interactive Learning Features
- **Practice Screen with Multiple Exercise Types**:
  - Multiple choice questions with instant feedback
  - Fill-in-the-blank exercises
  - Translation exercises with real-time validation
  - Matching exercises for vocabulary building
- **Vocabulary Section**:
  - Interactive vocabulary cards with phonetics
  - Show/hide translation toggle for active learning
  - Example sentences for context
- **Exercise Progress Tracking**:
  - Real-time progress indicators (X/Y exercises completed)
  - Persistent storage of exercise completion
  - Smart practice buttons (Start/Continue/Review)
  - Completion celebration screen
  - Navigation between exercises with skip functionality
- **Sample Content**:
  - Added exercises for Days 1-3 (Greetings, Numbers, Days/Months)
  - Added vocabulary with phonetics for Days 1-3
  - 8 exercises per lesson covering different question types

#### Gamification & Progress
- **Achievement System**:
  - 17 unique achievements across categories (Streak, Learning, Completion, Practice)
  - Confetti celebration animation on unlock
  - Achievement gallery with tabbed categories
  - Progress tracking for partial achievements
- **Streak Tracking**:
  - Current streak counter with fire icon
  - Longest streak record
  - Total lessons completed
  - Date-based streak persistence
- **Daily Goals**:
  - Customizable daily lesson goals (1-10 lessons)
  - Visual progress bar with completion percentage
  - Celebration message when goal achieved
  - Integration with streak system

#### Navigation & Onboarding
- **Bottom Navigation**:
  - 4 main tabs: Home, Achievements, Profile, Settings
  - Badge indicators for new achievements
  - Smooth tab transitions
- **Onboarding Flow**:
  - 4-page animated welcome tutorial
  - Feature highlights for new users
  - Skip or complete onboarding
  - One-time display on first launch

#### Profile & Analytics
- **Profile Screen**:
  - Comprehensive learning statistics
  - Interactive progress charts (fl_chart)
  - Language-specific progress breakdown
  - Weekly activity visualization
  - Total XP and level progression
- **Enhanced Audio Player**:
  - Playback speed control (0.5x - 2.0x)
  - Loop mode for repetitive practice
  - Restart button for convenience
  - Visual speed indicator

#### Accessibility & Theming
- **Dark Mode Support**:
  - Automatic theme switching
  - Light and dark theme configurations
  - Persistent theme preference
  - Material Design 3 throughout
- **Accessibility Features**:
  - Text scaling (0.85x - 1.3x)
  - High contrast mode option
  - Screen reader compatibility
  - Customizable text sizes in settings

#### Technical Improvements
- **State Management**:
  - Provider-based architecture for all services
  - `GamificationService` for achievements and streaks
  - `SettingsService` for user preferences
  - `ProgressService` enhanced with exercise tracking
- **Data Persistence**:
  - SharedPreferences for all user data
  - Exercise completion tracking per lesson
  - Settings persistence across sessions
  - Achievement unlock state management
- **New Models**:
  - `Achievement` with categories and progress
  - `Streak` with date-based tracking
  - `Exercise` (MultipleChoice, FillInBlank, Translation)
  - `Vocabulary` with phonetics and examples
  - Enhanced `Lesson` model with exercise loading
- **UI Components**:
  - `DailyLessonsSheet` - Modal bottom sheet for lesson selection
  - `PracticeScreen` - Interactive exercise interface
  - Smooth animations with flutter_animate
  - Interactive charts with fl_chart
  - Confetti effects for celebrations

### Fixed - 2025-11-08
- Replaced deprecated `withOpacity()` calls with `withValues(alpha:)` across multiple files
- Fixed language selection state management in HomeScreen
- Improved audio player stream subscription lifecycle management
- Removed unused `_selectedLanguage` state from HomeScreen

### Changed - 2025-11-08
- Refactored language selection from inline day grid to modal bottom sheet
- Simplified HomeScreen layout by removing conditional rendering logic
- Updated CourseStructure to always be visible (not conditionally rendered)
- Migrated from two-step to one-step lesson selection flow

## [1.0.0] - 2025-04-11
### Added
- **Web Development**: Modern HTML5 and CSS, Vanilla JavaScript with modular architecture, Responsive design, Client-side rendering, localStorage for state management.
- **Internationalization (i18n)**: Dynamic multilingual support, Seamless language switching, Comprehensive translation management for English, Spanish, Portuguese, French, and German.
- **Educational Technology**: Structured 50-day learning curriculum, Progressive learning path, Interactive lesson interfaces, Multimedia learning approach with text and audio.
- **Content Generation**: Python-based content generation scripts, Systematic content organization, Scalable content management.
- **Audio Processing**: Multilingual audio file management, Text-to-speech integration, Cross-language audio content.

## [0.1.0] - Initial release
- Project setup and initial structure.
