# release.ps1 - Create a new release
$CURRENT_VERSION = python -c "from PyUIRender import __version__; print(__version__)"
$NEW_VERSION = Read-Host "Current version is $CURRENT_VERSION. Enter new version"
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"
git push origin "v$NEW_VERSION"
Write-Host "Version $NEW_VERSION has been released!"