import fastapi
import uvicorn


app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message" : "Hello world"
    }

if __name__ = '__main__':
    uvicorn.run(app)

# By <https://www.youtube.com/watch?v=qQNGw_m8t0Y>