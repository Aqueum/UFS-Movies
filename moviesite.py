import movies
import fresh_tomatoes

# instantiation of my three favourite movies:
shallow_grave = movies.Movie("Shallow Grave", "Bad housemates",
                             "https://upload.wikimedia.org/wikipedia/en/2/23/Shallow.jpg",
                             "https://www.youtube.com/watch?v=HbxNej_MJlw")

three_colours_blue = movies.Movie("Three Colours: Blue", "Post-tragic emotional liberty",
                                  "https://upload.wikimedia.org/wikipedia/en/2/2c/Bluevidcov.jpg",
                                  "https://www.youtube.com/watch?v=Hxu6my_t4pM")

casablanca = movies.Movie("Casablanca", "How to buy a pub",
                          "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
                          "https://www.youtube.com/watch?v=S9ID5DHsX8g")

# collection of my three favourite movie interfaces into movie_list
movie_list = [shallow_grave, three_colours_blue, casablanca]

# execution of the web page generator using my movie_list
fresh_tomatoes.open_movies_page(movie_list)
