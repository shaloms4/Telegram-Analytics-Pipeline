from fastapi import FastAPI, Query
from typing import List
import crud
import schemas

app = FastAPI(title="Telegram Medical Analytics API")

@app.get("/api/reports/top-products", response_model=List[schemas.TopProduct])
def top_products(limit: int = 10):
    return crud.get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def channel_activity(channel_name: str):
    return crud.get_channel_activity(channel_name)

@app.get("/api/search/messages", response_model=List[schemas.SearchMessage])
def search_messages(query: str = Query(..., min_length=1)):
    return crud.search_messages(query)
