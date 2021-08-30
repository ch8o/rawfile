import requests
import os
import time
import sys

APIKEY = 'AIzaSyBfUOoC0chroUi1rhWL0vIrquBDHQxa1UE'
BEARER_TOKEN = 'ya29.a0ARrdaM-wvpepjeiDeKPU5tuMjp-butUrdh-Z6uwUQ1Eikx6qVA-Aj0mhw5ZPqqLPHtZPkaZg0WDSflXgBaE-RZm9TCO58wK4yPL_dzNoNkx0DnP6j8SSM1lqqF3c3e_Zp4t-SYvxTCn04tbonO2r52j2KJjl'
PROJID = 'still-manifest-324108'
TEMPLATE = 'instance-template-1'
ZONE = 'asia-northeast3-a'


def checkStatus(iname):
    response = requests.get(
        'https://compute.googleapis.com/compute/v1/projects/' + PROJID + '/zones/' + ZONE + '/instances/' + iname + '?key=' + APIKEY,
        headers={'Authorization': 'Bearer ' + BEARER_TOKEN,
                 'Accept': 'application/json'})
    if response.status_code == 200:
        i_obj = response.json()
        if i_obj['status'] == 'RUNNING':
            print('instance is RUNNING!')
            return i_obj['networkInterfaces'][0]['accessConfigs'][0]['natIP']
        else:
            print('Instance not ready...')
    else:
        print('checkStatus status code:' + str(response.status_code))
        print(response.json())
    return ''


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('arg1:instance name')
        exit(-1)

    name = sys.argv[1]
    url = 'https://compute.googleapis.com/compute/v1/projects/' + PROJID + '/zones/' + ZONE + '/instances?sourceInstanceTemplate=global%2FinstanceTemplates%2F' + TEMPLATE + '&key=' + APIKEY
    print(url)
    body = '{"machineType":"zones/' + ZONE + '/machineTypes/e2-micro","name":"' + name + '"}'
    print(body)
    create_response = requests.post(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer ' + BEARER_TOKEN,
                                             'Accept': 'application/json'},
                                    data=body)

    if create_response.status_code == 200:
        obj = create_response.json()
        print(obj)
        print('creating......')
        time.sleep(10)
        ipv4Addr = ''
        while ipv4Addr == '':
            time.sleep(3)
            ipv4Addr = checkStatus(name)
        print('Success created, ip address is :' + ipv4Addr)
        print('waiting 60s...')
        time.sleep(60)
        print(os.system("~/gcp-remote-meson.sh " + ipv4Addr))
    else:
        print('status code:' + str(create_response.status_code))
        print(create_response.json())
