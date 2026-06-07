[app]
title = Dead Climb
package.name = deadclimb
package.domain = org.abhishek
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3
version = 0.1
requirements = python3,pygame
orientation = landscape
fullscreen = 1

# CRITICAL FIX: Lock the API versions so it doesn't look for version 37
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.0

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.skip_source_filter = 1
