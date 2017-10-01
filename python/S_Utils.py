# -*- coding: utf-8 -*-
import nuke
import nukescripts

def create_read_from_write():
    """
    create read node from selected write node
    :return: None
    """

    sel = nuke.selectedNode()

    if sel.Class() == "Write":
        read = nuke.createNode("Read")
        read.setXpos(int(sel["xpos"].getValue()))
        read.setYpos(int(sel["ypos"].getValue()+50))
        read["file"].setValue(sel["file"].getValue())
        read["first"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["last"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["origfirst"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["origlast"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["colorspace"].setValue(int(sel["colorspace"].getValue()))
    else:
        nuke.message("A Write node must be selected.")

def disable(x):
    '''Disables all X nodes
    :param x: String class of node to be selected
    :return: None
    '''
    
    for a in nuke.allNodes():
        if a.Class() == x:
            a['disable'].setExpression('$gui') # this is unreversible at moment

def select(x):
    '''Selects all X nodes
    :param x: String class of node to be selected
    :return: None
    '''
    
    for a in nuke.allNodes():
        if a.Class() == x:
            a.setSelected(True)

    nuke.message("Selected {} {} nodes.".format(len(nuke.selectedNode()), x))


def delete_disable():
    '''Deletes disable nodes'''

def propose():
    nuke.message("I love you!")
    
    if nuke.ask("Do you love me too?"):
        nuke.message("I appreciate that, but it was just a joke. :P")
    else:
        nuke.message("So rude you are. :/")
        