from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from settings import settings

async def get_async_mongo_client():
    mongo_client = AsyncIOMotorClient(settings.MONGO_URL, server_api=ServerApi('1'))
    try:
        yield mongo_client
    finally:
        mongo_client.close()

async def get_mongo_db(async_mongo_client=Depends(get_async_mongo_client)):
    yield async_mongo_client.get_database()