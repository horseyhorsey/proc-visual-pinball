# Visual Pinball - PROC - Setup
> Tested Win10 x64

#### Prerequisites 

Existing Python 2.6 or higher installations

> Remove entries from the enviroment path to Python26 to not interfere with the proc_env install as this will use and need Python 2.7.13

----

### 1. Installer (PROC)  http://skeletongame.com/files/proc_env_installer_wHD_1.27.exe

Courtesy of (https://github.com/mjocean) (https://skeletongame.com)

* Select all the options after opening the installer and run through any steps that require user input.

* After installation is completed open `C:\P-ROC` and remove or rename the `cmake` directory. (`stops R6304, msvcr90.dll`)

> Note (rare): If you get extreme errors whilst running the installer: Search for libiconv-2.dll and you'll find two versions of it - one in syswow64, which needs to be renamed during the install.

---

### 2. PROC VP Controller 

Download the files in this repository and copy to `C:\P-ROC\Tools`

https://github.com/horseyhorsey/proc-visual-pinball

Go to `C:\P-ROC\Tools` and open a command prompt and run the following to ensure pip installed.

	python -m ensurepip --no-default-pip
	
Run the following to clean up install if any parts are missing.

	python proc_env_fix.py	
	
This script will also register the `vp_com.py` controller. You will see the following line if OK.

	VPROC.Registered ok
	
---

> If you get an error along the lines of - ImportError: DLL load failed: The specified module could not be found. 

Run the following command.

	python C:\Python27\Scripts\pywin32_postinstall.py -install	

---

### 3. Last steps (Mandatory)

Edit the configuration that was created for you in the installer at `C:\Users\%UserName%\.pyprocgame\config.yaml`

Add the following line for vp game mapping.

	vp_game_map_file: c:\P-ROC\shared\vp_game_map.yaml  # relevant for Visual Pinball (only)
	
You can run a game now making sure you have a mapping for it in `P-ROC\Shared\vp_game_map.yaml`	
	
---

### 4. Updates

In some versions of skeleton game they use a higher SDL2 version than shipped.

https://www.libsdl.org/download-2.0.php (I am using latest as of now 2.0.10 stable without noticing issues)

Copy the `SDL2.dll` to `C:\P-ROC\DLLS`

---

### 5. Issues

`P-ROC\Shared\Log.txt` - Visual Pinball Controller log

---

Known issues:

* FontManager requires sdl2_tff (this wasn't an issue on last install)

Copy the `SDL2_ttf.dll` that works with Visual Pinball into 'P-ROC\DLLS'. You will find the file in `P-ROC\Tools\Dlls`

---
	
* When trying to run Visual Pinball after these steps and errors like "Controller not found"


Open command prompt as an Administrator.
	
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
	
