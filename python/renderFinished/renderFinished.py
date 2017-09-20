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
show_notification = True

# turn this False to disable ting sound
play_sound = True

# specify your own sound file
sound_file = "{}/01.wav".format(os.path.dirname(__file__))

####################################

def notify_user():
	"""
	show a notification and play a ting sound when render is done
	"""

	if play_sound:
		PySide.QtGui.QSound.play(sound_file)

	if show_notification:
		nuke.message("Rendering Finished")

