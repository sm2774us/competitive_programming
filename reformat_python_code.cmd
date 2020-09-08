@echo off
setlocal

@echo on
set script_file=%0
REM call :GetFileBaseDirWithoutEndSlash script_path "%script_file%"
for %%a in ("%script_file%") do set "script_path=%%~dpa"
REM set script_path=%cd%
@echo %script_path%
PUSHD %script_path%
c:\cygwin64\bin\bash.exe -l "%script_path%\reformat_python_code.sh"
POPD
@echo off

exit /b 0