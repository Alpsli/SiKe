
import requests
import json
import time
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


url1 = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
url2 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
url3 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request'
url4 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/flow-analysis'
# url5 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-health'
url8 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/onboarding/pnp-device'
url9 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/discovery/count'
myusername = 'devnetuser'
mypassword = 'Cisco123!'

# 获取token
def get_token():
    token = requests.post(url1, auth=HTTPBasicAuth(myusername, mypassword),
                          headers={'content-type': 'application/json'},
                          verify=False,
                          )
    data1 = token.json()
    return data1['Token']

# 获取设备
def get_devices(ticket):
    n = 0
    payload = ''
    newheaders = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
        }
    response = requests.request('GET', url2, data=payload, headers=newheaders)
    data2 = response.json()
    print(json.dumps(data2, indent=4, separators=(',', ':')))
    for i in data2['response']:
        if i['reachabilityStatus']== 'Reachable':
            n+=1
            print('{:30}'.format(i['hostname']) + ' ' +'{:50}'.format(i['series']) + ' ' + i['managementIpAddress'] )
    print('Total %d reachable devices' %n)

#获取设备版本
def get_version(ticket):
    payload = "{\n\t\"commands\" : " \
              "[\n\t\t\"show version\"\n\t]," \
              "\n\t\"description\": \"Command Runner @ Cisco Live 2018 - API call\",\n\t\"" \
              "deviceUuids\": [\n\t\t\"3a909883-948f-47c2-8e34-65a740ab423e\"\n\t]\n}"
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
    }
    response = requests.request("POST", url3, data=payload, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4, separators=(',', ':')))

#获取流
def get_flow_analysis(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
    }
    response = requests.request("GET", url4, data=payload, headers=headers)
    data = response.json()
    flow_id = []
    for i in range(len(data['response'])):
        flow_id.append(data['response'][i]['id'])
    print(json.dumps(data, indent=4, separators=(',', ':')))
    return flow_id

#通过id获取流信息
def get_flow_id(ticket, flow_id):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
    }
    url5 = url4 + '/' + str(flow_id[0])
    response = requests.request("GET", url5, data=payload, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4, separators=(',', ':')))
#获取时间戳
def get_timestamp():
    t = time.time()
    nowtime = lambda:int(round(t*1000))
    return nowtime()
#获取网络整体健康状况
def get_network_health(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
        }
    url6 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-health' + '?timestamp=' + str(get_timestamp())
    response = requests.request('GET', url6, data=payload, headers=headers)
    data2 = response.json()
    print(json.dumps(data2, indent=4, separators=(',', ':')))
#获取站点健康状况
def get_site_health(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
        }
    url7 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/site-health' + '?timestamp=' + str(get_timestamp())
    response = requests.request('GET', url7, data=payload, headers=headers)
    data2 = response.json()
    print(json.dumps(data2, indent=4, separators=(',', ':')))
#获取即插即用设备列表
def get_pnp_device(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
    }
    response = requests.request('GET', url8, data=payload, headers=headers)
    data2 = response.json()
    print(json.dumps(data2, indent=4, separators=(',', ':')))

def get_discovery_count(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
    }
    response = requests.request('GET', url9, data=payload, headers=headers)
    data2 = response.json()
    print(json.dumps(data2, indent=4, separators=(',', ':')))

ticket = get_token()

get_devices(ticket)
# get_version(ticket)
# flow_id = get_flow_analysis(ticket)
# get_flow_id(ticket, flow_id)
# get_network_health(ticket)
# get_site_health(ticket)
# get_pnp_device(ticket)
# get_discovery_count(ticket)