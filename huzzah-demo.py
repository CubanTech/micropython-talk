dir()
dir(builtins)

import pyb
pyb.info()

import gc
gc.collect()
gc.mem_free()
list(range(1000))
gc.mem_free()
gc.collect()
gc.mem_free()

gc.disable()
a = list(range(1000))
b = list(range(1000))

import time
time.localtime()
time.sleep(2)

import sys
sys.version

import os
os.listdir()
os.mkdir('bla')

import machine
machine.freq()
machine.freq(16000000)
machine.reset()

import network
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect('essid', 'password') # connect to an AP
wlan.config('mac')      # get the interface's MAC adddress
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

ap = network.WLAN(network.AP_IF)
ap.config(essid="MicroPython says hi to PyGrunn")
ap.config(password="pygrunn")
ap.active(True)
