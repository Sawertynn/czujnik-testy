from fastapi import FastAPI, Request
from datetime import datetime

SECRETS_DIR = './secrets'

KEYFILE = f'{SECRETS_DIR}/key.pem'
CERTFILE = f'{SECRETS_DIR}/cert.pem'

app = FastAPI()

@app.get("/test")
async def webpage(request: Request):
    return "nothing here for now"

@app.post("/test")
async def receive_data(request: Request):
    data = await request.body()
    timestamp = datetime.now().isoformat()
    
    text = f"received at: {timestamp}, data: {data!r}"
    print(text)
    return {"received_at": timestamp, "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile=KEYFILE, ssl_certfile=CERTFILE)
