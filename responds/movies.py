from pydantic import BaseModel,Field,UUID4

class movies(BaseModel):
    id_movies:UUID4=Field(min_length=1,null=False)
    title:str=Field(min_length=2,max_length=50,null=False)
    movies_director:str=Field(min_length=2,max_length=50)
    actors:str=Field(max_length=1000,null=False)
    kind_of_movies:str=Field(max_length=50,null=False)
    qualification:int=Field(ge=1,le=10,null=False)
    release_year:int=Field(ge=1994,le=2050,null=False)
    