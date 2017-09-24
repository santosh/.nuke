# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import PySide
from platform import python_version
from PySide import QtCore

print("Nuke: {nuke}, Python: {python}, PySide: {pyside}, QtCore: {qtcore})".format(
   nuke="9.0v7", # https://community.foundry.com/discuss/topic/135414/how-to-get-nuke-version-from-within-python
   python=python_version(),
   pyside=PySide.__version__,
   qtcore=QtCore.qVersion())
   )

# Santosh Tools Folder
# Copyright (c) 2017 Santosh Kumar. All Rights Reserved.
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')
