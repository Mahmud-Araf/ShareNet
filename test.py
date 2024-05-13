
from tkinter import *
from tkinter import filedialog
import os,socket,ipaddress,threading,time
from GradientFrame import GradientFrame
from video_server import share_video_server,close_video_server
from video_client import share_video_client,close_video_client
from audio_server import share_audio_server,close_audio_server
from audio_client import share_audio_client,close_audio_client

root = Tk()
root.title("ShareNet")
root.geometry("450x560")
root.configure(bg="#f4fdfe")
root.resizable(False, False)




def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def other_share():

    root.withdraw()
    window = Toplevel(root)
    window.title("Other Share")
    window.geometry('450x560+500+200')
    window.configure(bg='#f4fdfe')
    window.resizable(False, False)
    
    gf = GradientFrame(window, colors = ("white", "pink"), width = 800, height = 600)
    gf.config(direction = gf.top2bottom)
    gf.pack()

    def video_btn():
        print("Video button clicked")
        ip = IP_Input.get()
        
        if is_valid_ip(ip):
            t1 = threading.Thread(target=share_video_server)
            t2 = threading.Thread(target=share_video_client,args=(ip,))
            t1.start()
            time.sleep(5)
            t2.start()

    def cancel_video_btn():

        print("Cancel video button pressed")

        close_video_server()

        time.sleep(0.5)

        close_video_client()

        window.protocol("WM_DELETE_WINDOW", on_closing)
        

    def back_btn():
        print("Back button pressed")
        window.withdraw()
        root.deiconify()
        

    def connect_btn():
        print("connect button pressed")
        ip = IP_Input.get()
        if is_valid_ip(ip):
            cnt_btn.destroy()
            Label(window, text=f'      Connected      ', font=('Calibari', 20), bg='#f4fdfe', fg="#000").place(relx=0.5, y=250,anchor='center')

    def share_audio_btn():
        print("share your audio button pressed")

        ip = IP_Input.get()

        if is_valid_ip(ip):
            share_audio_server()
            share_audio_client(ip)

        

    def cancel_audio_btn():
        print("Cancel audio button pressed")

        close_audio_server()
        close_audio_client()
        
        window.protocol("WM_DELETE_WINDOW", on_closing)


    

    # icon
    image_icon1 = PhotoImage(file="Assets/screenshare.png")
    window.iconphoto(False, image_icon1)

    host = socket.gethostname()
    ip_address = socket.gethostbyname(host)

    Label(window, text=f'User IP: {ip_address}', bg='#fff', fg='#000', font=('Times New Roman', '20')).place(relx=0.5, y=80,anchor='center')

    global cnt_btn
    imgc = PhotoImage(file="Assets/connect.png")
    cnt_btn = Button(window, compound=LEFT, image=imgc,text="connect", width=280, font='caliabri 14 bold', bg='#f4fdfe', fg="#000",
                     command=connect_btn)
    cnt_btn.place(relx=0.5, y=250,anchor='center')

    IP_Input = Entry(window, width=25, fg="black", border=4, bg='white', font=('arial', 15),justify='center')
    IP_Input.place(relx=0.5, y=170,anchor='center')
    IP_Input.focus()
    IP_Input.insert(0, "Give Receiver IP Address")
    
    connect_image = PhotoImage(file="Assets/audio.png")
    Button(window, image=connect_image, bg='#ffd0df',activebackground='#ffd0df', bd=0,
       command=share_audio_btn).place(relx=0.5, y=330, x=-50, anchor='center')

    cancel_image = PhotoImage(file="Assets/cancelcall.png")
    Button(window, image=cancel_image, bg='#ffd0df',activebackground='#ffd0df', bd=0, 
       command=cancel_audio_btn).place(relx=0.5, y=330, x=50, anchor='center')
    
    
    imgv = PhotoImage(file="Assets/video.png")
    Button(window, image=imgv, bg='#ffd0df', bd=0,activebackground='#ffd0df',
           command=video_btn).place(relx=0.5,x=-80, y=410)
    
    cancel_video_img = PhotoImage(file="Assets/videocancel.png")
    Button(window, image=cancel_video_img, bg='#ffd0df',activebackground='#ffd0df', bd=0,
           command=cancel_video_btn).place(relx=0.5,x=30, y=420)
    
   
    Button(window, text="Back",font=('Calibari',15,'bold'),height=1, width=6, bg='#ffffff', activebackground='#ffffff', command=back_btn).place(relx=0.5, y=520,anchor='center')


    def on_closing():
        print("User clicked close button")
        window.destroy()
        root.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()


def file_transfer():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    scrn_share.place_forget()
    file_trans.place_forget()

    def back_press():
        label11.destroy()
        label22.destroy()
        label33.destroy()
        bck.destroy()
        send.destroy()
        rcv.destroy()

        global label1
        label1 = Label(root, text="Welcome to ShareNet!!", font=('Times New Roman', 20, 'bold'), bg="#f4fdfe")
        label1.place(relx=0.5, y=30, anchor='center')
        
        global scrn_image
        scrn_image = PhotoImage(file="Assets/screenshare.png")
        global scrn_share
        scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=other_share)
        scrn_share.place(relx=0.5,anchor='center', y=150)
        global label2
        label2 = Label(root, text="Audio & Video Share", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
        label2.place(relx=0.5,anchor='center', y=250)

        global file_image
        file_image = PhotoImage(file="Assets/fileshare.png")
        global file_trans
        file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
        file_trans.place(relx=0.5,anchor='center', y=350)
        global label3
        label3 = Label(root, text="File Transfer", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
        label3.place(relx=0.5,anchor='center', y=430)

    def Send():
        root.withdraw()
        window = Toplevel(root)
        window.title("Send File")
        window.geometry('450x560+500+200')
        window.configure(bg='#f4fdfe')
        window.resizable(False, False)

        def select_file():
            global filename
            global basename
            file = filedialog.askopenfile(initialdir=os.getcwd(), title='Select a File', filetypes=[('All Files', '*.*')])
            if file:
                filename = file.name
                basename = os.path.basename(filename)
                print("Exact file name:", basename)
                Label(window, text=f' {basename}', font=('Calibari', 13,), bg='#ffffff', fg="#000").place(relx=0.5,anchor='center', y=305)

        def sender():
            s = socket.socket()
            host = socket.gethostname()
            port = 8085
            s.bind((host, port))
            s.listen(1)
            print(host)
            print('waiting for any incoming connection.........')
            conn, addr = s.accept()
            conn.send(basename.encode())
            print(basename)
            seq_num = 0
            cwnd = 1
            ssthresh = 1024
            rtt = 1
            ack = conn.recv(1024).decode()
            if ack == 'OK':
                with open(filename, 'rb') as file:
                    window_size = 4  # set the window size to 4
                    packets = []
                    current_packet = 0
                    total_packets = (os.path.getsize(filename) // 1024) + 1
                    for i in range(total_packets):
                        file_data = file.read(1024)
                        packets.append(file_data)
                    conn.send(f"{total_packets}".encode())
                    print(basename)
                    ackk = conn.recv(1024).decode()
                    if ackk == "sz":
                        while current_packet < total_packets:
                            for i in range(total_packets):
                                conn.send(packets[i])
                                try:
                                    ack = conn.recv(1024).decode()
                                    if ack == "ACK":
                                        current_packet += 1
                                        if seq_num == len(file_data):
                                            # All packets have been acknowledged
                                            break
                                        if cwnd < ssthresh:
                                            cwnd *= 2
                                        else:
                                            cwnd += 1
                                    print(cwnd)
                                    # print(f"Packet {current_packet} acknowledged.")
                                except:
                                    ssthresh=max(cwnd/2,1)
                                    cwnd=1

                                    continue
                    else:
                        print('sz not rcvd')
                print(f" Total {current_packet} Packet acknowledged.")
                print("Data has been transmitted successfully...")
                send_btn.destroy()
                Label(window, text=f'Data has been transmitted successfully', font=('Calibari', 13,),bg='#ffffff', fg="#000").place(relx=0.5,anchor='center', y=350)

        def back_btn():
            window.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="Assets/sendbt.png")
        window.iconphoto(False, image_icon1)

        Sbackground = PhotoImage(file="Assets/bg_send.png")
        Label(window, image=Sbackground).place(x=-2, y=-2)

        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
        Label(window, text=f'Sender IP: {ip_address}', bg='#ffffff', fg="#000", font=('Caliabri',15)).place(relx=0.5,anchor='center', y=195)

        Button(window, text="Select File", width=20, height=1, font='arial 14 bold', bg='white', fg="black",relief='raised', command=select_file).place(relx=0.5,anchor='center', y=250)


        global send_btn
        imageicons = PhotoImage(file="Assets/sendarrow.png")
        send_btn = Button(window, text="Send", compound=LEFT, image=imageicons, 
                          width=280, font='caliabri 14 bold', bg='#ffffff', fg="#000",command=sender)
        send_btn.place(relx=0.5,anchor='center', y=350)
        
        sel_file = Entry(window, width=20, fg="black", border=4, bg='white', font=('caliabri', 15))
        sel_file.place(relx=0.5,anchor='center', y=300)
        sel_file.focus()
        sel_file.insert(0, "File Name...")

        
        Button(window, text="Back",font=('Calibari',15,'bold'),height=1, width=6, bg='#ffffff', activebackground='#ffffff', command=back_btn).place(relx=0.5, y=520,anchor='center')


        def on_closing():
            print("User clicked close button")
            window.destroy()
            root.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)

        window.mainloop()

    def Receive():
        root.withdraw()
        main = Toplevel(root)
        main.title("Receive")
        main.geometry('450x560+500+200')
        main.configure(bg='#f4fdfe')
        main.resizable(False, False)

        def receiver():
            ID = str(SenderID.get())

            s = socket.socket()
            port = 8085
            s.connect((ID, port))
            filename1 = s.recv(1024).decode()
            print(filename1)
            s.send("OK".encode())
            rcv = "receive/" + filename1
            sz = s.recv(1024).decode()
            print(sz)
            sz = int(sz)
            s.send("sz".encode())
            with open(rcv, 'wb') as file:
                current_packet = 0
                while True:
                    if current_packet == sz:
                        break
                    try:
                        file_data = s.recv(1024)
                        if not file_data:
                            break
                        file.write(file_data)
                        s.send("ACK".encode()) 
                        current_packet += 1
                    except:
                        continue
            print(f"Total {current_packet} Packet  received.")
            print("file has been received successfully..")
            rr.destroy()
            Label(main, text=f'File has been received successfully.....', font=('Acumin Variable Concept', 13,),
                  bg='#7FFFD4', fg="#000").place(relx=0.5,anchor='center', y=360)

        def back_btn():
            main.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="Assets/rcvbt.png")
        main.iconphoto(False, image_icon1)
        
        Hbackground = PhotoImage(file="Assets/bg_send.png")
        Label(main, image=Hbackground).place(x=-2, y=-2)

        SenderID = Entry(main, width=20, fg="black", border=2, bg='white', font=('arial', 15))
        SenderID.place(relx=0.5,anchor='center', y=200)
        SenderID.focus()
        SenderID.insert(0, "Sender IP..")

       
        Button(main, text="Back",font=('Calibari',15,'bold'),height=1, width=6, bg='#ffffff', activebackground='#ffffff', command=back_btn).place(relx=0.5, y=520,anchor='center')


        imageicon = PhotoImage(file="Assets/rcvarrow.png")
        rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=280, bg='#ffffff', fg="#000",
                    font='arial 14 bold',
                    command=receiver)
        rr.place(relx=0.5,anchor='center', y=250)

        def on_closing():
            print("User clicked close button")
            main.destroy()
            root.destroy()

        main.protocol("WM_DELETE_WINDOW", on_closing)

        main.mainloop()

    global label11
    label11 = Label(root, text="File transfer", font=('Calibari', 20, 'bold'), bg="#f4fdfe")
    label11.place(relx=0.5,anchor='center', y=30)

    send_image = PhotoImage(file="Assets/sendbt.png")
    send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
    send.place(x=50, y=100)
    global label22
    label22 = Label(root, text="Send", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
    label22.place(x=60, y=220)

    rcv_image = PhotoImage(file="Assets/rcvbt.png")
    rcv = Button(root, image=rcv_image, bg="#f4fdfe", bd=0, command=Receive)
    rcv.place(x=300, y=100)
    global label33
    label33 = Label(root, text="Receive", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
    label33.place(x=300, y=220)

    
    bck = Button(root,text="Back",font=('Calibari', 15, 'bold'), bg="#ffffff", bd=0, command=back_press)
    bck.place(relx=0.5,anchor='center', y=350)
    
    root.mainloop()



image_icon = PhotoImage(file="Assets/Share.png")
root.iconphoto(False, image_icon)

global label1
label1 = Label(root, text="Welcome to ShareNet!!", font=('Times New Roman', 20, 'bold'), bg="#f4fdfe")
label1.place(relx=0.5,anchor='center', y=30)


global scrn_image
scrn_image = PhotoImage(file="Assets/screenshare.png")
global scrn_share
scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=other_share)
scrn_share.place(relx=0.5,anchor='center', y=150)
global label2
label2 = Label(root, text="Audio & Video Share", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
label2.place(relx=0.5,anchor='center', y=250)

global file_image
file_image = PhotoImage(file="Assets/fileshare.png")
global file_trans
file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
file_trans.place(relx=0.5,anchor='center', y=350)
global label3
label3 = Label(root, text="File Transfer", font=('Calibari', 17, 'bold'), bg="#f4fdfe")
label3.place(relx=0.5,anchor='center', y=430)


def on_closing():
    print("User clicked close button")
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
