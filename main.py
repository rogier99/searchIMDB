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
            print("\n" + str(item))
            print(movie.get(item))

def title_search (keyword):
    # Get the list of movies and find moves with given keyword
    ia = imdb.Cinemagoer()
    movies = ia.search_movie(keyword)

    # Print the results
    for movie in movies:
        print(movie)

def director_search (director):
    # Get the list of directors that are similar to the given input
    ia = imdb.Cinemagoer()
    persons = ia.search_person(director)

    # For every person, print the movies they directed
    for person in persons:
        print("Looking for movies from: " + str(person))
        print(person.get('director'))

def get_year(movie):
    movie['year']

def year_search (year):
    ia = imdb.Cinemagoer()
    # Get the list of all the movies <= This part I cannot find anywhere, just get by id or keyword and executing ia.get_movie for every id will be really slow

    # For every movie, look at the year (preferably looking from right to left (most movies start with either 1 or 2, the last two digits are more "unique") )
    for i in range(0, reversed(len(movies) - 1)):
        if movies[i]['year'] != year:
            movies.pop(i)
            
    # Use sort the movies by ranking
    movies.sort(key=get_year)

    # Print the list
    for movie in movies:
        print(movie)



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
