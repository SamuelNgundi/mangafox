from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from manga.routes import mangarouter


def get_app() -> FastAPI:
    _app = FastAPI()
    
    # Use our custom route
    _app.include_router(mangarouter, prefix='/manga')
    
    # Static files
    _app.mount('/static', StaticFiles(directory='static'), name='static')

    return _app


app = get_app()


@app.get('/anime', response_class=HTMLResponse)
def anime():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Anime Site</title>
</head>
<body>

    <h1>Welcome to my anime site</h1>

</body>
</html>
"""



templates = Jinja2Templates(directory='templates')

@app.get('/animeonlybetter')
def anime2(request: Request):
    context = {
        'request': request,
        'username': 'helloworldGuy',
        'country': 'Philippines',
        'year': 2023,
    }
    return templates.TemplateResponse('anime.jinja2', context)

@app.get('/page2')
def page2(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('page2.jinja2', context)


