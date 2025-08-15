@echo off
echo === Little Lemon API ===
echo Démarrage du serveur de développement...
echo.

cd /d "C:\Users\TRETEC\Desktop\little-lemon-api\LittleLemon"
pipenv run python manage.py runserver

pause
