b = nuke.createNode('Blur')

# different type of knobs
b.knob('size').setValue(5)
b.knob('filter').setValue(2)
b.knob('crop').setValue(False)

# delete nodes by selecting
nuke.delete(nuke.toNode('CameraTracker1'))
