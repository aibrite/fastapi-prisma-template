from typing import Any, AsyncGenerator
from prisma import Prisma
from core.app import App
import core.config as config
from contextlib import asynccontextmanager

class ServiceBase:
    
    def __init__(self):
        app = self.app = App.get_instance()
        self.logger = app.logger;
        self.config = config
        
    @asynccontextmanager
    async def getDB(self):
        db = Prisma()
        try:
            await db.connect()
            yield db
        finally:
            await db.disconnect()
        