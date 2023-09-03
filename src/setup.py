# -*- coding: utf-8 -*-
import sys
import application
import platform
import os
from cx_Freeze import setup, Executable, winmsvcr
from requests import certs

def get_architecture_files():
    if platform.architecture()[0][:2] == "32":
        return ["../windows-dependencies/x86/oggenc2.exe", "../windows-dependencies/x86/bootstrap.exe", "../windows-dependencies/x86/libvlc.dll", "../windows-dependencies/x86/libvlccore.dll", "../windows-dependencies/x86/plugins",  ["../windows-dependencies/dictionaries", "lib/enchant/data/mingw32/share/enchant/hunspell"], ["../windows-dependencies/x86/Microsoft.VC142.CRT", "."], ["../windows-dependencies/x86/Microsoft.VC142.MFC", "."], ["../windows-dependencies/x86/Microsoft.VC142.MFCLOC", "."], ["../windows-dependencies/x86/ucrt", "."]]
    elif platform.architecture()[0][:2] == "64":
        return ["../windows-dependencies/x64/oggenc2.exe", "../windows-dependencies/x64/bootstrap.exe", "../windows-dependencies/x64/libvlc.dll", "../windows-dependencies/x64/libvlccore.dll", "../windows-dependencies/x64/plugins", ["../windows-dependencies/dictionaries", "lib/enchant/data/mingw64/share/enchant/hunspell"], ["../windows-dependencies/x64/Microsoft.VC142.CRT", "."], ["../windows-dependencies/x64/Microsoft.VC142.MFC", "."], ["../windows-dependencies/x64/Microsoft.VC142.MFCLOC", "."], ["../windows-dependencies/x64/ucrt", "."]]

def find_sound_lib_datafiles():
    import os
    import platform
    import sound_lib
    path = os.path.join(sound_lib.__path__[0], 'lib')
    if platform.architecture()[0] == '32bit' or platform.system() == 'Darwin':
        arch = 'x86'
    else:
        arch = 'x64'
    dest_dir = os.path.join('sound_lib', 'lib', arch)
    source = os.path.join(path, arch)
    return (source, dest_dir)

def find_accessible_output2_datafiles():
    import os
    import accessible_output2
    path = os.path.join(accessible_output2.__path__[0], 'lib')
    dest_dir = os.path.join('accessible_output2', 'lib')
    return (path, dest_dir)

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = dict(
    build_exe="dist",
    optimize=1,
    includes=["enchant.tokenize.en"], # This is not handled automatically by cx_freeze.
    include_msvcr=False,
    replace_paths = [("*", "")],
    include_files=["icon.ico", "app-configuration.defaults", "mastodon.defaults", "keymaps", "locales", "sounds", "documentation", find_sound_lib_datafiles(), find_accessible_output2_datafiles()]+get_architecture_files(),
    packages=["wxUI"],
    bin_path_excludes=["C:\\Program Files", "C:\Program Files (x86)"],
)

executables = [
    Executable('main.py', base=base, target_name="twblue")
]

winmsvcr.FILES = ()
winmsvcr.FILES_TO_DUPLICATE = ()
setup(name=application.name,
      version=application.version,
      description=application.description,
      options = {"build_exe": build_exe_options},
      executables=executables
      )
