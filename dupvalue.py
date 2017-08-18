mastersetting = nuke.toNode('MasterNode').knob('saturation').getValue()

ccNodes = [i for i in nuke.allNodes() if i.name().startswith('ColorCorrect')]

for i in ccNodes:
    i.knob('saturation').setValue(masterSetting)
    
    # below line does the same thing, but instead of doing silently,
    # it visually draws a green line between them
    #i.knob('saturation').setExpression(MasterNode.saturation)
