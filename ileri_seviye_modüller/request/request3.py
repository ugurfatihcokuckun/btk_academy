import requests

class theMovieDb:
    
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "1f0cf1b1a40e4f15fce73f7da43a1575"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Exit\nSeçim: ")

    if secim == "2":
        break
    else:
        if secim == "1":
            movies =movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])