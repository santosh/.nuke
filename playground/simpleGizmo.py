# bare gizmo node with python
g = nuke.createNode('Group')

# this give the code context
g.begin()

# inputs and their names
iput = nuke.createNode('Input')
iput.knob('name').setValue('mask')
oput = nuke.createNode('Input')
oput.knob('name').setValue('input')

cc = nuke.createNode('ColorCorrect')
cc.setInput(0, iput)

nuke.createNode('Output')
g.end()
