import hashlib
from tkinter import *
from vidstream import *
import socket
import threading
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Quick Share!")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)
host = socket.gethostname()
local_ip_address = socket.gethostbyname(host)
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)


def screen_share():
    root.withdraw()
    window = Toplevel(root)
    window.title("Other Share")
    window.geometry('450x560+500+200')
    window.configure(bg='#f4fdfe')
    window.resizable(False, False)

    def video_btn():
        print("share your video")
        global camera_client
        camera_client = CameraClient(SenderID.get(), 7777)
        t3 = threading.Thread(target=camera_client.start_stream)
        t3.start()

    def back_btn():
        window.withdraw()
        root.deiconify()
        server.stop_server()
        receiver.stop_server()

    def connect_btn():
        print("connect button pressed")
        t1 = threading.Thread(target=server.start_server)
        t2 = threading.Thread(target=receiver.start_server)
        t1.start()
        t2.start()
        cnt_btn.destroy()
        Label(window, text=f'       Connected     ', font=('Acumin Variable Concept', 20, 'bold'),
              bg='#7FFFD4', fg="#000").place(
            x=110, y=310)

    def share_audio_btn():
        print("share your audio button pressed")
        global audio_sender
        audio_sender = AudioSender(SenderID.get(), 6666)
        t5 = threading.Thread(target=audio_sender.start_stream)
        t5.start()

    def cancel_audio_btn():
        print("cancel audio button pressed")
        audio_sender.stop_stream()
        window.protocol("WM_DELETE_WINDOW", on_closing)
        # server.stop_server()
        # receiver.stop_server()

    def cancel_video_btn():
        print("cancel video button pressed")
        camera_client.stop_stream()
        window.protocol("WM_DELETE_WINDOW", on_closing)

    # icon
    image_icon1 = PhotoImage(file="image/scrn_share.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="image/bg_send_450x560.png")
    Label(window, image=Sbackground).place(x=-2, y=-2)

    Mbackground = PhotoImage(file="image/sss_ui.png")
    Label(window, image=Mbackground).place(x=130, y=20)

    host = socket.gethostname()
    ip_address = socket.gethostbyname(host)
    Label(window, text=f'IP: {ip_address}', bg='#87CEEB', fg='#000').place(x=190, y=190)

    global cnt_btn
    cnt_btn = Button(window, text="connect", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
                     command=connect_btn)
    cnt_btn.place(x=110, y=310)

    SenderID = Entry(window, width=22, fg="black", border=4, bg='white', font=('arial', 15))
    SenderID.place(x=110, y=250)
    SenderID.focus()
    SenderID.insert(0, "IP Address")
    Button(window, text="Share Audio", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=share_audio_btn).place(x=110, y=370)
    cancel_image = PhotoImage(file="image/cancel_audio.png")
    Button(window, image=cancel_image, width=30, height=30, bg='#7FFFD4', fg="#000", command=cancel_audio_btn).place(
        x=380, y=370)
    cancel_video_img = PhotoImage(file="image/cancel_video.png")
    Button(window, text="Share Video", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=video_btn).place(x=110, y=430)
    Button(window, image=cancel_video_img, width=30, height=30, bg='#7FFFD4', fg="#000",
           command=cancel_video_btn).place(x=380, y=430)
    Button(window, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
           command=back_btn).place(x=110, y=490)

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

    # file_trans.destroy()
    # scrn_share.destroy()

    def back_press():
        label11.destroy()
        label22.destroy()
        label33.destroy()
        bck.destroy()

        global label1
        label1 = Label(root, text="Welcome!!", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
        label1.place(x=20, y=30)

        # Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

        global scrn_image
        scrn_image = PhotoImage(file="image/scrn_share.png")
        global scrn_share
        scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=screen_share)
        scrn_share.place(x=50, y=100)

        global file_image
        file_image = PhotoImage(file="image/file_transfer.png")
        global file_trans
        file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
        file_trans.place(x=300, y=100)
        global label2
        label2 = Label(root, text="Screen Share", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        label2.place(x=40, y=200)
        global label3
        label3 = Label(root, text="File Transfer", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        label3.place(x=280, y=200)

    # def catch_minimize(event):
    #     root.wm_state()
    #     print("window minimzed")

    def Send():
        root.withdraw()
        window = Toplevel(root)
        window.title("Send")
        window.geometry('450x560+500+200')
        window.configure(bg='#f4fdfe')
        window.resizable(False, False)

        def select_file():
            global filename
            global basename
            file = filedialog.askopenfile(initialdir=os.getcwd(), title='Select image File',
                                          filetypes=(('file type', '*.txt'), ('all files', '*.*')))
            if file:
                filename = file.name
                basename = os.path.basename(filename)
                print("Exact file name:", basename)
                Label(window, text=f' {basename}', font=('Acumin Variable Concept', 13,), bg='#7FFFD4',
                      fg="#000").place(x=114, y=305)

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
                                    # print(f"Packet {current_packet} acknowledged.")
                                except:
                                    ssthresh = max(cwnd / 2, 1)
                                    cwnd = 1
                                    continue
                    else:
                        print('sz not rcvd')
                print(f" Total {current_packet} Packet acknowledged.")
                print("Data has been transmitted successfully...")
                send_btn.destroy()
                Label(window, text=f'Data has been transmitted successfully...', font=('Acumin Variable Concept', 13,),
                      bg='#7FFFD4', fg="#000").place(
                    x=90, y=350)
        def back_btn():
            window.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="image/send_fin.png")
        window.iconphoto(False, image_icon1)

        Sbackground = PhotoImage(file="image/bg_send_450x560.png")
        Label(window, image=Sbackground).place(x=-2, y=-2)

        Mbackground = PhotoImage(file="image/file_UI.png")
        Label(window, image=Mbackground, bg='#f4fdfe').place(x=130, y=20)

        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
        Label(window, text=f'IP: {ip_address}', bg='#7FFFD4', fg="#000", ).place(x=190, y=200)

        Button(window, text="+Select File", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=select_file).place(x=110, y=250)

        global send_btn
        send_btn = Button(window, text="Send", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
                          command=sender)
        send_btn.place(x=110, y=350)
        sel_file = Entry(window, width=22, fg="black", border=4, bg='#7FFFD4', font=('arial', 15))
        sel_file.place(x=110, y=300)
        sel_file.focus()
        sel_file.insert(0, "....")

        Button(window, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=back_btn).place(x=110, y=400)

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
            rcv = "RECEIVE\\" + filename1
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
                        s.send("ACK".encode())  # sending ACK for each packet received
                        current_packet += 1
                        # print(f"Packet {current_packet} received.")
                    except:
                        continue
            print(f"Total {current_packet} Packet  received.")
            print("file has been received successfully..")
            rr.destroy()
            Label(main, text=f'File has been received successfully.....', font=('Acumin Variable Concept', 13,),
                  bg='#7FFFD4', fg="#000").place(x=90, y=360)

        def back_btn():
            main.withdraw()
            root.deiconify()

        # icon
        image_icon1 = PhotoImage(file="image/rcv_fin.png")
        main.iconphoto(False, image_icon1)
        Hbackground = PhotoImage(file="image/bg_send_450x560.png")
        Label(main, image=Hbackground).place(x=-2, y=-2)

        Mbackground = PhotoImage(file="image/file_UI.png")
        Label(main, image=Mbackground, bg='#f4fdfe').place(x=130, y=40)

        # Label(main, text="Input Sender IP", font=('arial', 10, 'bold'), bg='#7FFFD4', fg="#000",).place(x=110, y=250)
        SenderID = Entry(main, width=22, fg="black", border=2, bg='white', font=('arial', 15))
        SenderID.place(x=110, y=300)
        SenderID.focus()
        SenderID.insert(0, "Sender IP..")

        Button(main, text="Back", width=20, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
               command=back_btn).place(x=110, y=420)

        imageicon = PhotoImage(file="image/arrow-removebg-preview_30x30.png")
        rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=240, bg='#7FFFD4', fg="#000",
                    font='arial 14 bold',
                    command=receiver)
        rr.place(x=110, y=350)

        def on_closing():
            print("User clicked close button")
            main.destroy()
            root.destroy()

        main.protocol("WM_DELETE_WINDOW", on_closing)

        main.mainloop()

    global label11
    label11 = Label(root, text="File transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
    label11.place(x=20,
                  y=30)

    Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

    send_image = PhotoImage(file="image/send_fin.png")
    send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
    send.place(x=50, y=100)

    rcv_image = PhotoImage(file="image/rcv_fin.png")
    rcv = Button(root, image=rcv_image, bg="#f4fdfe", bd=0, command=Receive)
    rcv.place(x=300, y=100)

    global label22
    label22 = Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
    label22.place(x=60, y=200)

    global label33
    label33 = Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
    label33.place(x=300, y=200)

    bck = Button(root, text="Back", width=10, height=1, font='arial 14 bold', bg='#7FFFD4', fg="#000",
                 command=back_press)
    bck.place(x=150, y=500)
    root.mainloop()


# icon
image_icon = PhotoImage(file="image/Neon Blue and Black Gamer Badge Logo (1).png")
root.iconphoto(False, image_icon)
global label1
label1 = Label(root, text="Welcome!!", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe")
label1.place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6", bd=0).place(x=25, y=80)

global scrn_image
scrn_image = PhotoImage(file="image/scrn_share.png")
global scrn_share
scrn_share = Button(root, image=scrn_image, bg="#f4fdfe", bd=0, command=screen_share)
scrn_share.place(x=50, y=100)

global file_image
file_image = PhotoImage(file="image/file_transfer.png")
global file_trans
file_trans = Button(root, image=file_image, bg="#f4fdfe", bd=0, command=file_transfer)
file_trans.place(x=300, y=100)
global label2
label2 = Label(root, text="Other Share", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
label2.place(x=40, y=200)
global label3
label3 = Label(root, text="File Transfer", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
label3.place(x=280, y=200)

background = PhotoImage(file="image/background.png")
Label(root, image=background).place(x=-2, y=280)


def on_closing():
    print("User clicked close button")
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

# root.bind("<Unmap>", catch_minimize)

root.mainloop()
