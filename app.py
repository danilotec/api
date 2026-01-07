from fastapi import FastAPI
from firrmware_routes import firmware

app = FastAPI()

@app.get('/')
async def home():
    return {'message': 'home page'}


app.include_router(firmware)