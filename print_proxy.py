import requests,json
r=requests.get('http://sumanjay.ooo/jsonproxy/proxy.json')
r_json=r.json()
print(len(r_json['data']))
