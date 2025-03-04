import socket
from datetime import datetime


UDP_PORT = 9999
BUFSIZE = 1024
HOST = "0.0.0.0"
SAVEFILE = "./savefile.txt"


def udp_server(host: str, port: int):
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind((host, port))

    print(f"Listening for UDP on {host}:{port}")

    try:
        while True:
            data, addr = udp_sock.recvfrom(BUFSIZE)
            timestamp = datetime.now().isoformat()
            text = f"{timestamp} :: {data!r}"
            print(text)
            with open(SAVEFILE, "a") as file:
                file.write(text + '\n')
    except KeyboardInterrupt:
        print('\nclosing connection...')
        udp_sock.close()    


if __name__ == "__main__":
    udp_server(HOST, UDP_PORT)
