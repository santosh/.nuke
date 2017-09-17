# find the tutorial at nukestation.com/python-scripting-in-nuke-part-1-of-2-creating-nodes/

# using naming convention, like i b n for int, bool, node

iRepeat = 10 # probably gonna be replaced by knob input
bFirstLoop = True

nGroup = nuke.nodes.Group(name="Trails")
nGroup.begin()

nInput = nuke.nodes.Input()
nDot = nuke.nodes.Dot()
nDot.setInput(0, nInput)

for i in range(iRepeat):
    # translating by 20 in x and y
    nTrans = nuke.nodes.Transform(name="transform" + str(i), translate="20 20")
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
nOutput.setInput(0, nMerge)

nGroup.end()