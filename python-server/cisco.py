import requests
import json
import time
from requests.auth import HTTPBasicAuth


url1 = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
url2 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
url3 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-health'
url4 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/flow-analysis'
url5 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/topology/physical-topology'
url6 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/onboarding/pnp-device'
url7 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/discovery/count'
myusername = 'devnetuser'
mypassword = 'Cisco123!'

def get_token():
    token = requests.post(url1, auth=HTTPBasicAuth(myusername, mypassword),
                          headers={'content-type': 'application/json'},
                          verify=False,
                          )
    data1 = token.json()
    return data1['Token']

def get_devices(ticket):
    payload = ''
    newheaders = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
        }
    response = requests.request('GET', url2, data=payload, headers=newheaders)
    data2 = response.json()  # data2 为字典格式，带单引号，json.dumps(data2)为json格式，带双引号
    devices_num = len(data2['response'])
    devices = []
    for i in range(devices_num):
        devices.append({})
    reachable_devices_num = 0
    WirelessController_num = 0
    Switches_Hubs_num = 0
    Unified_AP_num = 0
    n = 0
    for j in data2['response']:
            devices[n]['hostname'] = j['hostname']
            devices[n]['series'] = j['series']
            devices[n]['macAddress'] = j['macAddress']
            devices[n]['managementIpAddress'] = j['managementIpAddress']
            devices[n]['id'] = j['id']
            devices[n]['type'] = j['family']
            if j['reachabilityStatus'] == 'Reachable':
                reachable_devices_num += 1
                # print('{:30}'.format(j['hostname']) + ' ' + '{:50}'.format(j['series']) + ' ' + j['managementIpAddress'])
            if j['family'] == 'Wireless Controller':
                WirelessController_num += 1
            if j['family'] == 'Switches and Hubs':
                Switches_Hubs_num += 1
            if j['family'] == 'Unified AP':
                Unified_AP_num += 1
            n += 1
    type_num = {'total_devices_num': devices_num, 'reachable_devices_num': reachable_devices_num, 'WirelessController_num': WirelessController_num,
                'Switches_Hubs_num': Switches_Hubs_num, 'Unified_AP_num': Unified_AP_num}
    devices_data = {'devices': devices, 'type_num': type_num}
    return devices_data


def get_timestamp():
    t = time.time()
    nowtime = lambda: int(round(t*1000))
    return nowtime()


def get_network_health(ticket):
    payload = ''
    headers = {
        'X-Auth-Token': ticket,
        'Content-Type': "application/json",
        }
    timestamp = str(get_timestamp())
    params = {'timestamp': timestamp}
    # print(timestamp)
    response = requests.request('GET', url3, data=payload, headers=headers, params=params)
    data2 = response.json()
    health_data = {}
    health_data['overall_health'] = {}
    health_data['overall_health']['overall_healthScore'] = data2['response'][0]['healthScore']
    health_data['overall_health']['totalCount'] = data2['response'][0]['totalCount']
    health_data['overall_health']['goodCount'] = data2['response'][0]['goodCount']
    health_data['overall_health']['fairCount'] = data2['response'][0]['fairCount']
    health_data['overall_health']['badCount'] = data2['response'][0]['badCount']
    health_data['overall_health']['timeinMillis'] = data2['response'][0]['timeinMillis']
    for i in range(len(data2['healthDistirubution'])):
        health_data[str(data2['healthDistirubution'][i]['category'])] = {}
        health_data[str(data2['healthDistirubution'][i]['category'])]['overall_healthScore'] = data2['healthDistirubution'][i]['healthScore']
        health_data[str(data2['healthDistirubution'][i]['category'])]['totalCount'] = data2['healthDistirubution'][i]['totalCount']
        health_data[str(data2['healthDistirubution'][i]['category'])]['goodCount'] = data2['healthDistirubution'][i]['goodCount']
        health_data[str(data2['healthDistirubution'][i]['category'])]['badCount'] = data2['healthDistirubution'][i]['badCount']
        health_data[str(data2['healthDistirubution'][i]['category'])]['fairCount'] = data2['healthDistirubution'][i]['fairCount']
    return health_data


def get_users(ticket):
    payload = ''
    newheaders = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
    }
    ap = []
    # host = {'wired': [], 'wireless': []}
    hosts = []
    response = requests.request('GET', url5, data=payload, headers=newheaders)
    devices_data = get_devices(token)['devices']
    data2 = response.json()
    for i in range(len(data2['response']['nodes'])):
        if data2['response']['nodes'][i]['family'] == 'Unified AP':
            ap.append({'label': str(data2['response']['nodes'][i]['label']),
                       'ip': str(data2['response']['nodes'][i]['ip']),
                       'id': str(data2['response']['nodes'][i]['id'])})
        if data2['response']['nodes'][i]['role'] == 'HOST':
            hosts.append({'id': str(data2['response']['nodes'][i]['id']),
                          'ip': str(data2['response']['nodes'][i]['ip']),
                          'macaddress': str(data2['response']['nodes'][i]['additionalInfo']['macAddress'])})
            # if data2['response']['nodes'][i]['deviceType'] == 'wired':
            #     host['wired'].append({'id': str(data2['response']['nodes'][i]['id']),
            #                           'ip': str(data2['response']['nodes'][i]['ip']),
            #                          'macaddress': str(data2['response']['nodes'][i]['additionalInfo']['macAddress'])})
            # elif data2['response']['nodes'][i]['deviceType'] == 'wireless':
            #     host['wireless'].append({'id': str(data2['response']['nodes'][i]['id']),
            #                              'ip': str(data2['response']['nodes'][i]['ip']),
            #                              'macaddress': str(data2['response']['nodes'][i]['additionalInfo']['macAddress'])})
    for j in range(len(devices_data)):
        devices_data[j]['link'] = []
    for i in range(len(data2['response']['links'])):
        for j in range(len(devices_data)):
            if devices_data[j]['id'] == data2['response']['links'][i]['source']:
                for k in range(len(hosts)):
                    if hosts[k]['id'] == data2['response']['links'][i]['target']:
                        devices_data[j]['link'].append(hosts[k])
                # for m in range(len(devices_data)):
                #     if devices_data[m]['id'] == data2['response']['links'][i]['target']:
                #         devices_data[j]['link'].append({'id': devices_data[m]['id'],
                #                                         'ip': devices_data[m]['managementIpAddress'],
                #                                         'macaddress': devices_data[m]['macAddress']})
                #         devices_data[m]['link'].append({'id': devices_data[j]['id'],
                #                                         'ip': devices_data[j]['managementIpAddress'],
                #                                         'macaddress': devices_data[j]['macAddress']})
    data = []
    for i in range(len(devices_data)):
        if devices_data[i]['link']:
            data.append(devices_data[i])
    return data
    print(json.dumps(data, indent=4, separators=(',', ':')))


token = get_token()
devices_data = get_devices(token)
devices_health_data = get_network_health(token)
host_data = get_users(token)
devices_data['devices_health_data'] = devices_health_data
devices_data['host_data'] = host_data
print(json.dumps(devices_data, indent=4, separators=(',', ':')))


