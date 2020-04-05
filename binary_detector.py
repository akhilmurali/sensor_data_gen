import socket
import time
import random
import sys


def start_socket(threshold):
    if len(sys.argv) < 5:
        print("Format: <host> <port> <device-id> <floor>", sys.argv[0])
        exit(-1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    DEVICE_ID = sys.argv[3]
    FLOOR = sys.argv[4]
    LIMIT = threshold
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
                        trigger = random.random() > LIMIT
                        # time in milliseconds
                        data = "{},{},{},{}".format(int(time.time()) * 1000, DEVICE_ID, FLOOR, trigger)
                        # data = "{},{},{},{}".format(datetime.now(), DEVICE_ID, REGION, smoke)
                        print(data)
                        conn.sendall("{}\n".format(data).encode('utf-8'))
                        time.sleep(1)
                    except Exception as e:
                        print(e)
                        break
