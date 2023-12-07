import json
import os
import sys
import requests

try: latest_release = requests.get('https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest')
except Exception as e:
    print(e)
    sys.exit(-1)
json_release = json.loads(latest_release.text)
for i in json_release['assets']:
    if i["name"].find("Lin64.tar.gz") != -1:
        download_url = i['browser_download_url']

os.system(f'wget {download_url} -O lolminer.tar.gz')
os.system('mkdir temp')
try: os.system(f"tar -xvf lolminer.tar.gz -C temp")
except Exception as e:
    print(e)
    sys.exit(-1)
folder = os.listdir('temp')[0]
os.system("mkdir lolminer")
os.system(f"cp -r temp/{folder}/* lolminer")
