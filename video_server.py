import cv2,socket,pickle


port = 2222
ip = "localhost"
global is_running_server
is_running_server = True

def share_video_server():

    global is_running_server
    is_running_server = True
    s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)       
    s.bind((ip,port)) 

    while is_running_server:
        x=s.recvfrom(100000000)             
        data=x[0]                  
        data=pickle.loads(data)   
        data = cv2.imdecode(data, cv2.IMREAD_COLOR) 
        cv2.imshow('Client Video', data)
        cv2.waitKey(10)
    
    cv2.destroyWindow('Client Video') 

def close_video_server():
    global is_running_server
    is_running_server = False