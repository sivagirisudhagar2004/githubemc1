import subprocess
import re

#Get saved Wi-Fi profiles
result = subprocess.check_output(
    "netsh wlan show profiles",
    shell=True, text=True, encoding="utf-8", errors="ignore"
)

#Extract profile names
profiles = []
for line in result.splitlines():
    if("All User Profile" in line):
        name = line.split(":")[1].strip()
        profiles.append(name)
#Show profiles
print("Saved Wi-fi Profiles : ")
for i, name  in enumerate(profiles,1):
    print(f"[{i}] {name}")
#Choose a profile
choice = int(input("\n Enter wi-Fi number to view password : "))
ssid = profiles[choice - 1]

#Get password for selected profile
result = subprocess.check_output(
    f'netsh wlan show profile name = "{ssid}" key = clear',
    shell=True, text=True, encoding="utf-8", errors="ignore"
)

# Extract password(Key Content)
match = re.search(r"Key content\s*:\s*.(.*)",result)
if(match):
    print(f"\n Password : {match.group(1).strip()}")
else:
    print("\n Password not found  or not saved for this Wi-Fi.")