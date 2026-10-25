import subprocess

profiles = subprocess.check_output('netsh wlan show profiles', shell=True).decode('utf-8', errors='ignore')

names = [line.split(':')[1].strip() for line in profiles.split("\n") 
         if 'All User Profile' in line]

for i, n in enumerate(names, start=1):
    print(f"[{i}] {n}")

ch = int(input("\nChoose Wifi number to see password: "))

wifi_name = names[ch - 1]

result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear']).decode('utf-8', errors='ignore')

for line in result.split('\n'):

    if 'Key Content' in line:
        print("  " + line.split(':')[1].strip())

print(f"\nPassword for '{wifi_name}' is displayed above.")

print("[+] Password: " + result.split('Key Content')[1].split(':')[1].strip())