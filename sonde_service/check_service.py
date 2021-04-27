#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 07:49:05 2021

@author: cybermeme
"""

import os
import sys



used_space=os.popen("systemctl status " + sys.argv[1] + ".service | grep 'Active: active (running)'").readline().strip()



if used_space:
    print("OK - Process is running.")
    sys.exit(0)
else:
    print("CRITICAL - Process is not running.")
    sys.exit(2)
