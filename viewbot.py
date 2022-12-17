import random
import requests
from pystyle import *

sendurl = "https://camo.githubusercontent.com/32d5f1ca52774c8b63492746ee3c1f510da8894fc5e5a15a09e703da2468bc8b/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6e6f747a73"

URL = "https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"
response = requests.get(URL)
open("user_agents.txt", "wb").write(response.content)
lines = open('user_agents.txt').read().splitlines()
myline = random.choice(lines)

user_agent = {'User-agent': myline}

print(myline)
i = 0

while i < 10000000:
  i = i + 1
  response = requests.get(sendurl, headers = user_agent)
  print(Colorate.Horizontal(Colors.rainbow,"sent +1 view to notzs"))