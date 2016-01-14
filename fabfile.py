#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Description: PlaceLocal deployment script used to deploy the PlaceLocal code to
             different environments.

Requirements: pip install -r fabfile/requirements.txt
Available Commands: fab --list
"""
import json
import os
import sys
import hipchat
import time
import os
import sendgrid

from StringIO import StringIO as _StringIO
from circleclient import circleclient
from fabric.api import env, local, run, execute, cd, get, settings, quiet, hide
from fabric.decorators import roles, parallel, runs_once
from datetime import datetime

STARTTIME = datetime.now()

#path exists for operator
path = '/var/www/Operator'

if path not in sys.path:
    sys.path.append(path)

def test():
    print "hello world"
