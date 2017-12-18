# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import timelog

nuke.addOnScriptLoad(timelog.TimeLog().start_thread)