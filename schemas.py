from pydantic import BaseModel
from typing import List, Optional

class TopProduct(BaseModel):
    product: str
    mentions: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class SearchMessage(BaseModel):
    message_id: int
    channel_name: str
    message: str
    date: str
