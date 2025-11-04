# ============================================
# System Monitor Script
# ============================================

function Get-CPUUsage {
    $cpu = Get-Counter '\Processor(_Total)\% Processor Time'
    return [math]::Round($cpu.CounterSamples.CookedValue, 2)
}

function Get-MemoryUsage {
    $mem = Get-Counter '\Memory\Available MBytes'
    return [math]::Round($mem.CounterSamples.CookedValue, 2)
}

function Write-SystemReport {
    $cpu = Get-CPUUsage
    $mem = Get-MemoryUsage
    Write-Host "CPU Usage: $cpu%"
    Write-Host "Memory Available: $mem MB"
}

# main logic
while ($true) {
    Write-SystemReport
    Start-Sleep -Seconds 5
}
