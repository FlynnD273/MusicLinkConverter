function Get-PythonPath {
	return Join-Path -Path $PSScriptRoot -ChildPath "/.venv/Scripts/python.exe"
}
