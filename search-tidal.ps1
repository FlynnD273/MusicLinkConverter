. .\get-python.ps1
& $(Get-PythonPath) "D:\repos\MusicLinkConverter\search-tidal.py" $($args -join ' ') | Set-Clipboard
