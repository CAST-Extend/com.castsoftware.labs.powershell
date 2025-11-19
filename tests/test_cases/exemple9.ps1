# exemple9.ps1
# Purely custom logic

function Call-ExternalAction {
    param([string]$Value)

    # Re-import the module (custom code only)
    Import-Module "$PSScriptRoot\exemple7.psm1"

    # Create custom class instance
    $tmp = [User]::new("Cross")

    # Use custom methods
    $msg = $tmp.BuildGreeting()
    $data = $tmp.BuildInternalData()

    # Use custom module function
    $v = Get-CustomVersion

    # Assign to variables only (no built-in output)
    $combined = $Value + "_" + $msg + "_" + $data + "_" + $v
}
