#!/usr/bin/python
import requests
import json
import sys

hostname = sys.argv[1]
host_ip = sys.argv[2]
host_group_id = sys.argv[3]
template_id = sys.argv[4]
zabbix_username = sys.argv[5]
zabbix_password = sys.argv[6]
url = sys.argv[7]


def get_auth_key():
    payload = {'jsonrpc': '2.0', 'method': 'user.login', 'params': {'user': zabbix_username, 'password': zabbix_password}, 'id': '1'}
    auth = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}, verify=False)

    if auth.status_code != 200:
        print 'Authorization error'
        print auth.status_code
        print auth.text
        sys.exit()
    else:
        result = auth.json()
        auth_key = result['result']
        return auth_key


def create_host(auth_key):
    payload =\
    {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": hostname,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": host_ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": host_group_id
                }
            ],
            "templates": [
                {
                    "templateid": template_id
                }
            ],
        },
        "auth": auth_key,
        "id": 1
    }

    host = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}, verify=False)
    if host.status_code != 200:
        result = host.json()['error']
        print 'Host creation error'
        print host.status_code
        print host.text
        print result
        sys.exit()
    else:
        result = host.json()['result']
        host_id = result['hostids'][0]
        return host_id

key = get_auth_key()
created_host_id = create_host(key)
print created_host_id