[app]

# عنوان التطبيق
title = MusicPlayer

# معلومات الحزمة
package.name = musicplayer
package.domain = org.test

# إعدادات البناء
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,gif,ttf,otf

# المتطلبات
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

# إعدادات الشاشة
orientation = portrait
fullscreen = 0

# الأيقونات
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/data/default_album_cover.gif

# الأذونات
android.permissions = 
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    INTERNET

# إعدادات Android SDK
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk = 33
android.ndk = 25.1.8937393
android.archs = arm64-v8a,armeabi-v7a

# خيارات البناء
bootstrap = sdl2
p4a.branch = master
android.multi_touch = 1
android.hide_titlebar = 0
android.window_soft_input_mode = adjustResize

# تضمين الملفات الإضافية
include_patterns = 
    assets/*,
    fonts/*.ttf,
    fonts/*.otf,
    data/*.json,
    data/*.gif

# إعدادات Buildozer
[buildozer]
log_level = 2
warn_on_root = 1

#############################################
# إعدادات إضافية مهمة لمنع الأخطاء
#############################################

# قبول التراخيص تلقائياً
android.accept_sdk_license = True

# إعدادات NDK
android.ndk_path = /opt/android-ndk/

# إعدادات OpenJDK
android.java_jdk_path = /usr/lib/jvm/java-17-openjdk-amd64

# منع استخدام build-tools 36
android.build_tools_min_version = 33.0.2
android.build_tools_max_version = 33.0.2

# تحسينات للأداء
android.enable_androidx = True
android.enable_jetifier = True