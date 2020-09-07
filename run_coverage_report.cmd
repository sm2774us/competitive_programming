set script_file=%0
call :GetFileBaseDirWithoutEndSlash script_path "%script_file%"
REM set script_path=%cd%
@echo %script_path%
PUSHD %script_path%
c:\cygwin64\bin\bash.exe -l "%script_path%\run_coverage_report.sh"
POPD
exit /b 0