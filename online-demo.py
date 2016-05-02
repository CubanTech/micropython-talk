# FIRST
import pyb
pyb.LED(1).on()

# READFILE
import os
print(os.listdir('/'))
print(os.listdir('/sd'))
with open('/sd/readme.txt') as f:
    print(f.read())

# LCD
import pyb
lcd = pyb.LCD('Y')
lcd.light(True)
lcd.write('Hello PyGrunn!')

with open('/sd/readme.txt') as f:
    lcd.write(f.read())
