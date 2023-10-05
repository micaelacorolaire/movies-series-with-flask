from flask import Flask

app=Flask(__name__)

@app.route('/movies',methods=['get'])
def get_movies():
    movies=db.session.query(movies).filter(movies.title).filter(movies.title==movies.title.one_or_one)
    if movies.title is None:
        response=('error':f'the title of the movie{movies.title}dosent exists')
        return 404
@app.route('/movies/{id},methods=['delete']')  
def movies_delete(id:str) :
     movie = movie.query.get(id)

     if movie is None:
         response:{
             ('error':f'the movie was not deleted')
         }
        db.session.delete(movie)
        db.session.commit()
    
@app.route('/movies,methods=[post]')
def app_post():
    movie = movie.query.filter_by(title=movie).first()
    if movie in movie ==True:
        print(r'the movie exists yet') 
    else:
        print(r'the movie has been added to this app')
    db.session.updated(movie.title)
    db.commit()
    
@app.route('/series,methods={get}')
def get_series():
    serie=serie.query.filter_by(id=serie).first()
    if serie in serie==False:
        print(r'the serie could not be found')
    else:
        print(r'the serie exist ')
        db.session.get(id_serie)
        db.commit()
        
@app.route('/serie/{id}',methods=['delete'])
def delete_id_series(id:str):
    serie=serie.query.filter_by(id_series=id).first()
    if serie:
        db.session.delete(serie)
        db.session.commit()
        response = {
            'message': f'the series with  {id} have deleted it.'
        }
        return 20
    else:
        response = {
            'error': f'La serie con ID {id} no existe.'
        }
        return  404
    
@app.route('/series/{id},methods=[post]')
def post_series(id:str):
    serie=series.query.filter_by(id_series=id).first()
    if serie:
        db.session.post(serie)
        db.commit()
    else:
        print(r' the serie with id {id}could not be updated')
        

if __name__=='__main__':
    app.run(debug=True)
    





    
    
    

    
    
    
         
         






