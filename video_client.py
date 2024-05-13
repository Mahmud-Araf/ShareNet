import cv2,socket,pickle


global is_running_client
is_running_client = True

def share_video_client(ip,port):

    cap = cv2.VideoCapture(0)

    global is_running_client
    is_running_client = True

    s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000) 
                
    while is_running_client:
        ret,photo = cap.read()      
        cv2.imshow('Your Video', photo) 
        ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),30]) 
        x_as_bytes = pickle.dumps(buffer)      
        s.sendto(x_as_bytes,(ip ,port ))
        cv2.waitKey(10)

    cv2.destroyWindow('Your Video') 
    cap.release()
    
    
def close_video_client():
    global is_running_client
    is_running_client = False

