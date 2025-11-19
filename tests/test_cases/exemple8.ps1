# exemple8.ps1
# Pure custom calls, no built-in commands

Import-Module "$PSScriptRoot\exemple7.psm1"

# Instance creation (class is custom)
$user = [User]::new("Ayoub")

# Call custom class methods
$greeting = $user.BuildGreeting()
$internal = $user.BuildInternalData()

# Call custom module function
$ver = Get-CustomVersion

# Call external custom function from exemple9.ps1
Call-ExternalAction "INPUT_FROM_EX8"
