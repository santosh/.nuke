import nuke
import nukescripts

def Scene_3D():
	nuke.createNode('Light')
	nuke.createNode('Scene')
	nuke.createNode('ScanlineRender')
	nuke.createNode('Camera')
	
	# select scalinerender
	# nukescripts.connect_selected_to_viewer(0)

def disable(x):
	'''Disables X nodes, defaults to RotoPaint'''
	
	# if nuke.ask('Disable all RotoPaint Nodes GUI?'):
	# 	for a in nuke.allNodes('RotoPaint'):
	# 		a['disable'].setExpression('$gui')

def delete_disable():
	'''Deletes disable nodes'''

def propose():
	nuke.message("I love you!")
	nuke.ask("Do you love me too?")

# Here for templating purpose only

# Delete all nodes except x
# for i in nuke.allNodes():
# 	if i.Class() != 'Read':
# 		nuke.delete(i)
