# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import dummy
import S_Utils

# Eliminates the frustration of 10 panels, defaults to 2

maxPanels = nuke.toNode('preferences')['maxPanels']
maxPanels.setValue(3)

# Nuke's Own Menus
# This will add dummy under Edit/Node menu
# this is the top nuke menubar
nk = nuke.menu('Nuke')
# adds custom item in existing menu
nk.findItem('Edit/Node').addCommand('Dummy', 'nuke.createNode("Write")', 'ctrl+y', index=0)

# Santosh Menubar
SantoshMenu = menubar.addMenu("$antosh")
SantoshMenu.addCommand("Create/Scene", 'S_Utils.Scene_3D()', 'alt+shift+s')
SantoshMenu.addCommand("Create/R from W", "S_Utils.create_read_from_write()", "alt+j")

# Santosh inside Toolbar; this is for gizmos
toolbar = nuke.menu('Nodes')
S_Nodes_Menu = toolbar.addMenu('$antoshTools', icon='S_Santosh.png')
S_Nodes_Menu.addCommand('S_Dummy', 'nuke.createNode("Write")', 'ctrl+b', icon='S_Dummy.png')