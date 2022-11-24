@echo off

rem --- Configure environment

call config.cmd

rem --- Build project

echo Configuring build...

pushd %BUILD_DIR%
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=%BUILD_TYPE% ..
%MAKE_CMD%
popd

rem --- Copy Python extension module to root directory

echo Copying binaries...

copy %BUILD_DIR%\src\particle-lib\*.pyd
copy %BUILD_DIR%\src\particles\*.exe