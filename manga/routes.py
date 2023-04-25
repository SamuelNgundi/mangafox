from fastapi import APIRouter
from .schema import CreateManga


mangarouter = APIRouter()


@mangarouter.post('/add')
def add_manga(manga: CreateManga):
    return manga

@mangarouter.get('/{accr}')
def read_manga():
    return 'This is a GET route'

@mangarouter.post('/{accr}/update')
def update_manga():
    pass

@mangarouter.post('/{accr}/delete')
def delete_manga():
    pass

@mangarouter.post('/{accr}/rate')
def rate_manga():
    pass