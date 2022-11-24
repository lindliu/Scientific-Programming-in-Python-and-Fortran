@echo off

rem --- Configure environment

call config.cmd

echo Cleaning project...

if exist %BUILD_DIR% ( 
    echo Removing build directory...
    rmdir /Q /S %BUILD_DIR%
)

del /Q /S *.pyd >nul 2>&1
del /Q /S *.exe >nul 2>&1
del /Q /S *.state >nul 2>&1
