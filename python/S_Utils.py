# -*- coding: utf-8 -*-
import nuke
import nukescripts

def create_read_from_write():
	"""
	create read node from selected write node
	:return: None
	"""

	sel = nuke.selectedNode()

	if sel.Class() == "Write":
		read = nuke.createNode("Read")
		read.setXpos(int(sel["xpos"].getValue()))
		read.setYpos(int(sel["ypos"].getValue()+50))
		read["file"].setValue(sel["file"].getValue())
		read["first"].setValue(int(nuke.Root()["first_frame"].getValue()))
		read["last"].setValue(int(nuke.Root()["last_frame"].getValue()))
		read["origfirst"].setValue(int(nuke.Root()["first_frame"].getValue()))
		read["origlast"].setValue(int(nuke.Root()["last_frame"].getValue()))
		read["colorspace"].setValue(int(sel["colorspace"].getValue()))
	else:
		nuke.message("A Write node must be selected.")

def Scene_3D():
	'''
	Create bare 3D setup consisting a Scene, Camera, Light and Renderer.
	:return: None
	'''
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
	
	if nuke.ask("Do you love me too?"):
		nuke.message("I appreciate that, but it was just a joke. :P")
	else:
		nuke.message("So rude you are. :/")

# Here for templating purpose only

# Delete all nodes except x
# for i in nuke.allNodes():
# 	if i.Class() != 'Read':
# 		nuke.delete(i)
