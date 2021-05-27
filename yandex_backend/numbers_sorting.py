import sys
import requests
import json

address = sys.stdin.readline().strip()
port = sys.stdin.readline().strip()
param_a = int(sys.stdin.readline().strip())
param_b = int(sys.stdin.readline().strip())

response = requests.get(f'{address}:{port}', params={'a': param_a, 'b': param_b})

for i in sorted([int(x) for x in json.loads(response.content)]):
    print(i)
