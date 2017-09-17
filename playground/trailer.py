# using naming convention, like i b n for int, bool, node

iRepeat = 10 #probably gonna be replaced by knob input
bFirstLoop = True

nDot = nuke.nodes.Dot()

for i in range(iRepeat):
    # translating by 20 in x and y
    nTrans = nuke.nodes.Transform(name="transform" + str(i), translate="20 20")
    # create a merge node
    nMerge = nuke.nodes.Merge2(name="merge" + str(i))
    # set first input of merge to translated image
    nMerge.setInput(1, nTrans)

    if bFirstLoop: # if this is the first loop
        bFirstLoop = False # it will no longer be first loop for rest of the script
        nTrans.setInput(0, nDot) # connect tranlate node to dot
        nMerge.setInput(0, nDot) # then merge to dot
    else: # do the same thing, but with previous merges
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)
    
    # nMerge becomes nPrevMerge for next Merge2
    nPrevMerge = nMerge