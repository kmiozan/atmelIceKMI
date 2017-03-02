# -*- coding: utf-8 -*-

import intelhex

class ParHex(intelhex.IntelHex):
    """
    This class inherits the intelhex Python library to read, write, create from scratch and manipulate data from
    HEX (also known as Intel HEX) file format. These operations are provided by IntelHex class.
    """

    def __init__(self, _source =None, calibrate=False, _calibrationValue=None, _calibrationValueFile=None, ):
        """  """

        self.source=_source

        intelhex.IntelHex.__init__(self, self.source)

        if calibrate is True:
            self.calibrationValueFile = _calibrationValueFile
            self.calibrationValue = _calibrationValue

            if self.calibrationValueFile is not None:
                with open(self.calibrationValueFile) as calibValHex:
                    self.calibrationValue = calibValHex.read()
                    self.calibrate()
            else:
                if self.calibrationValue is not None:
                    self.calibrate()
                else:
                    raise ValueError("Calibration value is not initialized")

    def calibrate(self):
        self.puts(65534, chr(int(self.calibrationValue, 16)))
        print("Calibration Value 0x" + self.calibrationValue + " has been written at address FFFE")

    def parE2E(self, stock=None, brand=None, initLang=None):
        # 0xFFF0 adresinden baslayarak,
        # ilk 5 byte stok no (7188874400 i?in;
        strHexStock = str(hex(int(stock)))[2:] # 1AC7D84A0
        #strHexStock = strHexStock[2:]

        while len(strHexStock) < 10:
            strHexStock = "0"+strHexStock

        print(strHexStock)

        for sC in range(0,5,1):
            self.puts(65520+sC, chr(int(strHexStock[2*sC:2*sC+2], 16)))
            #print(65520+sC)
            #print(chr(int(strHexStock[2*sC:2*sC+2], 16)))
            #print(sC)
            #print(2*sC)
            #print((2*sC+2))

        #self.puts(65520, chr(int(strHexStock[0:2],16))) # 0xFFF0:71,
        #self.puts(65521, chr(int(hexStock[2:4]))) # 0xFFF1:88,
        #self.puts(65522, chr(int(hexStock[4:6]))) # 0xFFF2:87,
        #self.puts(65523, chr(int(hexStock[6:8]))) # 0xFFF3:44,
        #self.puts(65524, chr(int(hexStock[8:10]))) # 0xFFF4:00), sonraki byte brand no(

        self.puts(65525, chr(int(brand))) # 0xFFF5:1(1:Arcelik,2:Grundig,3:Beko)), sonraki byte default dil(
        self.puts(65526, chr(int(initLang))) # 0xFFF6:0(0:Turkce,1:ingilizce,2:Almanca,3:Fransizca) olarak kullaniliyor. Siz hex uzerinden degistirebilirsiniz.
