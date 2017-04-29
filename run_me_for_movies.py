# Run this file to launch the movies page
import media
import fresh_tomatoes

#Credits for movie posters: http://unrealitymag.com/movies/a-collection-of-cool-stylized-movie-posters/ and http://geektyrant.com/news/2012/4/20/insanely-cool-series-of-stylized-poster-art-for-classic-genr.html 
pulp_fiction = media.Movie("Pulp Fiction", "1994", "You won't know the facts until you've seen the fiction", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a014e/1334883407527/1000w/pulp_fiction_poster_by_samraw08-d3b7d7i.png", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
robocop = media.Movie("Robocop", "1987", "Robot cop takes on Detroit crime", "http://unrealitymag.com/wp-content/uploads/2010/08/roadshow-robocop.jpg", "https://www.youtube.com/watch?v=zbCbwP6ibR4")
re_animator = media.Movie("Re-Animator", "1985", "Watch science come alive", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a014d/1334883392087/1000w/re_animator_poster_by_samraw08-d3fv9dd.png", "https://www.youtube.com/watch?v=6NOcRIHiRtc")
back_to_the_future  = media.Movie("Back to the Future", "1985", "A boy travels back in time to the 1950s", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0159/1334883569203/1000w/back_to_the_future_poster_by_samraw08-d3a5jrr.png", "https://www.youtube.com/watch?v=qvsgGtivCgs")
dawn_of_the_dead = media.Movie("Dawn of the Dead", "1979", "The dead walk the earth, watch out!", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0158/1334883553005/1000w/dawn_of_the_dead_vector_poster_by_samraw08-d39gyv8.png", "https://www.youtube.com/watch?v=j69OPw9nFHw")
let_me_in = media.Movie("Let Me In", "2010", "Innocence Dies. Abby Doesn't.", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0153/1334883479693/1000w/let_me_in_poster_by_samraw08-d3da2s2.png", "https://www.youtube.com/watch?v=reRRAEVHq8E")
a_nightmare_on_elm_street = media.Movie("A Nightmare on Elm Street", "1984", "A fight to the death with Freddy", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0151/1334883452553/1000w/nightmare_on_elm_street_poster_by_samraw08-d3e1vja.png", "https://www.youtube.com/watch?v=dCVh4lBfW-c")
on_the_waterfront = media.Movie("On The Waterfront", "1954", "One man on a hunt for justice", "http://unrealitymag.com/wp-content/uploads/2010/08/roadshow-waterfront.jpg", "https://www.youtube.com/watch?v=QOLHbQjtSFs")
there_will_be_blood = media.Movie("There Will Be Blood", "2007", "Dad and son search for oil in the west", "http://unrealitymag.com/wp-content/uploads/2010/08/roadshow-there-will-be-bloo.jpg", "https://www.youtube.com/watch?v=OjZ1rUQQKxY")
the_goonies = media.Movie("The Goonies", "1985", "Never say die", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0145/1334883272051/1000w/the_goonies_vector_poster_by_samraw08-d397xmv.png", "https://www.youtube.com/watch?v=hJ2j4oWdQtU")
drag_me_to_hell = media.Movie("Drag Me to Hell", "2009", "Be careful with whom you deal", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c4e4b0d911b44a0140/1334883195077/1000w/drag_me_to_hell_vector_poster_by_samraw08-d39jfim.png", "https://www.youtube.com/watch?v=BUZTybLlWKI")
rocky = media.Movie("Rocky", "1976", "A down and out boxer rises to the top", "http://unrealitymag.com/wp-content/uploads/2010/08/roadshow-rocky.jpg", "https://www.youtube.com/watch?v=7RYpJAUMo2M")



movies = [pulp_fiction, re_animator, back_to_the_future, robocop, let_me_in, rocky, dawn_of_the_dead, on_the_waterfront, the_goonies, there_will_be_blood, drag_me_to_hell, a_nightmare_on_elm_street]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__name__, media.Movie.__module__)

