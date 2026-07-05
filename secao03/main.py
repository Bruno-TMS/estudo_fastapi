from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query


from models import Curso


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
async def get_curso(curso_id: int = Path(default=None, title='Id do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        return cursos[curso_id]
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Curso não encontrado"})


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        next_id = len(cursos) + 1
        cursos[next_id] = curso
        del curso.id
        return curso
    
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com id {curso.id}.')


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id : int, curso: Curso):
    if curso_id not in cursos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso id {curso_id}')
    
    cursos[curso_id] = curso
    del curso.id

    return curso


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id:int):
    try:
        cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=F'não existe id de curso {curso_id}')


@app.get('/calculadora')
async def get_calculadora(a:int = Query(default=None, gt=5), b:int = Query(default=None, lt=10), c: int | None = Query(default=None, gt=100)):
    soma = a + b

    if c:
        soma = soma + c
    
    return {'soma': soma}


if __name__ ==  '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, debug=True, reload=True)