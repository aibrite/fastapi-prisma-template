from ast import arg
from pyclbr import Function
from sys import prefix
from fastapi import FastAPI, Body, APIRouter
from fastapi_versioning import VersionedFastAPI
import uvicorn
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles
from core.config import APP_ENV, LOG_LEVEL, APP_PORT, APP_PATH
from core.util import import_source
from core.logger import configure_logging
from prisma import Prisma
from chainlit.utils import mount_chainlit

class App(FastAPI):
    __app_instance = None
    
    def getDB():
        return Prisma()
    
    def __init__(self, *args, **kwargs):
        if (App.__app_instance is not None):
            raise Exception("App instance already exists")
        App.__app_instance = self
        self.logger = configure_logging(LOG_LEVEL.upper())
        super().__init__(title="LabGPT Api",
                         version="metadata.version(api)",
                         openapi_url="/api/openapi.json",
                         *args,
                         **kwargs
                         )        
        # self.mount(
        #     "/public",
        #     StaticFiles(directory=f"{APP_PATH}/public"),
        #     name="static"
        # )
        import_source(src=APP_PATH, pattern="router.py", star_import=True) 
        
    @staticmethod
    def get_instance():
        return App.__app_instance
    
    @staticmethod
    def start():
        uvicorn.run(app="core.app:create_app",
                factory=True,
                reload=APP_ENV == "dev",
                port= APP_PORT ,
                log_level=LOG_LEVEL)
        return App.get_instance()
    
    def create_router(self, *args, **kwargs):
        router = APIRouter(*args, **kwargs)
        self.include_router(router)
        return router


def create_app() -> FastAPI:
    app = App();
    v_app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}') 
    mount_chainlit(app=v_app, target="chainlit_app.py", path="/chat")
    return v_app