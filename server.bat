@rem
@echo off

set "_root=%~dp0"
set "_root=%_root:~0,-1%"
cd "%_root%"


set "_pyBin=%_root%\toolkit"
set "_GitBin=%_root%\toolkit\Git\mingw64\bin"
set "_adbBin=%_root%\toolkit\Lib\site-packages\adbutils\binaries"
set "PATH=%_root%\toolkit\alias;%_root%\toolkit\command;%_pyBin%;%_pyBin%\Scripts;%_GitBin%;%_adbBin%;%PATH%"

title OAS Console Debugger
echo This is an console to run adb, git, python and pip.
echo     adb devices
echo     git log
echo     python -V
echo     pip -V
echo. & echo ----- & echo.
echo.
)
echo.
chcp 65001
PROMPT $P$_$G$G$G
python server.py
cmd /Q /K
