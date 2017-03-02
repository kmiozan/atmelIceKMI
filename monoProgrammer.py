# -*- coding: utf-8 -*-

import subprocess
from parhex import ParHex
from os import listdir
import sys, os

print('---------------------------------------------------------')

frozen = 'the development'

if getattr(sys, 'frozen', False):
    # we are running in a bundle
    frozen = 'the production'
    bundle_dir = sys._MEIPASS
# print('bundle dir is', bundle_dir)
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

print('It is ', frozen,
      ' environment, you need to have \n"firmwares" and "parameters" folders filled with firmware \nfiles and related atprogram*.bat files along with the \nexecutable!')

# print( 'sys.argv[0] is', sys.argv[0] )
print('You are running:\n', sys.executable)
print('Current working directory is:\n', os.getcwd())
print('---------------------------------------------------------')

card = ['Mono FTC', 'Mono']

print('\n Select the electronic card: ')

numb = 0
for ct in card:
    print(str(numb) + " : " + ct)
    numb += 1

c = input('\n')
c = int(c)

fList = listdir()
fwExt = ['.hex', '.a90']
fwList = [f for f in fList if any(fw in f for fw in fwExt)]

cfList = listdir('firmwares')
cfwExt = ['.hex', '.a90']
cfwList = [cf for cf in cfList if any(cfw in cf for cfw in cfwExt)]

print("\n Select the core firmware file: ")

numb = 0
for fw in cfwList:
    print(str(numb) + " : " + fw)
    numb += 1

a = input("\n")

cfw = 'firmwares\\' + cfwList[int(a)]



while (input("\n---------------------------------------------------------\nPress ENTER to program the selection continuously or type\nanything to exit . . .\n") == ""):

    print('---------------------------------------------------------')
#    print('')
    print('       ** S T A R T   P R O G R A M M I N G **')
#    print('')
    print('---------------------------------------------------------')

    if card[c] is 'Mono':

        parfList = listdir('parameters')

        parExt = ['.par', '.a90']
        parList = [f for f in parfList if any(fw in f for fw in parExt)]

        print("\n Select the parameter file: ")

        numb = 0
        for p in parList:
            print(str(numb) + " : " + p)
            numb += 1

        b = input("\n")
        p = 'parameters\\' + parList[int(b)]

    if card[c] is 'Mono FTC':
        print('\n' + cfwList[int(a)] + " is being installed.")
        fh = ParHex(cfw, False, None, None)
        fh.write_hex_file("MonoFTC.hex")
        # fh.merge(ph, overlap='replace')
        # fh.write_hex_file("Mono.hex")
        # prog = subprocess.Popen(bundle_dir+"\\atprogram_monoftc.bat", shell=False)
        prog = subprocess.Popen("atprogram_monoftc.bat", shell=False)
        prog.wait()
        # subprocess.call(['rm', 'MonoPar.hex'])
        # subprocess.call(['rm', 'MonoCore.hex'])
        print('\n' + cfwList[int(a)] + " was installed.")
    elif card[c] is 'Mono':
        print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " are being installed.")
        fh = ParHex(cfw, False, None, None)
        fh.write_hex_file("MonoCore.hex")
        ph = ParHex(p, False, None, None)
        ph.write_hex_file("MonoPar.hex")
        # fh.merge(ph, overlap='replace')
        # fh.write_hex_file("Mono.hex")
        # prog = subprocess.Popen(bundle_dir+"\\atprogram_mono.bat", shell=False)
        prog = subprocess.Popen("atprogram_mono.bat", shell=False)
        prog.wait()
        # subprocess.call(['rm', 'MonoPar.hex'])
        # subprocess.call(['rm', 'MonoCore.hex'])
        print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " were installed.")
    else:
        raise ValueError("Card type is not initialixed")

    print('---------------------------------------------------------')
#    print('')
    print('      ** P R O G R A M M I N G   C O M P L E T E D **')
#    print('')
    print('---------------------------------------------------------')

print('---------------------------------------------------------')
print('                 ** G O O D   B Y E **')
print('---------------------------------------------------------')