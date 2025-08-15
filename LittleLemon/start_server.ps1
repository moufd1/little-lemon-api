# Little Lemon API Startup Script
Write-Host "=== Little Lemon API ===" -ForegroundColor Green
Write-Host "Démarrage du serveur de développement..." -ForegroundColor Yellow
Write-Host ""

Set-Location "C:\Users\TRETEC\Desktop\little-lemon-api\LittleLemon"
& pipenv run python manage.py runserver
