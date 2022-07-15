echo "STARTING..."
cmd.exe /c "start .\psiphon3.exe" 

timeout 6 

echo "[!] Starting the Web scrapping script..."
cmd.exe /c "python .\main2.py"



echo "[+] File formed."

echo " Killing the VPN"
taskkill /IM psiphon3.exe.exe

echo "Scrapping Complete"