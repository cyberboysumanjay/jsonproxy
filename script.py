from gevent import monkey
monkey.patch_all()
import time
import getproxy
import requests
import urllib.request
from traceback import print_exc
from ast import literal_eval
import pprint
from datetime import datetime
from pytz import timezone
import schedule
import json

def set_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        np_list.append(i)
    #print(len(np_list))
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    print(len(proxy))
    return(proxy)

def push_to_git():
    #Import dependencies
    from subprocess import call
    #Commit Message
    india = timezone('Asia/Kolkata')
    in_time = datetime.now(india)
    commit_message= ("Updated at "+ str(in_time.strftime('%H-%M-%S'))+" IST")
    #Stage the file
    call('git add .', shell = True)
    # Add your commit
    call('git commit -m "'+ commit_message +'"', shell = True)
    #Push the new or update files
    call('git push origin master', shell = True)

def get_proxy():
    proxies=[]
    user_agent = {'User-agent': 'Mozilla/5.0'}
    proxy=set_proxy()
    i,j=0,0

    try:
        print("Entered getproxylist")
        proxies=proxies+getproxylist()
    except Exception:
        pass
    try:
        print("Entered Spy proxy")
        proxies=proxies+spy_proxy()
        print("Length after spy Proxy is ",len(proxies))
    except Exception :
        pass
    try:
        print('Entered Fate Proxy')
        proxies=proxies+fate_proxy()
        print("Length after fate Proxy is ",len(proxies))
    except Exception:
        pass
    try:
        print("Entered gatherproxy")
        proxies=proxies+gatherproxy()
        print("Length after gatherproxy is ",len(proxies))
    except Exception:
        pass

    for p in proxy:
        url = 'http://pubproxy.com/api/proxy?country=IN&limit=20&https=True&user_agent=true'
        while(len(proxies)<100):
            try:
                j=0
                resp = requests.get(url=url,headers=user_agent,proxies={"http": p, "https": p})
                data = resp.json()
                time.sleep(2.1)
                for proxy in data['data']:
                    proxies.append(proxy['ipPort'])
                print('Length of Proxy till '+str(i)+'th attempt is ',len(proxies))
            except Exception as e:
                print(resp.text)
                print('Skipped proxy '+str(p)+" "+str(i)+' time')
                break
            finally:
                i=i+1

    return list(set(proxies))

def gatherproxy():
    r=requests.get('http://www.gatherproxy.com/proxylist/country/?c=india')
    a=str(r.text)
    b=(a.split('gp.insertPrx('))
    l,pl=[],[]
    for i in b:
      if ');' in i:
        i=i.split(');')[0]
        l.append(i)
    for i in l:
      d=json.loads(i)
      port=i = int(d['PROXY_PORT'], 16)
      p=(str(d['PROXY_IP']+":"+str(port)))
      pl.append(p)
    return pl

def getproxylist():
    url='https://api.getproxylist.com/proxy?country[]=IN&lastTested=600'
    p=requests.get(url).json()
    l=[]
    l.append(str(p['ip'])+':'+str(p['port']))
    return l

def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    return(proxy)

def spy_proxy():
    resp=requests.get('http://spys.me/proxy.txt')
    data=((resp.text).split("Google_passed(+)")[1]).split('\r')[0]
    data=data.split('\n')
    l=[]
    for i in data:
        if 'IN' in i:
            i=i.split(' IN')[0]
            l.append(i)
    return l

def start():
    proxy_json={'data':get_proxy()}
    with open('proxy.json', 'w') as outfile:
        json.dump(proxy_json, outfile)
    push_to_git()


start()
