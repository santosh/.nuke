# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import S_Utils

# Eliminates the frustration of 10 panels, defaults to 2
nuke.toNode('preferences')['maxPanels'].setValue(3)

# nuke.addFavoriteDir("User Settings", "C:/Users/sntshk/.nuke/", nuke.PYTHON)

# this is the top nuke menubar
nukemenu = nuke.menu('Nuke')
# adds custom item in existing menu
nukemenu.findItem('File').addCommand('Restart Nuke', 'S_Utils.restartNuke()', "ctrl+shift+q", index=-1, shortcutContext=1)

# Nuke's Node menu
nodemenu = nuke.menu("Nodes")
# nodemenu.addCommand("Channel/Shuffle", 'nuke.createNode("Shuffle")', "n", shortcutContext=2, icon='Shuffle.png')
# https://support.foundry.com/hc/en-us/articles/208720909-Q100118-Setting-custom-keyboard-shortcuts-in-Nuke-9-and-10
nodemenu.findItem('Channel/Shuffle').setShortcut('n')

# Santosh Menubar
SantoshMenu = menubar.addMenu("S_Scriptlets")
SantoshMenu.addCommand("Create/R from W", "S_Utils.create_read_from_write()", "alt+j")
SantoshMenu.addCommand("Select", "S_Utils.select(nuke.getInput('Which nodes to select?', 'Read'))")

# Santosh inside Toolbar; this is for gizmos
toolbar = nuke.menu('Nodes')
S_Nodes_Menu = toolbar.addMenu('$antoshTools', icon='S_Santosh.png')
S_Nodes_Menu.addCommand('S_Trails', 'nuke.createNode("S_Trails")', 'alt+shift+t', icon='S_Trails.png')
S_Nodes_Menu.addCommand('S_FrequencySep', 'nuke.createNode("S_FrequencySep")', icon='S_FrequencySep.png')

# NODES CUSTOMIZATONS
#################################

# Shuffle label be the input of first "in" value
nuke.knobDefault("Shuffle.label", "[knob in]")

# Project Settings > Default format: HD 1920x1080
nuke.knobDefault("Root.format", "HD_1080")

# Sets the bounding box to B instead of A and B combined
# See https://twitter.com/sntshk/status/877413861254725635
nuke.knobDefault("Merge.bbox", "3")

#################################

# REMEMBER: USING CANCEL BUTTON IS REDUNDANT IN UI DESIGN
