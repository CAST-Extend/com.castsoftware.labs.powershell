# ============================================
# Module: Network Tools
# ============================================

function Test-HostConnection {
    param([string]$HostName)
    try {
        Test-Connection -ComputerName $HostName -Count 1 -Quiet
    } catch {
        Write-Error "Failed to connect to $HostName"
    }
}

function Resolve-HostIP {
    param([string]$HostName)
    try {
        $ip = [System.Net.Dns]::GetHostAddresses($HostName)
        Write-Host "$HostName -> $($ip[0].IPAddressToString)"
    } catch {
        Write-Error "Could not resolve host"
    }
}

function Ping-And-Report {
    param([string]$HostName)
    if (Test-HostConnection $HostName) {
        Resolve-HostIP $HostName
    } else {
        Write-Host "Host is unreachable"
    }
}
