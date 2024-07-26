import os

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

ROOT = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(ROOT, "templates"))

@app.get('/')
async def homepage(request: Request):
    """
    Simple homepage.
    """
    return templates.TemplateResponse("client_pyscript.html", {"request": request})

@app.get('/wasm/client_main.py')
async def wasm_python_code(request: Request):
    """
    Simple homepage.
    """
    return templates.TemplateResponse("client_main.py", {"request": request})

""" START
"""

db = { }  

# CREATE
@app.post('/membership_api/{key:str}')
async def do_POST(request: Request):
    print(">> do_POST() activated")

    content = await request.json()

    key = list(content.keys())[0]
    value = list(content.values())[0]

    global db
    if key in db :
        print(':: CREATE {}:{} rejected'.format(key, value))
        content = 'CREATE rejected'
    else:
        db[key] = value

        print(':: CREATE {}:{} created'.format(key, value))
        content = 'CREATE accpeted'

    return { content }

# READ
@app.get('/membership_api/{key:str}')
async def do_GET(request: Request):
    print(">> do_GET() activated")

    key = request.path_params["key"]    

    global db
    if key in db:
        print(':: READ {}:{} completed'.format(key, db[key]))
        content = 'READ accepted for < {} : {} >'.format(key, db[key])
    else:
        print(':: READ {} rejected'.format(key))
        content = 'READ rejected'

    return { content }


# UPDATE
@app.put('/membership_api/{key:str}')
async def do_PUT(request: Request):
    print(">> do_PUT() activated")

    content = await request.json()

    key = list(content.keys())[0]
    value = list(content.values())[0]

    global db
    if key in db :
        db[key] = value

        print(':: UPDATE {}:{} completed'.format(key, value))
        content = 'UPDATE completed'
    else:
        print(':: UPDATE {}:{} rejected'.format(key, value))
        content = 'UPDATE rejected'

    return { content }

# DELETE
@app.delete('/membership_api/{key:str}')
async def do_DELETE(request: Request):
    print(">> do_DELETE() activated")

    key = request.path_params["key"]    

    global db
    if key in db:
        del db[key]

        print(':: DELETE {} completed'.format(key))
        content = 'DELETE accepted'
    else:
        print(':: DELETE {} rejected'.format(key))
        content = 'DELETE rejected'

    return { content }