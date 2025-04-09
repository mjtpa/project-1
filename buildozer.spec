[app]
# (str) Title of your application
title = PythonProject1

# (str) Package name
package.name = pythonproject1

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pythonproject1

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif

# (list) Application data sources
source.data = data/default_album_cover.gif

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,arabic_reshaper,python-bidi,cython==0.29.36,mutagen,sdl2_ttf==2.0.18,sdl2_image==2.0.5,sdl2_mixer==2.0.4



# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# Use the SDK directory path here, not sdkmanager
android.sdk_path = /opt/android-sdk

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) The format used for the signature. The default is PKCS1, but for
# newer applications, PKCS1 with SHA256 is preferred.
android.keystore_signature_algorithm = PKCS1withRSA

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (int) Android logcat verbosity (defaults to 2)
android.logcat_level = 2

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Disable Android optimization
android.optimize = 0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (list) Add custom environment variables
# Here we define the path for the Android SDK and NDK, ensuring Buildozer finds them
env = ANDROID_SDK_ROOT=/opt/android-sdk;ANDROIDNDK=/opt/android-sdk/ndk/25.1.8937393
