#!/bin/bash

# Script to generate screenshots using fastlane
# Usage: ./scripts/generate_screenshots.sh [language]
# If no language is provided, screenshots will be generated for all languages

set -e

cd "$(dirname "$0")/../ios"

# Check if bundler is available and Gemfile exists
if [ -f "Gemfile" ] && command -v bundle &> /dev/null; then
  # Install dependencies if needed
  if [ ! -d "vendor/bundle" ]; then
    echo "Installing bundler dependencies..."
    bundle install
  fi
  FASTLANE_CMD="bundle exec fastlane"
else
  # Fall back to system fastlane
  FASTLANE_CMD="fastlane"
fi

if [ -z "$1" ]; then
  echo "Generating screenshots for all languages..."
  $FASTLANE_CMD screenshots
else
  echo "Generating screenshots for language: $1"
  $FASTLANE_CMD screenshots_for_language language:"$1"
fi

echo "✅ Screenshot generation complete!"
echo "Screenshots are located in: ios/fastlane/screenshots/"

