from pydantic import BaseModel


class datatype(BaseModel):
    query_related_pet_agent : bool
    reasoning:str