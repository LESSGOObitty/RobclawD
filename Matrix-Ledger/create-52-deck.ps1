#!/usr/bin/env pwsh

Set-Location "C:\AiTenet\weather-stream"

$suits = @("Hearts", "Diamonds", "Clubs", "Spades")
$ranks = @("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
$seasons = @("Spring", "Summer", "Fall", "Winter")

$cardNum = 0

foreach ($suit in $suits) {
    foreach ($rank in $ranks) {
        $cardNum++
        $card = "$rank-$suit"
        
        $suitIndex = [array]::IndexOf($suits, $suit)
        $season = $seasons[$suitIndex]
        
        $tag = "card-$cardNum-$card-$season"
        $message = "JARVIS Weather: Card $cardNum ($card) - $season - Seq 45 - K=0.9999999997"
        
        git tag -a $tag -m "$message" 2>$null
        
        if ($cardNum % 13 -eq 0) {
            Write-Host "$suit completed: Cards $($cardNum-12)-$cardNum" -ForegroundColor Green
        }
    }
}

Write-Host ""
Write-Host "CREATED 52 CARD TAGS" -ForegroundColor Cyan
Write-Host "52 cards x 4 seasons = 52 permanent anchors" -ForegroundColor Cyan

git tag -l | Select-String "card-" | Measure-Object | Select-Object Count
