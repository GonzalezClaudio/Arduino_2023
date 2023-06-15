from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
    Persona
)
from .persona import Persona as PersonaModel


class createPersona(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    persona = Field(lambda: Persona)

    def mutate(self, info, name, last_name, email=None):
        persona = PersonaModel(name=name, last_name=last_name, email=email)

        db.session.add(persona)
        db.session.commit()

        return createPersona(persona=persona)

class updatePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            if email:
                persona.email = email
            if name:
                persona.name = name
            if last_name:
                persona.last_name = last_name
            db.session.add(persona)
            db.session.commit()

        return updatePersona(persona=persona)


class deletePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            db.session.delete(persona)
            db.session.commit()

        return deletePersona(persona=persona)

class Mutation(ObjectType):
    create_persona = createPersona.Field()
    update_persona = updatePersona.Field()
    delete_persona = deletePersona.Field()