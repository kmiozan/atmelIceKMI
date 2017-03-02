@echo off
@SET CPU=atmega64a
@SET SW_TOOL="C:\Program Files (x86)\Atmel\Studio\7.0\atbackend\atprogram.exe"
@SET TOOL=atmelice
@SET CUSTOMER_FUSES=CD99FF
@SET CUSTOMERCODECORE="MonoCore.hex"
@SET CUSTOMERCODEPAR="MonoPar.hex"
@SET REMOVE=del

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP chiperase

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP write -fs --values %CUSTOMER_FUSES%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 1mhz program -fl -f %CUSTOMERCODEPAR%

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP write -fs --values %CUSTOMER_FUSES%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 1mhz program -fl -f %CUSTOMERCODECORE%

pause

