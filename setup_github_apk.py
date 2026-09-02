import os

os.makedirs('.github/workflows', exist_ok=True)

workflow_code = '''name: Build Optimus Jarvis APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer kivy

    - name: Build with Buildozer
      uses: ArtemSydoryk/buildozer-action@v1
      with:
        command: buildozer -v android debug
        subfolder: .

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: Optimus-Jarvis-APK
        path: bin/*.apk
'''

with open('.github/workflows/build.yml', 'w') as f:
    f.write(workflow_code)

print("Workflow created!")
