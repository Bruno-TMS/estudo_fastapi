from typing import Any

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Depends

from time import sleep
from models import Curso, cursos


def fake_db():
    try:
        print('Abrindo conexão com o Banco de Dados.')
        sleep(2)
        yield
    
    finally:
        print('Fechando conexão com o Banco de Dados')
        sleep(2)


app = FastAPI(
    title='Minha primeira API',
    version='0.0.1',
    description= 'Uma APi para estudo do FastAPi'
    )


@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia.', summary='Retorna todos os cursos.',response_model= list[Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}', description='Retorna um curso pelo id informado.', summary='Get curso by id.', response_model=Curso)
async def get_curso(curso_id: int = Path(default=..., title='Id do curso', description='Deve ser entre 1 e 10', gt=0, lt=10), db: Any = Depends(fake_db)):
    for curso in cursos:
        if curso.id == curso_id:
            return curso
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Curso não encontrado"})
    


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    novo_id = len(cursos) + 1
   
    while any(novo_id == curso_registrado.id for curso_registrado in cursos):
        novo_id += 1

    curso.id = novo_id

    cursos.append(curso)

    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id : int, curso: Curso, db: Any = Depends(fake_db)):
    for curso_registrado in cursos:
        if curso_id == curso_registrado.id:
            curso_registrado.titulo = curso.titulo
            curso_registrado.aulas =  curso.aulas
            curso_registrado.horas = curso.horas
            
            return curso_registrado
        
    raise HTTPException(status_code=status.http_404, detail={"error": "Curso não encontrado"})


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id:int, db: Any = Depends(fake_db)):
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