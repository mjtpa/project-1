[app]

# (اسم التطبيق)
title = MusicPlayer

# (اسم الحزمة ونطاقها)
package.name = musicplayer
package.domain = org.test

# (إصدار التطبيق)
version = 0.1

# (دليل المصدر)
source.dir = .

# (امتدادات الملفات التي يجب تضمينها)
source.include_exts = py,png,jpg,kv,atlas,json,gif,ttf,otf,mp3,wav,flac,ogg,m4a,aac,wma,aiff,opus

# (استبعاد الأنماط غير الضرورية)
exclude_patterns = apache-ant-1.9.4/**

# (المكتبات المطلوبة)
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

# (إعدادات العرض والواجهة)
orientation = portrait
fullscreen = 0

# (أيقونة التطبيق)
icon.filename = %(source.dir)s/icon.png

# (صورة الشاشة التمهيدية)
presplash.filename = %(source.dir)s/data/default_album_cover.gif

# (أذونات Android)
android.permissions = 
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    INTERNET

# (مستوى API المستهدف وأدنى مستوى مدعوم)
android.api = 33
android.minapi = 21

# (إصدار NDK وAPI الخاص به)
android.ndk = 25.1.8937393
android.ndk_api = 21

# (المعالجات المدعومة)
android.archs = arm64-v8a,armeabi-v7a

# (بيئة البناء الأساسية)
bootstrap = sdl2

# (فرع Python-for-Android)
p4a.branch = master

# (إعدادات أخرى)
android.multi_touch = 1
android.hide_titlebar = 0
android.window_soft_input_mode = adjustResize
android.accept_sdk_license = True

# (أدوات البناء)
android.build_tools_min_version = 33.0.2
android.build_tools_max_version = 33.0.2

# (تضمين الملفات الإضافية)
include_patterns = 
    assets/*,
    fonts/*.ttf,
    fonts/*.otf,
    data/*.json,
    data/*.gif

# (تفعيل AndroidX وJetifier)
android.enable_androidx = True
android.enable_jetifier = True

# (مستوى تسجيل الأحداث)
log_level = 2
android.allow_background = true

[buildozer]
log_level = 2
warn_on_root = 1

[pythonforandroid]

# (إعدادات إضافية لـ NDK)
[android]
android.extra_ndk_args = -O3 -fstrict-aliasing

[ios]
