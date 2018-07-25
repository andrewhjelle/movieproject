# Run this file to launch the movies page
import media
import fresh_tomatoes

#Credits for movie posters: https://goo.gl/yrsNZS and https://goo.gl/Hj4MKJ 
pulp_fiction = media.Movie("Pulp Fiction", "1994", "You won't know the facts until you've seen the fiction",
                           "https://goo.gl/bptpW7", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
robocop = media.Movie("Robocop", "1987", "Robot cop takes on Detroit crime", 
                      "https://goo.gl/FzNCF4", "https://www.youtube.com/watch?v=zbCbwP6ibR4")
re_animator = media.Movie("Re-Animator", "1985", "Watch science come alive",
                          "https://goo.gl/aYnZvA", "https://www.youtube.com/watch?v=6NOcRIHiRtc")
back_to_the_future  = media.Movie("Back to the Future", "1985", "A boy travels back in time to the 1950s",
                                  "https://goo.gl/hwRe3i", "https://www.youtube.com/watch?v=qvsgGtivCgs")
dawn_of_the_dead = media.Movie("Dawn of the Dead", "1979", "The dead walk the earth, watch out!", 
                               "https://goo.gl/GRYJP4", "https://www.youtube.com/watch?v=j69OPw9nFHw")
let_me_in = media.Movie("Let Me In", "2010", "Innocence Dies. Abby Doesn't.", 
                        "https://goo.gl/1A6UaC", "https://www.youtube.com/watch?v=reRRAEVHq8E")
a_nightmare_on_elm_street = media.Movie("A Nightmare on Elm Street", "1984", "A fight to the death with Freddy",
                                        "https://goo.gl/AVXuCG", "https://www.youtube.com/watch?v=dCVh4lBfW-c")
on_the_waterfront = media.Movie("On The Waterfront", "1954", "One man on a hunt for justice",
                                "https://goo.gl/JvdzTC", "https://www.youtube.com/watch?v=QOLHbQjtSFs")
there_will_be_blood = media.Movie("There Will Be Blood", "2007", "Dad and son search for oil in the west", 
                                  "https://goo.gl/yk64BW", "https://www.youtube.com/watch?v=OjZ1rUQQKxY")
the_goonies = media.Movie("The Goonies", "1985", "Never say die",
                          "https://goo.gl/5Z6bsd", "https://www.youtube.com/watch?v=hJ2j4oWdQtU")
drag_me_to_hell = media.Movie("Drag Me to Hell", "2009", "Be careful with whom you deal",
                              "https://goo.gl/q4qp3G", "https://www.youtube.com/watch?v=BUZTybLlWKI")
rocky = media.Movie("Rocky", "1976", "A down and out boxer rises to the top",
                    "https://goo.gl/fnqNb3", "https://www.youtube.com/watch?v=7RYpJAUMo2M")

movies = [pulp_fiction, re_animator, back_to_the_future, robocop, let_me_in, rocky, dawn_of_the_dead,
          on_the_waterfront, the_goonies, there_will_be_blood, drag_me_to_hell, a_nightmare_on_elm_street]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__name__, media.Movie.__module__)

