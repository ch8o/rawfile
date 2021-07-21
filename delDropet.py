import requests
import sys
import os


def getNewTeamDropetIps(bearer):
    resultList = []
    res = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=100',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer ' + bearer})
    if res.status_code == 200:
        json = res.json()
        for one in json['droplets']:
            for networkv4 in one['networks']['v4']:
                if networkv4['type'] == 'public':
                    resultList.append(networkv4['ip_address'])
    return resultList


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('arg1:old team bearer token')
        print('arg2:new team bearer token')
        print('arg3:newteam droplet to skip ( skip top n)')
        exit(-1)
    oldTeamBearer = sys.argv[1]
    newTeamBearer = sys.argv[2]
    skipTopN = ''
    if len(sys.argv) > 3:
        skipTopN = sys.argv[3]
    else:
        skipTopN = '0'

    newTeamIps = getNewTeamDropetIps(newTeamBearer)
    newTeamIps = newTeamIps[int(skipTopN):]
    if len(newTeamIps) == 0:
        print('newTeamIps size 0 exit')
        exit(-1)
    else:
        print('newTeamIps size:' + str(len(newTeamIps)))

    response = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=100',
                            headers={'Content-Type': 'application/json',
                                     'Authorization': 'Bearer ' + oldTeamBearer})
    if response.status_code == 200:
        result = response.json()
        for i, droplet in enumerate(result['droplets']):
            ipv4Addr = ''
            for networkv4 in droplet['networks']['v4']:
                if networkv4['type'] == 'public':
                    ipv4Addr = networkv4['ip_address']
            responseDel = requests.delete('https://api.digitalocean.com/v2/droplets/' + str(droplet['id']),
                                          headers={'Content-Type': 'application/json',
                                                'Authorization': 'Bearer ' + oldTeamBearer})
            if responseDel.status_code == 204:
                print('.sh ' + ipv4Addr + ' ' + newTeamIps[i] + ' ')
            else:
                print('delete failed:' + str(responseDel.status_code) + "|" + ipv4Addr)
            # testtesttesttesttesttesttest
            # break

