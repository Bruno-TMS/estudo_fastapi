from fastapi import FastAPI, HTTPException, status

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


@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso_by_id(curso_id: int):
    try:
        return cursos[curso_id]
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Curso não encontrado"})


if __name__ ==  '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, debug=True, reload=True)