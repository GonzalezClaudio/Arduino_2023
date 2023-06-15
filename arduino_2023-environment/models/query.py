from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int
)

from .persona import Persona as PersonaModel
from .objects import Persona, Departamento, Sueldo
from .departamento import Departamento as DepartamentoModel
from .sueldo import Sueldo as SueldoModel
class Query(ObjectType):
    personas = List(lambda: Persona, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    departamentos = List(lambda: Departamento)
    departamento = Field(lambda: Departamento, id=Int())
    sueldos = List(lambda: Sueldo)
    sueldo = Field(lambda: Sueldo, id=Int()) 



    def resolve_personas(self, info, id=None, last_name=None, has_email=None, order_by_name=None):
        query = Persona.get_query(info=info)
        if id:
            query = query.filter(PersonaModel.id==id)
        if last_name:
            query = query.filter(PersonaModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PersonaModel.email != None)
            else:
                query = query.filter(PersonaModel.email == None)
        if order_by_name:
            query = query.order_by(PersonaModel.name)
        return query.all()
    
    def resolve_departamentos(self, info):
        query = Departamento.get_query(info=info)
        return query.all()
    
    def resolve_departamento(self, info, id):
        dpto = DepartamentoModel.query.get(id)
        return dpto
    
    def resolve_sueldos(self, info):
        query = Sueldo.get_query(info=info)
        return query.all()
    
    def resolve_sueldo(self, info, id):
        suel = SueldoModel.query.get(id)
        return suel
