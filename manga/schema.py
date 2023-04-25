from pydantic import BaseModel, Field
from app.constants import Settings as S
from datetime import datetime


class CreateManga(BaseModel):
    title: str = Field(..., max_length=S.MAX_CHARACTERS)
    published: datetime
    author: str = Field(..., max_length=S.MAX_CHARACTERS)
    genre: str = Field('', max_length=S.MAX_CHARACTERS)
    summary: str = Field('', max_length=S.MAX_CHARACTERS)
    rating: float = Field(0, ge=0, le=5)
    is_ongoing: bool = Field(False)
    publisher: str = Field('', max_length=S.MAX_CHARACTERS)
    translations: list = Field(None)
    comments: list = Field(None)
    updated_at: datetime = Field(None)
    has_anime: bool = Field(False)
    chapters: int = Field(..., ge=4)
    wiki: str = Field('', max_length=S.MAX_CHARACTERS)
    
    
    