import socket
import sys
import time
import random
import math
from datetime import datetime

def start_socket(mean, std, sensorType):
    if len(sys.argv) < 5:
        print(f"Format: <host> <port> <device-id> <floor> [<{sensorType}-mean>] [<{sensorType}-std>]", sys.argv[0])
        exit(-1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    DEVICE_ID = sys.argv[3]
    FLOOR = sys.argv[4]
    MEAN = sys.argv[5] if len(sys.argv) >= 6 else mean
    STD = sys.argv[6] if len(sys.argv) >= 7 else std

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
                        value = random.gauss(MEAN, STD)
                        # time in milliseconds
                        data = "{},{},{},{:.2f}".format(int(time.time()) * 1000, DEVICE_ID, FLOOR, value)
                        # data = "{},{},{},{:.2f}".format(datetime.now(), DEVICE_ID, REGION, temp)
                        print(data + "\n")
                        conn.sendall("{}\n".format(data).encode('utf-8'))
                        time.sleep(1)
                    except Exception as e:
                        print(e)
                        break