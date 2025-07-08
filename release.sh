#!/bin/bash
# release.sh - Create a new release

# Get current version
CURRENT_VERSION=$(python -c "from PyUIRender import __version__; print(__version__)")

# Prompt for new version
read -p "Current version is $CURRENT_VERSION. Enter new version: " NEW_VERSION

# Create git tag
git tag -a v$NEW_VERSION -m "Release version $NEW_VERSION"

# Push tag to remote
git push origin v$NEW_VERSION

echo "Version $NEW_VERSION has been released!"