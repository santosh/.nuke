import os
import sys
import nuke
import subprocess

print "Passing through revealInFinder.py"

"""
This module contains functionality of having a 'reveal in explorer' button in each
important node that carries a 'file' knob
"""

def add_reveal_button():
	"""
	add custom tab in node and add reveal button
	"""

	node = nuke.thisNode()
	button_reveal = nuke.PyScript_Knob("revealInFinder", "Reveal in Finder")
	tab_custom = nuke.Tab_Knob("custom", "custom") # first one is not for the interface, second one is
	node.addKnob(tab_custom)
	node.addKnob(button_reveal)

def reveal_in_finder():
	"""
	get file path and reveal src file finder
	:return: None
	"""

	node = nuke.thisNode()
	knob = nuke.thisKnob()

	if knob.name() == "revealInFinder":
		path = os.path.dirname(node["file"].getValue())
		if os.path.isdir(path):
			open_dir(path)
		else:
			nuke.message("File path doesn't seem to be set.")

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