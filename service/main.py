import fastapi
import uvicorn
import models.movie_model.py
import movie_data

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message" : "Hello world"
    }

@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    
    return movie.dict()


if __name__ == '__main__':
    uvicorn.run(app)

# By <https://www.youtube.com/watch?v=qQNGw_m8t0Y>