# -*- coding: utf-8 -*-
import nuke

print "executing exrSplit"

def split():
    """
    Splits layers of exr file into multiple files and connects to Read
    """
    selection = nuke.selectedNode()
    # Make sure there's only one node selected
    if selection.Class() != "Read":
        nuke.message("Select an EXR Read node.")
    # Deal if Read node is not exr
    elif selection["file"].getValue()[-3:] != "exr":
        nuke.message("Read sequence is {}, exr needed.".format(selection["file"].getValue()[-3:]))
    else:
        # get layers https://docs.thefoundry.co.uk/products/nuke/developers/90/pythondevguide/channels.html#autocomp
        layers = list( set([c.split('.')[0] for c in selection.channels()]) )
        layers.remove('rgba')
        for layer in layers:
            # Shuffle out each layer
            shuffleNode = nuke.nodes.Shuffle()
            shuffleNode.setInput(0, selection)
            shuffleNode.knob('in').setValue(layer)
            shuffleNode.knob('label').setValue("[knob in]")

            # TODO: Checkbox if user wants to do AutoCrop
            # Autocrop with CurveTool        
            # curveToolNode = nuke.nodes.CurveTool(inputs=[shuffleNode])
            # curveToolNode.knob('operation').setValue(0) # Auto Crop
            # nuke.execute(curveToolNode, selection.knob('first').value(), selection.knob('last').value()) # doesn't performs proper execute | try last argument 1 as increment
            # get crop data from curvetool
            # cropNode = nuke.nodes.Crop(inputs=[curveToolNode])
