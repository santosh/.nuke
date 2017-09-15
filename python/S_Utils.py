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
	