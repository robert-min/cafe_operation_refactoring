from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from libs.exception import CustomHttpException


def error_handlers(app):
    @app.exception_handler(CustomHttpException)
    async def http_custom_exception_handler(request: Request, exc: CustomHttpException):
        content = {
            "meta": {
                "code": exc.code,
                "error": str(exc.error),
                "message": exc.message if exc.message else str(exc.error)
            },
            "data": None
        }
        return JSONResponse(
            status_code=exc.code,
            content=content
        )
