
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\Automatyczne wype³nianie recept.lnk")
$Shortcut.TargetPath = "C:\Recepty\runProgram.bat"
$Shortcut.WorkingDirectory = "C:\Recepty"
$Shortcut.IconLocation = "C:\Recepty\src\resources\prescription_icon_with_background.ico"
$Shortcut.Save()