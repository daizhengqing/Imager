import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import asyncio

from typing import Optional
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from database.manager import insert_image, search_image
from utils.image import get_text_vector
from utils.choose_directory import choose_directory
from utils.configure import read_config, write_config

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
    return True

@app.post("/images/add")
async def add_images():
    dir = choose_directory()

    config = read_config()

    if (not dir in config['dirs']):
        print('???')

        config['dirs'].append(dir)

        write_config(config)

        asyncio.create_task(insert_image(dir))
    
    return True

@app.get("/images/search")
async def search_images(keyword: Optional[str] = ""):
   print(keyword)

   return search_image([get_text_vector(keyword)])

@app.get("/images")
async def get_image_path(path: Optional[str] = ""):
   print(path)
   return FileResponse(path)