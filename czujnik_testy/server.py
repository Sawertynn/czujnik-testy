from datetime import datetime
import os

from fastapi import FastAPI, Request
import uvicorn

SECRETS_DIR = "./secrets"
KEYFILE = f"{SECRETS_DIR}/key.pem"
CERTFILE = f"{SECRETS_DIR}/cert.pem"

SAVE_FILE = "savefile.txt"

PORT = 8000

app = FastAPI()


@app.get("/")
async def send_data(request: Request):
    try:
        with open(SAVE_FILE, "r") as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        return "nothing saved for now"


@app.post("/")
async def receive_data(request: Request):
    data = await request.body()
    timestamp = datetime.now().isoformat()

    text = f"received at: {timestamp}, data: {data!r}"
    print(text)
    with open(SAVE_FILE, "a") as file:
        file.write(text + "\n")
    return {"received_at": timestamp, "data": data}


if __name__ == "__main__":
    if not os.path.isfile(KEYFILE):
        os.system("sh create_key.sh")

    uvicorn.run(
        app, host="0.0.0.0", port=PORT, ssl_keyfile=KEYFILE, ssl_certfile=CERTFILE
    )
