# for feedback, please post here: https://github.com/santosh/.nuke/issues

# using naming convention, like i b n k for int, bool, node, knob

strRepeat = nuke.getInput("Enter number of copies: ", "10")
iRepeat = int(strRepeat) # probably gonna be replaced by knob input
bFirstLoop = True

# packing into group {{{
nGroup = nuke.nodes.Group(name="S_Trails")
nGroup.begin()

## GUI COMPONENETS BEGIN
kX_Trans = nuke.Double_Knob("x_trans", "Translate X:")
kX_Trans.setRange(-50.,50.)
kX_Trans.setValue(20.)
nGroup.addKnob(kX_Trans)

kY_Trans = nuke.Double_Knob("y_trans", "Translate Y:")
kY_Trans.setRange(-50.,50.)
kY_Trans.setValue(20.)
nGroup.addKnob(kY_Trans)

kX_Rot = nuke.Double_Knob("rot", "Rotate:")
kX_Rot.setRange(-20.,20.)
kX_Rot.setValue(0.)
nGroup.addKnob(kX_Rot)

kX_Scale = nuke.Double_Knob("scale", "Scale:")
kX_Scale.setRange(-1.,2.)
kX_Scale.setValue(1.)
nGroup.addKnob(kX_Scale)

## GUI COMPONENTS END

# calculate center of the project dimension
projwidth = nuke.root()['format'].value().width()
projheight = nuke.root()['format'].value().height()

nInput = nuke.nodes.Input() #input node is gateway into the gizmo
nDot = nuke.nodes.Dot()
nDot.setInput(0, nInput) # input comes to a Dot node

for i in range(iRepeat):
    # translating by 20 in x and y
    nTrans = nuke.nodes.Transform(name="transform" + str(i),
                                    translate="parent.x_trans parent.y_trans",
                                    rotate = "parent.rot",
                                    scale = "parent.scale",
                                    center = "{x} {y}".format(x=projwidth/2, y=projheight/2)
                                    )
    # create a merge node
    nMerge = nuke.nodes.Merge2(name="merge" + str(i))
    # set first input of merge to translated image
    nMerge.setInput(1, nTrans)

    if bFirstLoop: # if this is the first loop
        bFirstLoop = False # disable the logic, so below commands execute only once
        nTrans.setInput(0, nDot) # connect tranlate node to dot
        nMerge.setInput(0, nDot) # then merge to dot
    else: # do the same thing, but with previous merges
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)
    
    # nMerge becomes nPrevMerge for next Merge2
    nPrevMerge = nMerge

nOutput = nuke.nodes.Output()
nOutput.setInput(0, nMerge) # output node is attached to last Merge's output

nGroup.end()

# }}} group ends