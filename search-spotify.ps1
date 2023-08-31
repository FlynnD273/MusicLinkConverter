. .\get-python.ps1
& $(Get-PythonPath) "D:\repos\MusicLinkConverter\search-spotify.py" $($args -join ' ') | Set-Clipboard
