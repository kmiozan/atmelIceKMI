@echo off
@SET CPU=atmega644pa
@SET SW_TOOL="C:\Program Files (x86)\Atmel\Studio\7.0\atbackend\atprogram.exe"
@SET CAL_HEX="rc_calib.hex"
@SET CAL_0HEX="0xFF_byte.hex"
@SET CAL_OSCBIN="osccal.bin"
@SET CAL_OSCHEX="oschex.hex"
@SET TOOL=atmelice
@SET CAL_FUSES=E2D9FD
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 250khz -v chiperase
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -v write -fs --values %CAL_FUSES%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 250khz -v program -fl --verify --format hex -f %CAL_HEX%

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 6480hz calibrate

%SW_TOOL% -t %TOOL% -d %CPU% -i ISP -cl 125khz verify -ee -f %CAL_0HEX%



%SW_TOOL% -t %TOOL% -d %CPU% -i ISP read -ee -s 1 -o 0 --format bin -f %CAL_OSCBIN%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP read -ee -s 1 -o 0 --format hex -f %CAL_OSCHEX%
%SW_TOOL% -t %TOOL% -d %CPU% -i ISP chiperase program -ee -f %CAL_OSCBIN% -o 0

