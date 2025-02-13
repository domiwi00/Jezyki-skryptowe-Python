@echo off
setlocal enabledelayedexpansion
set mypath="%~dp0"
cd %mypath%
echo %mypath%

echo 			Dominika Wisniewska 
echo 		zadanie 1 2020 "Miejskie Widoki"

:menu		
echo 	Menu
echo 1. Start programu
echo 2. Wyswietlenie raportu
echo 3. Opis programu
echo 4. Zakoncz

set /p wybor=Wybierz opcje: 

if %wybor%==1 goto start
if %wybor%==2 goto raport
if %wybor%==3 goto opis
if %wybor%==4 goto koniec

echo Wybierz liczbe 1 - 4
goto menu

:opis
echo Program tworzy tablice na podstawie liczby w pliku wejsciowym, w ktorej dana liczba ma sie nie powtarzac w danej kolumnie i wierszu.
echo Te liczby przedstawiaja ilosc pieter w budynku, ktory stoi w miejscu danej liczby. Nizsze bloki beda zasloniete przez wyzsze.
echo Z kazdej strony liczymy ile blokow jest widocznych.
echo Jesli program nie bedzie w stanie utworzyc tablicy w przeciagu 60 sekund, program przerwie dzialanie.
pause
goto menu

:start
if not exist "in" (
    echo Katalog "in" nie istnieje.
    pause
    exit /b 1
)

if not exist "out" (
    mkdir "out"
)

echo id pliku powinno odpowiadac liczbie wewnatrz pliku 
set /p id=Podaj id pliku in: 
echo sprawdz czy istnieje plik z koncowka %id%
if not exist %mypath%in\in%id%.txt (
    echo Taki plik nie istnieje.
    pause
    exit /b 1
)

python main.py in\in%id%.txt out\out%id%.txt

python raport.py

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
mkdir backups\"%fullstamp%"

xcopy in backups\"%fullstamp%"\in /E /I /Y
xcopy out backups\"%fullstamp%"\out /E /I /Y
copy *.html backups\"%fullstamp%"

pause
goto menu

:raport
start raport.html
if not exist raport.html (
    echo Nie ma zadnego raportu w katalogu
)
pause
goto menu

:koniec
pause
exit /b 0