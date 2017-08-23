from __future__ import absolute_import, division, print_function

# Eliminates the frustration of 10 panels, defaults to 2

maxPanels = nuke.toNode('preferences')['maxPanels']
maxPanels.setValue(2)

# Santosh Menubar
SantoshMenu = menubar.addMenu("Santosh")

# Santosh Toolbar
toolbar = nuke.toolbar('Nodes')
SMenu = toolbar.addMenu('Santosh Tools', icon='V_Victor.png')