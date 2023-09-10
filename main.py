import imdb
from imdb import Cinemagoer


def movie_info (movie_id):
    # Get the list of movies and get our movie
    ia = imdb.Cinemagoer()
    movie = ia.get_movie(movie_id)
    # Every movie consists of main, plot and synopsis
    # Go over every element and print the content of these lists
    for dic in movie.infoset2keys:
        for item in movie.infoset2keys[dic]:
            print(item)
            print(movie.get(item))

def title_search (keyword):
    ia = imdb.Cinemagoer()
    print(type(ia))

def director_search (director):
    return

def year_search (year):
    return

def main():
    print("Options menu, for debugging only:")
    print("1. Get movie information from id.")
    print("2. Get movie titles from a keyword.")
    print("3. Get movies made by given director.")
    print("4. Get movies orderd by ranking in given year.")
    option = input()
    if option == '1':
        print("Give movie id.")
        movie_id = input()
        movie_info(movie_id)
    
    if option == '2':
        print("Give keyword.")
        keyword = input()
        title_search(keyword)
        
    if option == '3':
        print("Give director.")
        director = input()
        director_search(director)
    
    if option == '4':
        print("Give year.")
        year = input()
        year_search(year)

if __name__ == "__main__":
    main()