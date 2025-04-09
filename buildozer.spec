[app]

title = MusicPlayer
package.name = musicplayer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,gif,ttf,otf
version = 0.1

requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,arabic_reshaper,python-bidi,cython==0.29.33,mutagen,wheel

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/data/default_album_cover.gif

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# Android SDK/API settings
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
android.ndk = 25b

# Build options
bootstrap = sdl2
copy_libs = 1
log_level = 2
android.multi_touch = 1
android.hide_titlebar = 0
android.pip_options = --use-pep517

# Include extra assets
include_patterns = assets/*,fonts/*.ttf,fonts/*.otf,data/*.json

# Other settings (optional)
# android.entrypoint = org.kivy.android.PythonActivity
# android.logcat_filters = *:S python:D

[buildozer]

log_level = 2
warn_on_root = 1

[hostpython]

# Optional, leave empty unless using a custom hostpython

[pythonforandroid]

# Optional: Add any extra build options here
