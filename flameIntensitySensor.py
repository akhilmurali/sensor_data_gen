"""

OUTPUT FORMAT:
<time>,<device-id>,<region>,<temp-value>

"""

import socket
import sys
import time
import random
import math
from datetime import datetime

if len(sys.argv) < 5:
    print("Format: <host> <port> <device-id> <region> [<flame-intensity-mean>] [<flame-intensity-std>]", sys.argv[0])
    exit(-1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
DEVICE_ID = sys.argv[3]
REGION = sys.argv[4]
FLAME_INTENSITY_MEAN = sys.argv[5] if len(sys.argv) >= 6 else 27
FLAME_INTENSITY_STD = sys.argv[6] if len(sys.argv) >= 7 else 30

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print("Connected to: {}".format(addr))
        with conn:
            while True:
                try:
                    temp = random.gauss(FLAME_INTENSITY_MEAN, FLAME_INTENSITY_STD)
                    # time in milliseconds
                    data = "{},{},{},{:.2f}".format(int(time.time()) * 1000, DEVICE_ID, REGION, temp)
                    # data = "{},{},{},{:.2f}".format(datetime.now(), DEVICE_ID, REGION, temp)
                    print(data+"\n")
                    conn.sendall("{}\n".format(data).encode('utf-8'))
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    break
