import fresh_tomatoes
from media import Movie

# Creates Movie objects
inception = Movie("Inception",
                  "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                  "https://www.youtube.com/watch?v=66TuSJo4dZM")

toy_story = Movie("Toy Story",
                  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")

battle_la = Movie("Battle: Los Angeles",
                  "https://upload.wikimedia.org/wikipedia/en/2/29/Battle_Los_Angeles_Poster.jpg",
                  "https://www.youtube.com/watch?v=9otTzrO9Bfw")

resident_evil = Movie("Resident Evil",
                      "http://www.gstatic.com/tv/thumb/movieposters/29625/p29625_p_v8_aa.jpg",
                      "https://www.youtube.com/watch?v=o1Q68pbiEBI")

wreck_it_ralph = Movie("Wreck It Ralph",
                       "http://t3.gstatic.com/images?q=tbn:ANd9GcR6e2NEBAIaJQ8_-1KSrUc1NKuyBWAK0ch7DerecaEhYEow1dnL",
                       "https://www.youtube.com/watch?v=87E6N7ToCxs")

meet_the_millers = Movie("Meet the Millers",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcT6xk5KWWVADWHUBeG1ZXTfW-Y2pMIbiHbcWMSb2Mrg_G06vG_e",
                         "https://www.youtube.com/watch?v=0Vsy5KzsieQ")

# Stores Movie objects in a list/array to be used by the method fresh_tomatoes.open_movies_page
movies_list = [inception, toy_story, battle_la,
               resident_evil,
               wreck_it_ralph, meet_the_millers]

fresh_tomatoes.open_movies_page(movies_list)
