[app]

# Basic application information
title = MusicPlayer
package.name = musicplayer
package.domain = org.test

# Version information
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,gif,ttf,otf

# Python dependencies
requirements = 
    python3,
    kivy==2.1.0,
    kivymd==1.1.1,
    pillow,
    arabic_reshaper,
    python-bidi,
    cython==0.29.33,
    mutagen,
    wheel

# Orientation and display
orientation = portrait
fullscreen = 0

# Graphics assets
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/data/default_album_cover.gif

# Android permissions
android.permissions = 
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    INTERNET

# Android API settings
android.api = 33
android.minapi = 21
android.ndk = 25.1.8937393
android.ndk_path = /opt/android-ndk/android-ndk-r25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a

# Build behavior
bootstrap = sdl2
p4a.branch = master
android.multi_touch = 1
android.hide_titlebar = 0
android.window_soft_input_mode = adjustResize
android.accept_sdk_license = True

# Build tools version constraints
android.build_tools_min_version = 33.0.2
android.build_tools_max_version = 33.0.2

# Additional files to include
include_patterns = 
    assets/*,
    fonts/*.ttf,
    fonts/*.otf,
    data/*.json,
    data/*.gif

# Performance optimizations
android.enable_androidx = True
android.enable_jetifier = True

# Debugging options
log_level = 2
android.allow_background = true

##############################################
# Buildozer configuration section
##############################################
[buildozer]

# Logging and behavior
log_level = 2
warn_on_root = 1

##############################################
# Python for Android configuration
##############################################
[pythonforandroid]

# Recipe modifications if needed
# recipes.python = python3

##############################################
# Android specific configurations
##############################################
[android]

# Release signing (uncomment and fill for release builds)
# key.store = %(source.dir)s/keystore.jks
# key.store.password = yourpassword
# key.alias = youralias
# key.alias.password = youraliaspassword

# NDK optimizations
android.extra_ndk_args = -O3 -fstrict-aliasing

##############################################
# iOS specific configurations (optional)
##############################################
[ios]

# Uncomment and fill if building for iOS
# ios.kivy_ios_url = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master
