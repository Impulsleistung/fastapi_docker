import httpx

def get_movie(title_subtext: str):
    url = 'https://movieservice.talkpython.fm/api/search/{title_subtext}'

    with httpx