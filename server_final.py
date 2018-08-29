import socket
import sys
import numpy as np
import pickle
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except (socket.error, msg) :
    print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
output1=np.array([1,-1,1]).reshape(1,3)
output2=np.array([1,1,-1]).reshape(1,3)
output3=np.array([-1,1,1]).reshape(1,3)
out=[output1,output2,output3]
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except (socket.error , msg):
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
print("\n")
print("\n")
while 1:
    d = s.recvfrom(10240)
    data = d[0]
    addr=d[1]
    d = s.recvfrom(1024)
    num=d[0]
    if not data: 
        break
    data=pickle.loads(data)
    #print(data)
    if(str(data)=="close"):
        print("closing the socket")
        #print("u")
        break
    num=pickle.loads(num)
    out=np.roll(out,num,axis=0)
    y=[]
    y1=np.dot(out[0],data.T)
    y1[y1<=0]=0
    y1[y1>0]=1
    y1=y1.tolist()

    y2=np.dot(out[1],data.T)
    y2[y2<=0]=0
    y2[y2>0]=1
    y2=y2.tolist()

    y3=np.dot(out[2],data.T)
    y3[y3<=0]=0
    y3[y3>0]=1
    y3=y3.tolist()
    y.extend(y1[0])
    y.extend(y2[0])
    y.extend(y3[0])

    g=[]
    for j in range(0,len(y),9):
        g.append(int(''.join(str(e) for e in y[j:j+9]),2))
    final_str=""
    for h in g:
        final_str=final_str+str(chr(h))
    print(final_str)
s.close()
