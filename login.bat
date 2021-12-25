@if (@CodeSection == @Batch) @then


@echo off
SET BROWSER=chrome.exe

rem Use %SendKeys% to send keys to the keyboard buffer
set SendKeys=CScript //nologo //E:JScript "%~F0"
START %BROWSER% -newtab "10.100.1.1:8090"
timeout /T 2

%SendKeys% {TAB}"
%SendKeys% "{TAB}"
%SendKeys% "076bct059"
%SendKeys% "{TAB}"
%SendKeys% "cax9mx356b"
%SendKeys% "{ENTER}"

taskkill /IM %BROWSER%
goto :EOF

@end

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));