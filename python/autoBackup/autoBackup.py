import nuke
import os
import sys
import subprocess
import time

"""
This module works on doing a backup framework.
"""


# autoBackup Settings
###########################################
backup_dir = "{}/Desktop/nukebackup".format(os.path.expanduser("~"))

number_of_backups = 5

# Prototype of future functionality
#autosave_interval = 
###########################################

def open_dir(path):
	"""
	open directories in os dependent way
	:param path: String path to reveal in explorer
	:return: None
	"""

	if sys.platform == "darwin":
		subprocess.check_call(["open", path])
	if sys.platform == "linux2":
		try:
			subprocess.check_call(["xdg-open", path])
		except:
			nuke.message("Plugin not supported")
	if sys.platform == "win32":
		subprocess.check_call(["explorer", os.path.normpath(path)])


def get_current_script_name():
	"""
	get name of script from where function is being called
	:returns: String name of current nuke script
	"""

	script = nuke.root().name()
	script_name = os.path.splitext(os.path.basename(script))[0]

	return script_name


def open_backup_dir():
	"""
	opens backup dir
	"""

	script_name = get_current_script_name()
	script_backup_dir = "{}/{}".format(backup_dir, script_name)
	open_dir(script_backup_dir)

def make_backup():
	"""
	make backup of script
	:returns: none
	"""

	script_name = get_current_script_name()
	script_backup_dir = "{}/{}".format(backup_dir, script_name)
	current_time = time.strftime("%Y%m%d-%H%M")

	if not os.path.isdir(script_backup_dir):
		os.makedirs(script_backup_dir)

	try:
		nuke.removeOnScriptSave(make_backup)
		nuke.scriptSave("{}/bckp_{}_{}.nk".format(script_backup_dir, current_time, script_name))
		nuke.addOnScriptSave(make_backup)
	except:
		nuke.message("Couldn't write a backup file")

	delete_older_backup_versions(script_backup_dir)


def delete_older_backup_versions(path):
	"""
	keep only x number of backup file, where x is set in number_of_backups var
	:param path: String full path of script dir
	:returns: None
	"""

	files_list = []
	keep_list = []

	for filename in os.listdir(path):
		if os.path.splitext(filename)[1] == ".nk":
			files_list.append(filename)

	if len(files_list) > number_of_backups:
		keep_list = files_list[-number_of_backups:]

	for filename in files_list:
		if filename not in keep_list:
			file_to_delete = "{}/{}".format(path, filename)
			if os.path.isfile(file_to_delete):
				os.remove(file_to_delete)