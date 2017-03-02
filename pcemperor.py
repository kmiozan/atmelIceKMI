# -*- coding: utf-8 -*-

import subprocess
from parhex import ParHex
from os import listdir

print('---------------------------------------------------------')
print('')
print('       ** S T A R T   P R O G R A M M I N G **')
print('')
print('---------------------------------------------------------')

card = ['Emperor', 'Mono', 'MonoFTC', 'Vader', 'VaderE2E']

print('\n Select the electronic card: ')

numb = 0
for ct in card:
    print(str(numb)+ " : " + ct)
    numb+=1

c = input('\n')
c = int(c)

#c = 1

fList = listdir()
fwExt = ['.hex', '.a90']
fwList = [f for f in fList if any(fw in f for fw in fwExt)]
#print(fwList)

cfList = listdir('firmwares')
cfwExt = ['.hex', '.a90']
cfwList = [cf for cf in cfList if any(cfw in cf for cfw in cfwExt)]

print("\n Select the core firmware file: ")

numb=0
for fw in cfwList:
    print(str(numb)+" : "+fw)
    numb+=1

a = input("\n")

cfw = 'firmwares\\'+cfwList[int(a)]

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
    p = 'parameters\\'+parList[int(b)]

#print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " are being installed.")

if card[c] is 'Emperor':
    print('\n' + cfwList[int(a)] + " is being installed.")
    calib = subprocess.Popen("atprogram_emperor_osc.bat", shell=False)
    calib.wait()
    #subprocess.call(['C:\\Program Files (x86)\\Atmel\\Studio\\7.0\\atbackend\\atprogram.exe', '-t', 'atmelice', 'atmega644pa', '-i', 'ISP', '-cl', '250khz', '-v', 'chiperase'])
    fh = ParHex(cfw, True, None, "oschex.hex")
    fh.write_hex_file("EmperorCalibrated.hex")
    prog = subprocess.Popen("atprogram_emperor_prog.bat", shell=False)
    prog.wait()
    #subprocess.call(['rm', 'EmperorCalibrated.hex'])
    print('\n' + cfwList[int(a)] + " was installed.")
elif card[c] is 'MonoFTC':
    print('\n' + cfwList[int(a)] + " is being installed.")
    fh = ParHex(cfw, False, None, None)
    fh.write_hex_file("MonoFTC.hex")
    #fh.merge(ph, overlap='replace')
    #fh.write_hex_file("Mono.hex")
    prog = subprocess.Popen("atprogram_monoftc.bat", shell=False)
    prog.wait()
    #subprocess.call(['rm', 'MonoPar.hex'])
    #subprocess.call(['rm', 'MonoCore.hex'])
    print('\n' + cfwList[int(a)] + " was installed.")
elif card[c] is 'Mono':
    print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " are being installed.")
    fh = ParHex(cfw, False, None, None)
    fh.write_hex_file("MonoCore.hex")
    ph = ParHex(p, False, None, None)
    ph.write_hex_file("MonoPar.hex")
    #fh.merge(ph, overlap='replace')
    #fh.write_hex_file("Mono.hex")
    prog = subprocess.Popen("atprogram_mono.bat", shell=False)
    prog.wait()
    #subprocess.call(['rm', 'MonoPar.hex'])
    #subprocess.call(['rm', 'MonoCore.hex'])
    print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " were installed.")
elif card[c] is 'Vader':
    print('\n' + cfwList[int(a)] + " is being installed.")
    calib = subprocess.Popen("atprogram_vader_osc.bat", shell=False)
    calib.wait()
    #subprocess.call(['C:\\Program Files (x86)\\Atmel\\Studio\\7.0\\atbackend\\atprogram.exe', '-t', 'atmelice', 'atmega644pa', '-i', 'ISP', '-cl', '250khz', '-v', 'chiperase'])
    fh = ParHex(cfw, True, None, "oschex.hex")
    fh.write_hex_file("VaderCalibrated.hex")
    prog = subprocess.Popen("atprogram_vader_prog.bat", shell=False)
    prog.wait()
    #subprocess.call(['rm', 'VaderCalibrated.hex'])
elif card[c] is 'VaderE2E':
    stock = input("\n Enter the 10-digit stock number\n\n")
    brand = input("\n Select the brand\n1 : Arcelik\n2 : Grundig\n3 : Beko\n\n")
    initLang = input("\n Select the initial language\n0 : Turkish\n1 : English\n2 : German\n3 : French\n\n")
    print('\n' + cfwList[int(a)] + " is being installed.")
    calib = subprocess.Popen("atprogram_vader_osc.bat", shell=False)
    calib.wait()
    # subprocess.call(['C:\\Program Files (x86)\\Atmel\\Studio\\7.0\\atbackend\\atprogram.exe', '-t', 'atmelice', 'atmega644pa', '-i', 'ISP', '-cl', '250khz', '-v', 'chiperase'])
    fh = ParHex(cfw, True, None, "oschex.hex")

    fh.parE2E(stock, brand, initLang)
    fh.write_hex_file("VaderCalibrated.hex")
    print("Written parameters are\nStock number: "+stock+"\nBrand: "+brand+"\nInitial Language: "+initLang+"\n")
    prog = subprocess.Popen("atprogram_vader_prog.bat", shell=False)
    prog.wait()
    # subprocess.call(['rm', 'VaderCalibrated.hex'])
else:
    raise ValueError("Card type is not initialixed")


#calibrationValueFile = "oschex.hex"

#with open(calibrationValueFile) as calibValHex:
#    calibrationValue = calibValHex.read()

#print('calibrationValue = ' + calibrationValue)

#temporaryFirmware = "EmperorDeneme.hex"  # file should be in x folder


# with open(temporaryFirmware, 'r+b') as firmwareFile:
#    # """ Hex File Read Operation """
#    firmwareFile.read()  # hex file to memory
#    firmwareFile.seek(int(firmwareFile.tell()) - 27)  # move to file position :01FFFE00EA18
#    firmwareFile.write(':01FFFE00'+calibrationValue+'00')
#    #firmwareFile.write(':AAAAAAAA' + calibrationValue + '00')

# with open(temporaryFirmware, 'r+b') as firmwareFile:
#    firmwareFile.read()  # hex file to memory
#    firmwareFile.seek(int(firmwareFile.tell()) - 26)  # move to file position 01FFFE00EA18
#    calibrationLine = firmwareFile.readline(12)  # read the line with calibration byte
#    print('calibrationLine = ' + calibrationLine)
#    decodedCalibrationLine = calibrationLine.decode("hex")  # decode string to hex string
#    #print('decodedCalibrationLine = ' + decodedCalibrationLine)
#    integerChecksum = 0  # initial checksum value (integer)
#    for i in range(0, len(decodedCalibrationLine) - 1):
#        # """ summation loop of decoded string of line """
#        integerChecksum += int(decodedCalibrationLine[i].encode("hex"), 16)
#        #print(decodedCalibrationLine[i])
#    print('summation = ' + str(integerChecksum))
#    hexChecksum = hex(256 - integerChecksum + (integerChecksum / 256) * 256).split('x')[1]
#    print('hexadecimal checksum value for intelhex = ' + hexChecksum)
#    firmwareFile.seek(int(firmwareFile.tell()) - 2)  # move to file position 18
#    firmwareFile.write(hexChecksum)

#if card[c] is 'Emperor':
    #prog = subprocess.Popen("atprogram_emperor_prog.bat", shell=False)
    #prog.wait()
#elif card[c] is 'Mono':
    #prog = subprocess.Popen("atprogram_mono.bat", shell=False)
    #prog.wait()
#else:
    #raise ValueError("Card type is not initialixed")



#print('\n' + cfwList[int(a)] + ' and ' + parList[int(b)] + " were installed.")

print('---------------------------------------------------------')
print('')
print('       ** PROGRAMMING COMPLETED **')
print('')
print('---------------------------------------------------------')