[app]
# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Supported orientations
orientation = portrait

# (list) Application requirements
requirements = python3,kivy==2.1.0,pillow,arabic_reshaper,python-bidi,android

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /opt/android-sdk

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Features (adds uses-feature -tags to manifest)
# android.features = android.hardware.usb.host

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) Extra XML to write directly inside the <manifest> element of AndroidManifest.xml
# android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra XML to write directly inside the <manifest><application> tag of AndroidManifest.xml
# android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies' contains an 'androidx' package.
android.enable_androidx = True

# (list) Add Java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# android.add_gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"

# (list) Packaging options to add
# android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# (list) Java classes to add as activities to the manifest.
# android.add_activities = com.example.ExampleActivity

#
# Python-for-android (p4a) specific
#

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) python-for-android URL to use for checkout
# p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
# p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
# p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
# p4a.extra_args =

#
# Buildozer specific
#

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e., .apk, .aab, .ipa) storage
# bin_dir = ./bin
