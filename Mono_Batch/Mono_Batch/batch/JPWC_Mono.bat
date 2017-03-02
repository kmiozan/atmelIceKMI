cls
@echo off
setlocal EnableDelayedExpansion

set N=1

for /f "tokens=*" %%i in ('dir /b ..\*.a90') do (
set file_!N!=%%i
set /a N+=1
)

if !N! == 2 goto YAP1
if !N! GTR 10 goto hata1
:tekrar
set D=1
@ECHO Birden fazla dosya var. Lutfen dosya secin (1,2,3..vb):
@ECHO 1 - %file_1%
@ECHO 2 - %file_2%
if !N! == 3 goto break1
@ECHO 3 - %file_3%
if !N! == 4 goto break1
@ECHO 4 - %file_4%
if !N! == 5 goto break1
@ECHO 5 - %file_5%
if !N! == 6 goto break1
@ECHO 6 - %file_6%
if !N! == 7 goto break1
@ECHO 7 - %file_7%
if !N! == 8 goto break1
@ECHO 8 - %file_8%
if !N! == 9 goto break1
@ECHO 9 - %file_9%
:break1
set /p D=:
if %D% LSS %N% goto go1
@ECHO Dosya no yanlis girildi.
goto :tekrar
:go1
if !D! == 1 set file=%file_1%
if !D! == 2 set file=%file_2%
if !D! == 3 set file=%file_3%
if !D! == 4 set file=%file_4%
if !D! == 5 set file=%file_5%
if !D! == 6 set file=%file_6%
if !D! == 7 set file=%file_7%
if !D! == 8 set file=%file_8%
if !D! == 9 set file=%file_9%
goto SON1

:hata1
@ECHO HATA!!! Cok fazla eslesen var...
goto SON

:YAP1
set file=%file_1%

:SON1
@ECHO %file%

:SON
pause





rem @echo off

"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I250000 -datmega64 -f0x99CD -E0xFF -e -pf -ifrc_calib.hex
@IF ERRORLEVEL == 1 GOTO prog_Calib_code_error
"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I6480 -Y
@IF ERRORLEVEL == 1 GOTO Calibration_error
"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I250000 -datmega64 -ae0,0 -ve -ie0xFF_byte.hex
@IF ERRORLEVEL == 1 GOTO continue

@GOTO EEPROM_OSCCAL_value_error

:continue
"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I6480 -datmega64 -f0x99CD -E0xFF
"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I1000000 -datmega64 -e -pf -if..\%file% -Z0 -Sf0xFFFE
@IF ERRORLEVEL == 1 GOTO prog_customer_code_error




set K=1

for /f "tokens=*" %%i in ('dir /b ..\PAR\*.a90') do (
set parfile_!K!=%%i
set /a K+=1
)

if !K! == 2 goto YAP2
if !K! GTR 10 goto hata2
:tekrar1
set E=1
@ECHO Birden fazla dosya var. Lutfen dosya secin (1,2,3..vb):
@ECHO 1 - %parfile_1%
@ECHO 2 - %parfile_2%
if !K! == 3 goto break2
@ECHO 3 - %parfile_3%
if !K! == 4 goto break2
@ECHO 4 - %parfile_4%
if !K! == 5 goto break2
@ECHO 5 - %parfile_5%
if !K! == 6 goto break2
@ECHO 6 - %parfile_6%
if !K! == 7 goto break2
@ECHO 7 - %parfile_7%
if !K! == 8 goto break2
@ECHO 8 - %parfile_8%
if !K! == 9 goto break2
@ECHO 9 - %parfile_9%
:break2
set /p E=:
if %E% LSS %K% goto go2
@ECHO Dosya no yanlis girildi.
goto :tekrar1
:go2
if !E! == 1 set parfile=%parfile_1%
if !E! == 2 set parfile=%parfile_2%
if !E! == 3 set parfile=%parfile_3%
if !E! == 4 set parfile=%parfile_4%
if !E! == 5 set parfile=%parfile_5%
if !E! == 6 set parfile=%parfile_6%
if !E! == 7 set parfile=%parfile_7%
if !E! == 8 set parfile=%parfile_8%
if !E! == 9 set parfile=%parfile_9%
goto SON2

:hata2
@ECHO HATA!!! Cok fazla eslesen var...
goto SON

:YAP2
set parfile=%parfile_1%

:SON2
@ECHO %parfile%

:SON3
pause







"C:\Program Files (x86)\Atmel\AVR Tools\STK500\stk500.exe" -cUSB -I1000000 -datmega64 -pfv -if..\PAR\%parfile% 
@IF ERRORLEVEL == 1 GOTO prog_customer_parameter_code_error

COLOR AF
	@ECHO.
	@ECHO *********************************************************
	@ECHO 		P R O G R A M L A M A   T A M A M
	@ECHO 		CIKMAK ICIN BIR TUSA BASINIZ
	@ECHO *********************************************************
	@PAUSE
@GOTO END

:prog_Calib_code_error
COLOR CE
	@ECHO.
@ECHO ---------------------------------------------------------
	@ECHO.
	@ECHO 		H A T A
	@ECHO Kalibrasyon programinda hata var.
	@ECHO Programlanamadi !...
	@PAUSE
	@GOTO END
@ECHO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


:Calibration_error
COLOR CE
	@ECHO.
@ECHO ---------------------------------------------------------
	@ECHO.
	@ECHO 		H A T A
	@ECHO Kalibrasyon yapilamadi.
	@ECHO Programlanamadi !...
	@PAUSE
	@GOTO END
@ECHO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

:EEPROM_OSCCAL_value_error
COLOR CE
	@ECHO.
@ECHO ---------------------------------------------------------
	@ECHO.
	@ECHO 		H A T A
	@ECHO EEPROM OSCCAL okunan degeri: 0xFF
	@ECHO Programlanamadi!...
	@PAUSE
	@GOTO END
@ECHO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

:prog_customer_code_error
COLOR CE
	@ECHO.
@ECHO ---------------------------------------------------------
	@ECHO.
	@ECHO 		H A T A
	@ECHO OSCCAL degeri yazimi veya ana programlamada yapilamadi.
	@ECHO Programlanamadi!...
	@PAUSE
	@GOTO END
@ECHO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

:prog_customer_parameter_code_error
COLOR CE
	@ECHO.
@ECHO ---------------------------------------------------------
	@ECHO.
	@ECHO 		H A T A
	@ECHO Parametre dosyasý programlanamadý.
	@ECHO Programlanamadi!...
	@PAUSE
	@GOTO END
@ECHO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

:END				

