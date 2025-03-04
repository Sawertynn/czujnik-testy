import asyncio
import socket
from fastapi import FastAPI, BackgroundTasks
from contextlib import asynccontextmanager

app = FastAPI()
udp_data = []  # Shared list to store received UDP data

UDP_PORT = 9999
HTTP_PORT = 8000
BUFSIZE = 1024


async def udp_server(host: str, port: int):
    loop = asyncio.get_running_loop()
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_sock.bind((host, port))
    # udp_sock.setblocking(False)

    print(f"Listening for UDP on {host}:{port}")

    while True:
        # data, addr = await loop.run_in_executor(None, udp_sock.recvfrom, BUFSIZE)
        data, addr = await loop.sock_recv(udp_sock, BUFSIZE)
        print('dupa')
        message = data.decode()
        print(f"Received from {addr}: {message}")
        udp_data.append({"address": addr, "message": message})


@asynccontextmanager
async def lifespan(app: FastAPI):
    udp_task = asyncio.create_task(udp_server("0.0.0.0", UDP_PORT))
    print('raz')
    yield  # Startup complete, FastAPI is now running
    print('dwa')
    udp_task.cancel()  # Cleanup when shutting down


app.router.lifespan_context = lifespan


@app.get("/data")
async def get_udp_data():
    return udp_data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=HTTP_PORT)
