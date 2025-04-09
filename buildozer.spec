[app]
# (str) Title of your application
title = Music Player

# (str) Package name
package.name = musicplayer

# (str) Package domain (needed for android/ios packaging)
package.domain = org.musicplayer

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif

# (list) List of inclusions using pattern matching
source.include_patterns = default_album_cover.gif, fonts/*, *.json, theme.json, playlist.json

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Using compatible versions to avoid dependency conflicts
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,arabic_reshaper,python-bidi,cython==0.29.33,mutagen,sdl2_ttf,sdl2_image,sdl2_mixer,wheel

# (str) Presplash of the application
presplash.filename = %(source.dir)s/default_album_cover.gif

# (str) Icon of the application
icon.filename = %(source.dir)s/default_album_cover.gif

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Android application meta-data
android.meta_data = music_player=true

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.gradle_dependencies = androidx.core:core:1.7.0, androidx.media:media:1.4.3

# (int) Android logcat verbosity (defaults to 2)
android.logcat_level = 2

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Path to a custom build process manifest
p4a.branch = develop

# (bool) Skip certain build steps (for faster debugging)
# This is useful for CI environments
p4a.local_recipes = ~/.buildozer/android/platform/python-for-android/recipes

# (bool) If you're having boot-time memory issues, try to set these
android.extra_args = --release, --ignore-setup-py

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (list) Add custom environment variables
env = PYTHONPATH=$PYTHONPATH:$PYTHONHOME:/usr/local/lib/python3.10/site-packages
