# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import sys
import PySide
from PySide import QtCore

print("Nuke is starting with PySide", PySide.__version__,
	"and QtCore version", QtCore.qVersion())
print("Running on python version", tuple(sys.version_info)[:-2])

# Project Settings > Default format: HD 1920x1080
nuke.knobDefault("Root.format", "HD_1080")

# Sets the bounding box to B instead of A and B combined
# See https://twitter.com/sntshk/status/877413861254725635
nuke.knobDefault("Merge.bbox", "3")

# Santosh Tools Folder
# Copyright (c) 2017 Santosh Kumar. All Rights Reserved.
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')

