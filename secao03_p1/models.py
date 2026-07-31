from pydantic import BaseModel, validator, ValidationError

class Curso(BaseModel):
    id: int|None
    titulo: str
    aulas: int # mais de 12
    horas: int # mais de 10

    @validator('aulas')
    def validar_aulas(cls, value):
        value_min = 12
        if int(value) <= value_min:
            raise ValueError(f'O número de aulas deve ser maior que {value_min}.')
    
        return value
    
    @validator('horas')
    def validar_horas(cls, value):
        value_min = 10
        if int(value) <= value_min:
            raise ValueError(f'O número de aulas deve ser maior que {value_min}.')
    
        return value

    @validator('titulo')
    def validar_titulo(cls, value):
        if len(value.split(' ')) < 3:
            raise ValueError(f'Título deve ter ao menos 3 palavras.')
        
        return value


cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algorítimos e Lógica de Programaçã', aulas=52, horas=56)
    ]