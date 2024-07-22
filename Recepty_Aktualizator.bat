curl -L --output Recepty.zip http://github.com/Pepesob/Automatic-Prescription-Filling/archive/master.zip
tar -xf Recepty.zip

cd ".\Automatic-Prescription-Filling-master\Recepty_installer"
call INSTALATOR.bat

cd ..\..
del Recepty.zip
rmdir /s /q Automatic-Prescription-Filling-master


