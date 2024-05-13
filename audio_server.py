# server.py
import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
ip = socket.gethostname()
global is_recording
is_recording = True

def share_audio_server(port):

    
    global is_recording
    is_recording = True

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp.bind((ip, port))

    try:
        while is_recording:
            data, addr = udp.recvfrom(CHUNK * CHANNELS * 2)
            stream.write(data)
    except KeyboardInterrupt:
        pass

    
    udp.close()
    stream.stop_stream()
    stream.close()
    p.terminate()


def close_audio_server():
    global is_recording
    is_recording = False
