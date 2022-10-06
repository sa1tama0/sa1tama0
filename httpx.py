import requests
import sys
import urllib3

# Usages
# python3 httpx.py url.txt
# If you don't have httpx, But you have python. It will do your job.

urllib3.disable_warnings()
s=requests.session()
proxy={"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}
f=open(sys.argv[1], "r")
for line in f:
    line=line.strip()
    page = s.get(line,verify=False,proxies=proxy)
    print(page.status_code)
f.close()
