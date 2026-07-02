from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        'titulo': 'Programação em Python',
        'aulas': 112,
        'horas': 58
    },
    2: {
        'titulo': 'Programação em Java',
        'aulas': 80,
        'horas': 40
    }
}


if __name__ ==  '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, debug=True)