[app]

title = MusicPlayer
package.name = musicplayer
package.domain = org.test

version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,gif,ttf,otf
exclude_patterns = apache-ant-1.9.4/**

requirements = 
    python==3.10,
    kivy==2.1.0,
    kivymd==1.1.1,
    pillow,
    arabic_reshaper,
    python-bidi,
    cython==0.29.33,
    mutagen,
    wheel

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/data/default_album_cover.gif

android.permissions = 
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25.1.8937393
android.ndk_path = /opt/android-ndk/android-ndk-r25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a

bootstrap = sdl2
p4a.branch = master
android.multi_touch = 1
android.hide_titlebar = 0
android.window_soft_input_mode = adjustResize
android.accept_sdk_license = True

android.build_tools_min_version = 33.0.2
android.build_tools_max_version = 33.0.2

include_patterns = 
    assets/*,
    fonts/*.ttf,
    fonts/*.otf,
    data/*.json,
    data/*.gif

android.enable_androidx = True
android.enable_jetifier = True

log_level = 2
android.allow_background = true

[buildozer]
log_level = 2
warn_on_root = 1

[pythonforandroid]

[android]
android.extra_ndk_args = -O3 -fstrict-aliasing

[ios]