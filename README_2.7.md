## Remove entries from the enviroment path to Python26 so not to interfere with the proc_env install.

# 1. Installer (Python 2.7 32bit, P-ROC, SkeletonGame and VPROC controller)

Run this MOcean proc_env_installer. Next, next, next..

http://skeletongame.com/files/proc_env_installer_wHD_1.27.exe

Courtesy of (https://github.com/mjocean) 

### If you get extreme errors whilst running the installer: Search for libiconv-2.dll and you'll find two versions of it - one in syswow64, which needs to be renamed during the install.


# 2. Copy this repos files into C:\P-ROC\Tools 
## *** This repo meaning these files https://github.com/horseyhorsey/proc-visual-pinball

# 3. MOcean Installer falling over fix

Ensure PIP is installed:

	python -m ensurepip --no-default-pip

Run this script to install correct version of Win32Com and to make sure it installs pygame, pyyaml, pillow. Note: May need admin rights.

	python proc_env_fix.py
	
This will register the vp_com that was copied into Tools for you. For success look for:
	
	VPROC.Registered ok
	
#### If you get an error along the lines of - ImportError: DLL load failed: The specified module could not be found. Run the following command.

	python C:\Python27\Scripts\pywin32_postinstall.py -install

# 4. SDLTTF
Copy the SDLTff that works with Visual Pinball into 'P-ROC\DLLS' - ##### This DLL folder is in the files you downloaded and put into the tools folder

# 5. Base User Config.yaml
Edit the config file in "C:\Users\%UserName%\.pyprocgame" and add entry for the vp game map location:

	vp_game_map_file: c:\P-ROC\shared\vp_game_map.yaml  # relevant for Visual Pinball (only)
	
	
## When trying to run Visual Pinball after these steps and errors like "Controller not found"

	Open command prompt with Administrator
	
	python C:\Python27\Scripts\pywin32_postinstall.py -install
	
	On success you will see the following:
	
		Copied pythoncom27.dll to C:\WINDOWS\SysWOW64\pythoncom27.dll
		Copied pythoncomloader27.dll to C:\WINDOWS\SysWOW64\pythoncomloader27.dll
		Copied pywintypes27.dll to C:\WINDOWS\SysWOW64\pywintypes27.dll
		Registered: Python.Interpreter
		Registered: Python.Dictionary
		Registered: Python
		-> Software\Python\PythonCore\2.7\Help[None]=None
		-> Software\Python\PythonCore\2.7\Help\Pythonwin Reference[None]='C:\\Python27\\Lib\\site-packages\\PyWin32.chm'
		Pythonwin has been registered in context menu
		Shortcut for Pythonwin created
		Shortcut to documentation created
		The pywin32 extensions were successfully installed.
		
	You don't need to re-register the controller this should be all it needs.
	
