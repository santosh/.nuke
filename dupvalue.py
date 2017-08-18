mastersetting = nuke.toNode('MasterNode').knob('saturation').getValue()

ccNodes = [i for i in nuke.allNodes() if i.name().startswith('ColorCorrect')]

for i in ccNodes:
    i.knob('saturation').setValue(masterSetting)