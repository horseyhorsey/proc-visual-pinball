import os
import pip
import sys

""" Run from the C:\P-ROC\Tools directory after installing the MOceans proc_env 27 installer """

pip.main(['install', 'pyyaml'])
pip.main(['install', 'pygame'])
pip.main(['install', 'pillow'])
pip.main(['install', 'requests'])
os.system('python -m pip install pypiwin32')

vpComFile = 'register_vpcom.py'
regCommand = 'python ' + vpComFile + ' --register'

def Replacer(file, oldLine, newLine):
	# Read
	with open(vpComFile, 'r') as file :
	  filedata = file.read()

	# Replace
	filedata = filedata.replace(oldLine, newLine)

	# Save
	with open(vpComFile, 'w') as file:
	  file.write(filedata)

#Lines to replace
oldLine = '_reg_clsctx_ = pythoncom.CLSCTX_LOCAL_SERVER # LocalSever (no InProc) only means game reloads entirely on next play'
newLine = '#_reg_clsctx_ = pythoncom.CLSCTX_LOCAL_SERVER # LocalSever (no InProc) only means game reloads entirely on next play'	  

#Register the first pass
os.system(regCommand)
Replacer(vpComFile, oldLine, newLine)
os.system(regCommand)