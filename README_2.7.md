## Remove entries from the enviroment path to Python26 so not to interfere with the proc_env install.

## Installer (Python 2.7 32bit, P-ROC, SkeletonGame and VPROC controller)

http://skeletongame.com/files/proc_env_installer_wHD_1.27.exe

Run MJOcean installer. Next, next, next..

### Copy this repos files into C:\P-ROC\Tools

### Installer falling over fix

Ensure PIP is installed:

	python -m ensurepip --no-default-pip

Run script to install correct version of Win32Com and to make sure it installs pygame, pyyaml, pillow. Note: May need admin rights.

	python proc_env_fix.py

### SDLTTF
Copy the SDLTff that works with Visual Pinball into 'P-ROC\DLLS'

### Base User Config.yaml
Edit the config file in "C:\Users\%UserName%\.pyprocgame" and add entry for the vp game map location:

	vp_game_map_file: c:\P-ROC\shared\vp_game_map.yaml  # relevant for Visual Pinball (only)
