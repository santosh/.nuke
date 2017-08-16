from __future__ import absolute_import, division, print_function, unicode_literals
import PySide
from PySide import QtCore

print("Nuke is starting with PySide", PySide.__version__,
	"and QtCore version", QtCore.qVersion())

# Project Settings > Default format: HD 1920x1080
nuke.knobDefault("Root.format", "HD_1080")

# Sets the bounding box to B instead of A and B combined
# See https://twitter.com/sntshk/status/877413861254725635
nuke.knobDefault("Merge.bbox", "3")
