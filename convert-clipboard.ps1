. .\get-python.ps1
& $(Get-PythonPath) "D:\repos\MusicLinkConverter\convert.py" $(Get-Clipboard) | Set-Clipboard
