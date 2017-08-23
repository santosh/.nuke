# connect nodes to each other

flower = nuke.toNode('Read1')

cc = nuke.createNode('ColorCorrect')

# connect cc node to flower
# 0 is the first parameter, which defines it is the first
cc.setInput(0, flower)
cc.knob('shadows.gain').setValue(0.02)

nukescripts.connect_selected_to_viewer(0)
