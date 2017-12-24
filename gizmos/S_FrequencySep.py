# for feedback, please post here: https://github.com/santosh/.nuke/issues

# using naming convention, like i b n k for int, bool, node, knob

# Group packing starts
nGroup = nuke.nodes.Group(name="S_FrequencySep")
nGroup.begin() # gizmo starts

## GUI COMPONENETS BEGIN
kDetails = nuke.Double_Knob("details", "Details:")
kDetails.setRange(0,30.)
kDetails.setValue(0)
kDetails.setTooltip("Details to retain. Higher value goes back to original image. \
	Lowest point is inverse value of smoothness.")
nGroup.addKnob(kDetails)

kSmoothness = nuke.Double_Knob("smoothness", "Smoothness:")
kSmoothness.setRange(0,100.)
kSmoothness.setValue(0)
kSmoothness.setTooltip("Smoothness to achieve. Lower value goes back to original.")
nGroup.addKnob(kSmoothness)

## GUI COMPONENTS END

## DAG SETUP STARTS
nInput = nuke.nodes.Input() # gizmo input comes here

nMergeFrom = nuke.nodes.Merge(operation="from")
nMergeFrom.setInput(0, nInput)

nBlurDetails = nuke.nodes.Blur(label="Details",
							size="parent.details")
nBlurDetails.setInput(0, nInput)
nMergeFrom.setInput(1, nBlurDetails)

nInputMask = nuke.nodes.Input(name="mask")

nBlurSmoothness = nuke.nodes.Blur(label="Smoothness",
								size="parent.smoothness")
nBlurSmoothness.setInput(0, nBlurDetails)
nBlurSmoothness.setInput(1, nInputMask)

nMergePlus = nuke.nodes.Merge(operation="plus")
nMergePlus.setInput(1, nBlurSmoothness)
nMergePlus.setInput(0, nMergeFrom)

nOutput = nuke.nodes.Output()
nOutput.setInput(0, nMergePlus) # output node is attached to Merge plus

nGroup.end() # gizmo ends
## DAG SETUP ENDS
# group ends
