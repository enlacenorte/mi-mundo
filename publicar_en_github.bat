@echo off
chcp 65001 >nul
echo ===================================================
echo   SUBIR MI MUNDO A GITHUB (OPEN SOURCE + PAGES)
echo ===================================================
echo.

cd /d "%~dp0"

echo [1/3] Verificando inicio de sesión en GitHub CLI...
gh auth status >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo No has iniciado sesión en GitHub CLI aún.
    echo Se abrirá tu navegador para autorizar GitHub en un solo clic...
    echo.
    gh auth login --web --git-protocol https
)

echo.
echo [2/3] Creando repositorio público 'mi-mundo' en tu cuenta de GitHub...
gh repo create mi-mundo --public --source=. --remote=origin --push --description "🌐 Mi Mundo (My World) - Interactive Vector Globe & Capitals Game for Francisco Giudice"

echo.
echo [3/3] Habilitando GitHub Pages automáticamente...
gh repo edit --enable-pages --pages-branch main

echo.
echo ===================================================
echo   ¡PROYECTO PUBLICADO CON ÉXITO EN GITHUB!
echo ===================================================
echo Repositorio: https://github.com/enlacenorte/mi-mundo
echo Acceso Web:  https://enlacenorte.github.io/mi-mundo/
echo.
pause
