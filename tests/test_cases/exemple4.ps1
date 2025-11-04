# ============================================
# Device Manager Simulation
# ============================================

function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] $Message"
}

class Device {
    [string]$Name
    [bool]$Online

    Device([string]$name) {
        $this.Name = $name
        $this.Online = $false
        & Write-Log "Device created: $name"
    }

    [void]Connect() {
        $this.Online = $true
        & Write-Log "$($this.Name) is now connected"
    }

    [void]Disconnect() {
        $this.Online = $false
        & Write-Log "$($this.Name) disconnected"
    }

    [void]Status() {
        if ($this.Online) {
            & Write-Log "$($this.Name) is ONLINE"
        }
        else {
            & Write-Log "$($this.Name) is OFFLINE"
        }
    }
}

# ============================================
# Usage
# ============================================

$printer = [Device]::new("Printer")
$printer.Connect()
$printer.Status()
$printer.Disconnect()
