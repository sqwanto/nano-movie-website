import fresh_tomatoes
import media

# create instances of Movie class and specific instance variables
life_aquatic = media.Movie("The Life Aquatic",
                        "2004", 
                        "An eccentric oceanographer sets out to extra revenge on a mythical shark that ate his partner",
                        "Wes Anderson",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Lifeaquaticposter.jpg/220px-Lifeaquaticposter.jpg",
                        "https://www.youtube.com/watch?v=yh401Rmkq0o")

fear_and_loathing = media.Movie("Fear and Loathing in Las Vegas",
                    "1998", 
                     "An oddball journalist and his psychopathic lawyer travel to Las Vegas for a series of psychedelic escapades",
                    "Terry Gilliam", 
                     "http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/FandlinLV.jpg/256px-FandlinLV.jpg",
                     "https://www.youtube.com/watch?v=_d0hEzXrWT4")

rushmore = media.Movie("Rushmore",
                       "1998", 
                       "The extracurricular king of Rushmore preparatory school is put on academic probation",
                        "Wes Anderson", 
                       "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/Rushmoreposter.png/220px-Rushmoreposter.png",
                       "https://www.youtube.com/watch?v=GxCNDpvGyss")

lost_in_translation = media.Movie("Lost in Translation",
                                  "2003", 
                                  "A faded movie star and a neglected young woman form an unlikely bond after crossing paths in Tokyo",
                                  "Sofia Coppola",
                                  "http://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Lost_in_Translation_poster.jpg/220px-Lost_in_Translation_poster.jpg",
                                  "https://www.youtube.com/watch?v=6wXjObmziEk")

blade_runner = media.Movie("Blade Runner",
                            "1982",
                           "A blade runner must pursue and try to terminate four replicants who have returned to Earth to find their creator",
                            "Ridley Scott", 
                           "http://upload.wikimedia.org/wikipedia/en/thumb/5/53/Blade_Runner_poster.jpg/220px-Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=KPcZHjKJBnE")

grand_budapest = media.Movie("The Grand Budapest Hotel",
                             "2014",
                             "A legendary concierge teams up with one of his employees to prove his innocence after he is framed for murder",
                            "Wes Anderson", 
                             "http://upload.wikimedia.org/wikipedia/en/thumb/a/a6/The_Grand_Budapest_Hotel_Poster.jpg/220px-The_Grand_Budapest_Hotel_Poster.jpg",
                             "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

#create list of movies to pass to open_movies_page function                       
movies = [rushmore, life_aquatic, fear_and_loathing, lost_in_translation, blade_runner, grand_budapest]

#call open_movies_page function with list of Movie instances
fresh_tomatoes.open_movies_page(movies)
