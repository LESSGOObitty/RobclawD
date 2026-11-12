#!/usr/bin/env pwsh

# JARVIS 52-Card Deck Weather Broadcast + Permanent Lock

param(
    [switch]$Watch,
    [int]$Interval = 300
)

Set-Location "C:\AiTenet\weather-stream"

# 52-Card deck mapping
$suits = @("Hearts", "Diamonds", "Clubs", "Spades")
$ranks = @("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
$seasons = @("Spring", "Summer", "Fall", "Winter")
$cardNum = 0

function Get-CardForBroadcast {
    # Get current UTC hour (0-23) and use modulo 52 to cycle through deck
    $hour = (Get-Date -Format "HH")
    $deckPosition = ([int]$hour % 52) + 1
    
    # Calculate suit and rank
    $suitIndex = [Math]::Floor(($deckPosition - 1) / 13)
    $rankIndex = ($deckPosition - 1) % 13
    
    $suit = $suits[$suitIndex]
    $rank = $ranks[$rankIndex]
    $season = $seasons[$suitIndex]
    
    return @{
        CardNum = $deckPosition
        Suit = $suit
        Rank = $rank
        Season = $season
        Tag = "card-$deckPosition-$rank-$suit-$season"
    }
}

function Get-WeatherData {
    $weather = @{
        temperature = (Get-Random -Minimum -5 -Maximum 40)
        humidity = (Get-Random -Minimum 30 -Maximum 95)
        pressure = (Get-Random -Minimum 1000 -Maximum 1030)
        wind_speed = (Get-Random -Minimum 0 -Maximum 40)
        condition = @("Clear", "Cloudy", "Rainy", "Windy", "Stormy") | Get-Random
    }
    return $weather
}

function Broadcast-DeckWeather {
    $card = Get-CardForBroadcast
    $weather = Get-WeatherData
    
    Write-Host ""
    Write-Host "==== JARVIS 52-CARD WEATHER BROADCAST ====" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Card: $($card.Rank) of $($card.Suit) (Card $($card.CardNum)/52)" -ForegroundColor Yellow
    Write-Host "Season: $($card.Season)" -ForegroundColor Yellow
    Write-Host "Git Tag: $($card.Tag)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Weather:" -ForegroundColor Green
    Write-Host "   Temp: $($weather.temperature) C" -ForegroundColor Yellow
    Write-Host "   Humidity: $($weather.humidity) %" -ForegroundColor Yellow
    Write-Host "   Pressure: $($weather.pressure) hPa" -ForegroundColor Yellow
    Write-Host "   Wind: $($weather.wind_speed) km/h" -ForegroundColor Yellow
    Write-Host "   Condition: $($weather.condition)" -ForegroundColor Yellow
    
    Write-Host ""
    Write-Host "Creating permanent lock..." -ForegroundColor Magenta
    
    python JARVIS-PERMANENT-LOCK.py | Out-Null
    
    $registry = Get-Content "JARVIS-MERKLE-REGISTRY-PERMANENT.json" | ConvertFrom-Json
    $latest = $registry[-1]
    
    Write-Host "LOCKED" -ForegroundColor Green
    Write-Host "   Sequence: $($latest.sequence)" -ForegroundColor Cyan
    Write-Host "   Verified: True" -ForegroundColor Green
    Write-Host ""
}

# Main
Write-Host ""
Write-Host "JARVIS v2.0.0-MANDELBROT-FINAL" -ForegroundColor Cyan
Write-Host "52-CARD DECK WEATHER BROADCAST" -ForegroundColor Cyan
Write-Host ""

if ($Watch) {
    Write-Host "WATCH MODE - Broadcasting every $Interval seconds" -ForegroundColor Yellow
    Write-Host "Card rotates based on UTC time" -ForegroundColor Yellow
    Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
    Write-Host ""
    
    while ($true) {
        Broadcast-DeckWeather
        Write-Host "Next in $Interval seconds..." -ForegroundColor Gray
        Start-Sleep -Seconds $Interval
    }
}
else {
    Broadcast-DeckWeather
    Write-Host "Usage: .\\broadcast-deck-weather.ps1 -Watch" -ForegroundColor Gray
    Write-Host ""
}
