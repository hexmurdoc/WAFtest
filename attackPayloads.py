import requests
import sys




host = sys.argv[1]
q_params = 'command=cmd.exe /C ping 1.1.1.1'
print('issue request to:'+ host+'/?'+q_params)
res  = requests.get('http://'+host+'/?'+q_params)

if res.status_code == 200 and 'incident' not in res.text :
    print("Passed the WAF")
else:
    print("stopped by the WAF")