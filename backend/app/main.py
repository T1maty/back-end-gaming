import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import db

origins= [
    "http://localhost:3000"
]

def init_app():
    db.init()

    app = FastAPI(
        title = "Back-end Gaming",
        description = "Login",
        version = "1"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()
    
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    return app