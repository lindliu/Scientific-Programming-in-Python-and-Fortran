@echo off

rem --- Configuration variables

set BUILD_TYPE=Release
set BUILD_DIR=build
set QT_ROOT=e:\qt
set MINGW_ROOT=%QT_ROOT%\Tools\mingw810_64
set MAKE_CMD=mingw32-make

rem --- Which python are we using

for /f %%i in ('which python') do set PYTHON_EXE=%%i

rem --- Extract Python path

For %%A in ("%PYTHON_EXE%") do (
    Set PYTHON_ROOT=%%~dpA
)

echo Using Python at %PYTHON_ROOT%

rem --- Configure PATH

set PATH=%MINGW_ROOT%\bin;%PYTHON_ROOT%;%PYTHON_ROOT%\Scripts;%PYTHON_ROOT%\Library\bin;%PATH%

rem --- Summary

echo.
echo ---- Configuration summary --------------------------
echo Build type  : %BUILD_TYPE%
echo Build dir   : %BUILD_DIR%
echo Qt dir      : %QT_ROOT%
echo MinGW dir   : %MINGW_ROOT%
echo Make cmd    : %MAKE_CMD%
echo Python      : %PYTHON_ROOT%
echo -----------------------------------------------------
echo.

