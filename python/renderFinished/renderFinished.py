# -*- coding: utf-8 -*-
import os
import nuke
import PySide.QtGui

print "renderFinished.py is loaded"

"""
This module contains functionality of notifying the user when a render is finished.
This is done by playing a sound and showing notification window.
"""

# USER SETTINGS
####################################

# turn this to False to disable "Rendering Finished" notification
SHOW_NOTIFICATION = True

# turn this False to disable ting sound
PLAY_SOUND = True

# specify your own sound file
SOUND_FILE = "{}/01.wav".format(os.path.dirname(__file__))

####################################

def notify_user():
	"""
	show a notification and play a ting sound when render is done
	"""

	if PLAY_SOUND:
		PySide.QtGui.QSound.play(SOUND_FILE)

	if SHOW_NOTIFICATION:
		nuke.message("Rendering Finished")

