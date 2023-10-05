from pydantic import BaseModel,Field,UUID4

class series(BaseModel):
    id_series:UUID4=Field(min_length=1,null=False) #me pierdo aca,como lo completo?.
    title:str=Field(min_length=2,max_length=50,null=False)
    serie_director:str=Field(min_length=2,max_length=100)
    actors:str=Field(max_length=1000,null=False)
    kind_of_serie:str=Field(max_length=100,null=False)
    qualification:int=Field(ge=1,le=10,null=False)
    release_year:int=Field(ge=1928,null=False)
    seasons:int=Field(ge=1,null=False)
    episodies:int=Field(ge=1,le=25,null=False)