[app]

title = Optimus Jarvis Super Frame
package.name = optimusjarvis
package.domain = org.optimus.jarvis

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = *.py,*.json,*.sh

version = 1.0

requirements = kivy

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.service = False

[buildozer]
log_level = 2
build_dir = .buildozer
bin_dir = ./bin
