import logging
from fastapi import FastAPI

# TODO : Error logging 작업 필요
def set_logger(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        logger = logging.getLogger("uvicorn.access")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # console 
        stream_hander = logging.StreamHandler()
        stream_hander.setFormatter(formatter)
        logger.addHandler(stream_hander)

        # 파일 출력
        file_handler = logging.FileHandler('info.log', mode='w')
        logger.addHandler(file_handler)

    '''
    https://m.blog.naver.com/indy9052/221934084260
    @app.middleware("http")
    async def audit_log(request, call_next):
        response = await call_next(request)
        response_body = b''

        async for chunk in response.body_iterator:
            response_body += chunk

        if "response_body" in context:
            logging.info("Request Body : {}".format(context["request_body"]))

        logging.info("Response Body : {}".format(response_body))
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )

    app.add_middleware(
        ContextMiddleware
    )
    '''
