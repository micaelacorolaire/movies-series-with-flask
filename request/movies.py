from pydantic import BaseModel,UUID4

class movies(BaseModel):
    id_movies=UUID4
    title=str
    movies_director=str
    actors=str
    kind_of_movies=str
    qualification=int
    release_year=int
    