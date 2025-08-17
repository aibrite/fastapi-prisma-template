from core.service import ServiceBase

class HomeService(ServiceBase):
    async def get_all_users(self):
        async with self.getDB() as db:
            data = await db.user.find_many()
        return data
    
    def __init__(self):
        pass