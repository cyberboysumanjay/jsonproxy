import requests,json
r=requests.get('https://cyberboysumanjay.github.io/jsonproxy/proxy.json')
r_json=r.json()
print(len(r_json['data']))
