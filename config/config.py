import os
import pymongo
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")


class Settings:
    """creating environmental variables"""
    TITLE: str = "SCMXpertLite"
    DESCRIPTION: str = """SCMXpertLite  created in FastAPI"""
    PROJECT_VERSION: str = "1.0.0"
    MONGODB_USER = os.getenv("mongodb_user")
    MONGODB_PASSWORD = os.getenv("mongodb_password")
    CLIENT = pymongo.MongoClient(os.getenv("mongouri"))
    database = CLIENT[os.getenv("DB_NAME")]
    collection1=database['shipment_collection']
    collection2=database["user_details"]
    collection3=database['datastream']
    SECRET_KEY: str = "mysecretkey"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30 # in mins
    COOKIE_NAME = "access_token"
    HOST = (os.getenv("HOST"))
    PORT = (os.getenv("PORT"))

setting=Settings()