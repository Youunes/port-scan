print('devloper: younes abrane ')
print ('fb = https://www.facebook.com/gloria.decampospaulino')

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input("your ip : ")

def portsc(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,30):
    if portsc(x):
        print('[+] port',x,'is open|_____',x,'_______|')
    else:
        print('[-] port',x,'is closed|_____',x,'_______|')
        
