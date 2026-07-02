from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def raiz():
    return {'msg': 'FastAPI funcionando!'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)