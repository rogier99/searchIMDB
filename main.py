from imdb import Cinemagoer, IMDbError


def movie_info(movie_id):
    # Get the list of movies and get our movie
    ia = Cinemagoer()
    try:
        int(movie_id)
    except ValueError:
        print("Not a valid movie id is provided.")
        return

    try:
        movie = ia.get_movie(movie_id)
    except IMDbError:
        print("Movie id " + movie_id + " could not be found.")
        return

    # Every movie consists of main, plot and synopsis
    # Go over every element and print the content of these lists
    for dic in movie.infoset2keys:
        for item in movie.infoset2keys[dic]:
            print("\n" + str(item))
            print(movie.get(item))


def title_search(keyword):
    # Get the list of movies and find moves with given keyword
    ia = Cinemagoer()

    try:
        movies = ia.search_movie(keyword)
    except IMDbError:
        print("The movie with keyword " + keyword + " in the title could not be found.")
        return

    # Print the results
    for movie in movies:
        print(movie)


def director_search(director):
    # Get the list of directors that are similar to the given input
    ia = Cinemagoer()

    try:
        persons = ia.search_person(director)
    except IMDbError:
        print("The person " + director + " could not be found.")
        return

    # For every person, print the movies they directed
    for person in persons:
        print("Looking for movies from: " + str(person))
        print(person.get('director'))


def get_ranking(movie):
    return movie['rating']


def year_search(year):
    ia = Cinemagoer()
    # Get the list of all the movies, as even the top_100 is empty we use 3 movies, 2 from 1909, one from 1921
    movies = [ia.get_movie('1000'), ia.get_movie('1001'), ia.get_movie('12345')]
    # For every movie, look at the year
    for i in reversed(range(0, len(movies))):
        if movies[i]['year'] != int(year):
            movies.pop(i)

    # Use sort the movies by ranking
    if len(movies) == 0:
        print("There are no movies of year " + str(year) + " found")
        return

    movies.sort(key=get_ranking)

    # Print the list
    print("Sorted list:")
    for movie in movies:
        print(movie)


def main():
    print("Options menu, for debugging only:")
    print("1. Get movie information from id.")
    print("2. Get movie titles from a keyword.")
    print("3. Get movies made by given director.")
    print("4. Get movies ordered by ranking in given year.")
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
