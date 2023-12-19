from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzAzNTI1MjQzLCJpYXQiOjE3MDI5MjA0NDMsInN1YiI6IjIifQ.F0-FxWXdBIJIlGG1ukTUi1diFchKJ_1S2t0KBkUIlrM
Tipo: bearer

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzAzNjE0ODI0LCJpYXQiOjE3MDMwMTAwMjQsInN1YiI6IjMifQ.aPTMf1cSDLLJMTOOQ9LuJ4RBT1SuM6LT_HsseVQ-0Dw
"""
