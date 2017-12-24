# S_Santosh
_**S_Santosh**_ is a set of plugins and gizmos for the Foundry Nuke to aid in the process of digital compositing.

## Plugins
List of current plugins can be found in `python/init.py` file.

 * renderFinish - Rings a bell and shows a notification if rendern is finished.
 * revealInFinder - Opens file location in explorer on certain nodes, including but not limited to Read, Write and Camera nodes.
 * edgeNode - Jump to, or view first or last nodes in DAG.
 * exrSplit - Splits multi-channel EXR files into separate channels using shuffle nodes.

There are some other plugins inside the **S_Scriptlets** menu. Like *Read from Write*.

## Gizmos
Gizmos are inside left toolbar. 

 * S_Frequency_Sep - A frequency separation technique used in digital beautification.
 * S_Trails - 

## ToolSets
ToolSets are nothing but a set of nodes, for specific workflow. Find them in left toolbar (two wrench icon).
 
## Map

init.py - Initial startup settings. Works well with `menu.py`

menu.py - Just like init.py, custom settings and GUI addons

/python/ - python scripts and plugins

/gizmos/ - gizmo hub

/icons/ - sugar for gizmos

# Feedback
Having troubles? Have some suggestions? Want to talk about scripts? Feel free to create a post at https://github.com/santosh/.nuke/issues