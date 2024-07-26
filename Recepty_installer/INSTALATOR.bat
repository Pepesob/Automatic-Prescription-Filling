cd Recepty
py -m venv venv
venv\Scripts\pip.exe install -r requirements.txt
cd ..
xcopy ".\Recepty" "C:\Recepty" /E /I /H /Y /Q
powershell -ExecutionPolicy Bypass -File ".\make_shortcut.ps1"
