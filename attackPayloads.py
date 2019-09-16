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


s = requests.Session()
res = s.get('http://'+host+':8080/acme-webapp-java/')
cookie = s.cookies.get_dict()
headers = res.headers

a={
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Pragma': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
   'Origin': 'http://35.169.203.9:8080',
    'Referer': 'http://35.169.203.9:8080/acme-webapp-java/',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
   'X-Requested-With': 'XMLHttpRequest'}

# a.update(cookie)

params = {'symbol':'\' or 1=1;--'}
# params = {'symbol':'google'}
res  = s.post('http://'+host+':8080/acme-webapp-java/search',data= params,headers= a )
if 'incident' not in res.text  or 'com.prevoty' not in res.text:
    print("stopped by the WAF")
else:
    print("Passed the WAF")



