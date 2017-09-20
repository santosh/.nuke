import nuke
import revealInFinder

print "Passing through revealInFinder menu.py"

node_classes = ["Read", "Write", "Camera", "Camera2", "ReadGeo", "ReadGeo2", "WriteGeo"]

for node in node_classes:
	nuke.addOnUserCreate(revealInFinder.add_reveal_button, nodeClass=node)
	nuke.addKnobChanged(revealInFinder.reveal_in_finder, nodeClass=node)