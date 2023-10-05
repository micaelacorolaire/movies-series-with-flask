from pydantic import BaseModel,UUID4,String,integer,Column 

class series(BaseModel):
    id_series=UUID4
    title=Column(str,null=False)
    serie_director=Column(str,null=False)
    actors=Column(str,null=False)
    kind_of_serie=Column(str,null=False)
    qualification=Column(int,null=False)
    release_year=Column(int,null=False)
    seasons=Column(int,null=False)
    episodies=Column(int,null=False)