import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import asyncio

from typing import Optional
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from image import get_text_vector
from database import insert_image, search_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或者你可以指定允许的域名列表
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/images/add")
async def add_images(data: Request):
    params = await data.json()

    asyncio.create_task(insert_image(params['dir']))
    
    return True

@app.get("/images/search")
async def search_images(keyword: Optional[str] = ""):
   print(keyword)

   return search_image([get_text_vector(keyword)])

@app.get("/images")
async def get_image_path(path: Optional[str] = ""):
   print(path)
   return FileResponse(path)