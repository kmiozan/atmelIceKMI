@echo off
@SET CPU=atmega644pa
@SET SW_TOOL="C:\Program Files (x86)\Atmel\Studio\7.0\atbackend\atprogram.exe"
@SET TOOL=atmelice
@SET CUSTOMER_FUSES=D2D9FD
@SET CUSTOMERCODE="EmperorCalibrated.hex"
@SET REMOVE=del

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP write -fs --values %CUSTOMER_FUSES%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 1mhz program -fl -f %CUSTOMERCODE%
pause

