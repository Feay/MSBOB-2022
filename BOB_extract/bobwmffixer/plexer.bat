echo off
for %%i in (*.WMF) do python bobWMFfixer.py "%%i"
pause