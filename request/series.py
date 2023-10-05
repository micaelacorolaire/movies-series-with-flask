from pydantic import BaseModel,UUID4

class series(BaseModel):
    id_series=UUID4
    title=str
    serie_director=str
    actors=str
    kind_of_serie=str
    qualification=int
    release_year=int
    seasons=int
    episodies=int