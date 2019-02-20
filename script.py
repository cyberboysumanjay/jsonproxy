def push_to_git():
    #Import dependencies
    from subprocess import call
    #Commit Message
    commit_message = "Updating json files"
    #Stage the file
    call('git add .', shell = True)
    # Add your commit
    call('git commit -m "'+ commit_message +'"', shell = True)
    #Push the new or update files
    call('git push origin master', shell = True)
import json,requests,urllib.request
from traceback import print_exc

def get_proxy():
    proxies=[]
    i,c=0,0
    while(c!=10):
        try:
            url = 'http://pubproxy.com/api/proxy?country=IN&limit=20&https=True&user_agent=true'
            resp = requests.get(url=url)
            data = resp.json()
            pprint.pprint(data)
            for proxy in data['data']:
                proxies.append(proxy['ipPort'])

            #print('Direct Pubproxy accessed')
        except Exception as e:
            print(e.__class__.__name__)
            print_exc()
            i=1
            try:
                proxies=proxies+spy_proxy()
                #print('Spy Proxy accessed')
            except Exception as e:
                print(e)
                exit()
        c=c+1
        print(str(c)+'th Attempt taken')
    return proxies

import pprint
#print((get_proxy()))
def spy_proxy():
    resp=requests.get('http://spys.me/proxy.txt')

    #print(resp.text)
    data=((resp.text).split("Google_passed(+)")[1]).split('\r')[0]
    data=data.split('\n')
    #print(data)
    l=[]
    for i in data:
        if 'IN' in i:
            i=i.split(' IN')[0]
            l.append(i)
    return l

proxy_json={'data':get_proxy()}

import json
with open('proxy.json', 'w') as outfile:
    json.dump(proxy_json, outfile)
push_to_git()
