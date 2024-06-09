import uvicorn
import requests
from utils import Utils
from loguru import logger
from sqliteconnector import SqliteConnector
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import UJSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from starlette_exporter import PrometheusMiddleware, handle_metrics



class Server:
    def __init__(self):
        self.connector = SqliteConnector()
        self.connector.create_tables()
        
        self.app = FastAPI(title="Find My Kids", description="Find your kids in photos sent in whatsapp and save it", version='1.0.0',  contact={"name": "Tomer Klein", "email": "tomer.klein@gmail.com", "url": "https://github.com/t0mer/my-kids"})
        self.app.mount("/dist", StaticFiles(directory="dist"), name="dist")
        self.app.mount("/plugins", StaticFiles(directory="plugins"), name="plugins")
        self.app.mount("/js", StaticFiles(directory="dist/js"), name="js")
        self.app.mount("/css", StaticFiles(directory="dist/css"), name="css")
        self.templates = Jinja2Templates(directory="templates/")
        self.app.add_middleware(PrometheusMiddleware)
        self.app.add_route("/metrics", handle_metrics)
        self.origins = ["*"]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )



        @self.app.get("/wizard")
        def home(request: Request):
            """
            Homepage
            """
            return self.templates.TemplateResponse('wizard.html', context={'request': request })
    
    
    
    
        
        
        
        
        
        
        
        
        
    
    def start(self):
        uvicorn.run(self.app, host="0.0.0.0", port=7020)