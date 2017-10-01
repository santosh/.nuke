# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import PySide
import platform
from PySide import QtCore

print("Nuke: {nuke}, Python: {python}, PySide: {pyside}, QtCore: {qtcore})".format(
   nuke=nuke.NUKE_VERSION_STRING,
   python=platform.python_version(),
   pyside=PySide.__version__,
   qtcore=QtCore.qVersion())
   )

# Santosh Tools Folder
# Copyright (c) 2017 Santosh Kumar. All Rights Reserved.
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')
