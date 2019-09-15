import requests
import sys




host = sys.argv[1]
q_params = 'a=cmd.exe /c ping 1.1.1.1'
res  = requests.get(host+'?'+q_params)

if res.status_code == 200 and 'incident' not in res.text :
    print("Passed the WAF")
else:
    print("stopped by the WAF")