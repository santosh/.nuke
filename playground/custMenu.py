def dummyFunc():
	return "Dummy functions is being called.."

# adds shortcuts to existing nodes/gizmo

# adds shortcut to shuffle node
nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'ctrl+shift+alt+j',icon='Shuffle.png')
# the above command seems like pyside code.

# there's also a .findItem() and .setShortcut() method on nuke menus
nuke.menu('Nodes').findItem('Filter').findItem('ZDefocus').setShortcut('z')

# this is the top nuke menubar
nk = nuke.menu('Nuke')
# adds custom item in existing menu
nk.findItem('Edit/Node').addCommand('Dummy', 'dummyFunc()', 'ctrl+y', index=0)