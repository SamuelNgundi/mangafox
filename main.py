from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from manga.routes import mangarouter


def get_app() -> FastAPI:
    _app = FastAPI()
    
    # Use our custom route
    _app.include_router(mangarouter, prefix='/manga')
    
    # Static files
    _app.mount('/templates/images', StaticFiles(directory='templates/images'), name='images')
    
    return _app


app = get_app()



@app.get('/basic', response_class=HTMLResponse)
def html_string():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Foo</title>
</head>
<body>

    <h1>Hello world</h1>
    <p>This is some html.</p>

</body>
</html>
"""


templates = Jinja2Templates(directory='templates')

@app.get('/better')
def html_jinja(request: Request):
    context = {
        'request': request,
        'title': 'Welcome to Jinjax',
    }
    return templates.TemplateResponse('better.jinja2', context)