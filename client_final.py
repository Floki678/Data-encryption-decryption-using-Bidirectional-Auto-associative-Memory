import socket   #for sockets
import sys  #for exit
import pickle
import numpy as np
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except (socket.error):
    print ('Failed to create socket')
    sys.exit()
 
host = ('localhost');
port = 8888;
output1=np.array([1,-1,1]).reshape(1,3)
output2=np.array([1,1,-1]).reshape(1,3)
output3=np.array([-1,1,1]).reshape(1,3)
out=[output1,output2,output3]
d=True
while(d==True):
   # print("m")
    print("Enter the message:")
    i=input()
    if(i=="close"):
        msg=pickle.dumps("close")
        s.sendto(msg,(host, port))
        d=False
    leni=len(i)
    input_m=[]
    for ii in i:
        input_m=input_m+list(map(int,bin(ord(ii))[2:].zfill(9)))
    col=int(len(input_m)/3)
    input_m=np.array(input_m).reshape(3,col)
    input_m1=input_m[0].reshape(col,1)
    input_m2=input_m[1].reshape(col,1)
    input_m3=input_m[2].reshape(col,1)
    
    try :
        num=np.random.randint(1,5)
        out=np.roll(out,num,axis=0)
        num=pickle.dumps(num)   
        weight=np.dot(input_m1,out[0])+np.dot(input_m2,out[1])+np.dot(input_m3,out[2])
        print(weight)
        msg=pickle.dumps(weight) 
        s.sendto(msg,(host, port))
        s.sendto(num,(host,port))
    except (socket.error, msg):
        msg=pickle.loads(msg)
        sys.exit() 
s.close()
