from __future__ import absolute_import, division, print_function, unicode_literals

# Eliminates the frustration of 10 panels, defaults to 2

maxPanels = nuke.toNode('preferences')['maxPanels']
maxPanels.setValue(2)