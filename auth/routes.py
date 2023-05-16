from typing import Annotated
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from icecream import ic

from .schema import UserFavColor


data = {}

authrouter = APIRouter()
templates = Jinja2Templates(directory='templates')


@authrouter.get('/favcolor')
async def form_favcolor(request: Request):
    ic(data)
    context = {
        'request': request,
        'usernameerror': '',
        'passworderror': '',
    }
    return templates.TemplateResponse('auth/form.jinja2', context)


@authrouter.post('/favcolor')
async def set_favcolor(request: Request, username: Annotated[str, Form()],
                       favcolor: Annotated[str, Form()]):
    data[username] = favcolor
    context = {
        'request': request,
        'favcolor': favcolor,
        'username': username,
        'title': 'Thank You',
    }
    return templates.TemplateResponse('auth/success.jinja2', context)
