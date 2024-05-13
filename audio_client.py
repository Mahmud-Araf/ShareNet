# client.py
import pyaudio
import socket


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

global is_recording
is_recording = True



def share_audio_client(ip,port):
     
    global is_recording
    is_recording = True

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while is_recording:
            data = stream.read(CHUNK)
            udp.sendto(data, (ip, port))
    except KeyboardInterrupt:
        pass

    udp.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

def close_audio_client():
    global is_recording
    is_recording = False



