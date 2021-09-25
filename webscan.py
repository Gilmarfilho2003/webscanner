#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
#
#
#
 __          __  ______   ____     _____    _____              _   _   _   _   ______   _____  
 \ \        / / |  ____| |  _ \   / ____|  / ____|     /\     | \ | | | \ | | |  ____| |  __ \ 
  \ \  /\  / /  | |__    | |_) | | (___   | |         /  \    |  \| | |  \| | | |__    | |__) |
   \ \/  \/ /   |  __|   |  _ <   \___ \  | |        / /\ \   | . ` | | . ` | |  __|   |  _  / 
    \  /\  /    | |____  | |_) |  ____) | | |____   / ____ \  | |\  | | |\  | | |____  | | \ \ 
     \/  \/     |______| |____/  |_____/   \_____| /_/    \_\ |_| \_| |_| \_| |______| |_|  \_\
                                                                                               
#
#

# Importing the libraries
import sys
import argparse
import subprocess
import os
import time
import random
import threading
import re
from urlparse import urlsplit

 do = input('''
	Coloque o endereço competo do site 
		1 - Começar scannear 
		2 - Saida
		==> ''')
	
	
############
if do == '2':
    exit 
