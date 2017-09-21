import nuke
import edgeNode

SantoshMenu.addCommand("edgeNode/Jump to First", "edgeNode.jump_to_edge_node('top')")
SantoshMenu.addCommand("edgeNode/Jump to Last", "edgeNode.jump_to_edge_node('bottom')")
SantoshMenu.addCommand("edgeNode/View First", "edgeNode.view_edge_node('top')")
SantoshMenu.addCommand("edgeNode/View Last", "edgeNode.view_edge_node('bottom')")