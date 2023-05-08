from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise



DATABASE_URL = 'sqlite:///./mangafox.db'
DATABASE_MODELS = [
    'aerich.models',
]
TORTOISE_ORM = {
    'connections': {
        'default': DATABASE_URL
    },
    'apps': {
        'models': {
            'models': DATABASE_MODELS,
            'default_connection': 'default'
        }
    },
    'timezone': 'UTC',
    'use_tz': True,
    'echo': True,
}


def register_db(app: FastAPI) -> None:
    d = dict(config=TORTOISE_ORM)
    d['add_exception_handlers'] = True
    
    register_tortoise(app, **d)