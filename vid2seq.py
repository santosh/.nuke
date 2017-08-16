# getting into nuke 
# this script writes out targa sequences from a video file
# this script is intended to work from inside nuke
# expects availability of quicktime
# mostly hardcoded
nuke.nodes.Read(file="E:/Final/Practice/MVI_8411.mov", name="Footage")

footage = nuke.toNode("Footage")
nuke.createNode("Write")

# nuke.nodes.Read(file="E:/Final/Practice/footage/roof_###.tga")