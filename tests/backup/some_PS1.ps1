@echo off
cd %~dp0
set mypath=%~dp0
java -Dpixy.home="%mypath%\" -jar pixy.jar -a -A -y xss:file:sql %*
del graphs\*.dot > nul 2>&1
del graphs\*.txt > nul 2>&1

REM Grant the group FileAdmins 'Delete' and 'Write DAC' permissions to C:\demo\example:
cacls "C:\demo\example" /grant:r FileAdmins:(D,WDAC)

REM How do the CACLS Switches work?
REM Here is a purely personal view of how to understand the CACLS syntax.  Begin by dividing the CACLS command into three parts thus:

REM CACLS  1) folder name   2) replace, edit or revoke entries   3) grant user permission

REM Example:
cacls  c:\home   /t   /g guyt:F
