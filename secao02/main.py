from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI na Geek University"}


if __name__ == '__main__':
    import uvicorn
    # ip:"0.0.0.0" qualquer pessoa pode acessar por está configurado 0.0.0.0
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
