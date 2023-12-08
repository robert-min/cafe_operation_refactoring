from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.controller import auth
from libs.error_handlers import error_handlers
from libs.logging import set_logger

def create_app():
    app = FastAPI()
    app.include_router(auth)

    error_handlers(app)
    set_logger(app)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
