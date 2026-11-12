#!/usr/bin/env pwsh

# JARVIS Permanent Lock Trigger
# Usage:
#   .\trigger-jarvis-lock.ps1                 # Single trigger
#   .\trigger-jarvis-lock.ps1 -Watch          # Auto-trigger every 5 minutes
#   .\trigger-jarvis-lock.ps1 -Watch -Interval 60   # Every 60 seconds

param(
    [switch]$Watch,
    [int]$Interval = 300
)

Set-Location "C:\AiTenet\weather-stream"

function Trigger-Lock {
    Write-Host ""
    Write-Host "=== JARVIS PERMANENT LOCK TRIGGER ===" -ForegroundColor Cyan
    Write-Host "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') UTC" -ForegroundColor Gray
    
    python JARVIS-PERMANENT-LOCK.py | Out-Null
    
    $registry = Get-Content "JARVIS-MERKLE-REGISTRY-PERMANENT.json" | ConvertFrom-Json
    $count = @($registry).Count
    $latest = $registry[-1]
    
    Write-Host ""
    Write-Host "Sequence: $($latest.sequence)" -ForegroundColor Green
    Write-Host "Timestamp: $($latest.timestamp_utc)" -ForegroundColor Gray
    Write-Host "Merkle: $($latest.merkle_root.Substring(0, 24))..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Total in Chain: $count" -ForegroundColor Cyan
}

# Main
Write-Host ""
Write-Host "JARVIS v2.0.0-MANDELBROT-FINAL" -ForegroundColor Cyan
Write-Host "Permanent Lock Trigger" -ForegroundColor Cyan

if ($Watch) {
    Write-Host ""
    Write-Host "WATCH MODE - Auto-triggering every $Interval seconds" -ForegroundColor Yellow
    Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
    
    while ($true) {
        Trigger-Lock
        Write-Host "Next in $Interval seconds..." -ForegroundColor Gray
        Start-Sleep -Seconds $Interval
    }
}
else {
    Trigger-Lock
    Write-Host "Use -Watch to auto-trigger every 5 minutes" -ForegroundColor Gray
    Write-Host ""
}
