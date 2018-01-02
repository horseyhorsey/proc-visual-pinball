import os
import pip
import sys

pip.main(['install', 'pyyaml'])
pip.main(['install', 'pygame'])
pip.main(['install', 'pillow'])
os.system('python -m pip install pypiwin32')

#Force install pyWin32.
scriptsFolder = sys.exec_prefix + "\scripts"
pyWin32 = 'pywin32_postinstall.py'
os.system('python ' + scriptsFolder + "/" + pyWin32 + ' -install')