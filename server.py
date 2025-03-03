from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.body()
    timestamp = datetime.now().isoformat()
    
    text = f"received at: {timestamp}, data: {data}"
    print(text)
    return {"received_at": timestamp, "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
