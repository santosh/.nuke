# confirming the project dimension resolution
projset = nuke.Root()
projset["format"].setValue("HD_1080")

# load video and set in & out point
foot = nuke.nodes.Read(file="C:/Users/Santosh/Desktop/MVI_8411.MOV", name="Nuke_Class1")

# select read node and attach write node to it
nuke.toNode("Nuke_Class1").setSelected(True)
wr = nuke.createNode("Write")

# specify the sequence path
wr["file"].setValue("C:/Users/Santosh/Desktop/nukke/nuke_API_###.jpg")

# connect to the first viewer, if many
nukescripts.connect_selected_to_viewer(0)

# perform the render, 50th to 140th frame
nuke.render(wr, 50, 140, 1)
