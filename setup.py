#setup.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = ['tree.py', 'config.json']
excludes = ["tkinter"]
packages = ["os", "idna", "requests","json","base64","pyaudio", "bs4", "pyttsx3", "lxml","win32com"]
buildOptions = dict(packages = ['pyHook','speechrecognition', 'pypiwin32'], excludes = [])
setup(
    name = "Test",
    description='App Description',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("branch_search.py")]
)
