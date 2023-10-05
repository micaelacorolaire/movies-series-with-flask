from sqlalchemy import Column,INTEGER,String,ForeignKey,Httpurl,UUID4
from models.base import BaseModel
from sqlalchemy import relationship 

class movies(BaseModel):
    __tablename__='movies'
    __args__={'schema':'public'}
    id_movies=Column(int,primary_key=True,null=False)
    title=Column(str,null=False)
    movies_director=Column(str,null=False)
    actors=Column(str,null=False)
    kind_of_movies=Column(str,null=False)
    qualification=Column(int,null=False)
    release_year=Column(int,null=False)
    