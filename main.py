from fastapi import FastAPI
from manga.routes import mangarouter


def get_app() -> FastAPI:
    _app = FastAPI()
    
    # Use our custom route
    _app.include_router(mangarouter, prefix='/manga')
    
    return _app


app = get_app()