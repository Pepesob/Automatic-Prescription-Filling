@echo off

py --version >nul 2>&1 && (
    echo Python jest juz na tym komputerze
    echo Kliknij enter aby zakonczyc
    pause
) || (
    curl https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe --output python_instaler.exe
    python_instaler
)
