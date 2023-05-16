from pydantic import BaseModel


class UserFavColor(BaseModel):
    username: str
    color: str