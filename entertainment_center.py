from media import Movies
import fresh_tomatoes

#Create movie objects from media.Movies()
babyDriver = Movies("Baby Driver",
                    "https://i0.wp.com/media2.slashfilm.com/slashfilm" \
                    "/wp/wp-content/images/baby-driver-poster.jpg",
                    "https://www.youtube.com/watch?v=z2z857RSfhk")
rogueOne = Movies("Star Wars: Rogue One",
                  "http://a.dilcdn.com/bl/wp-content/uploads/sites/6" \
                  "/2016/10/rogueone_onesheetA.jpg",
                  "https://www.youtube.com/watch?v=frdj1zb9sMY")
spiderman = Movies("SpiderMan: Homecoming",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe" \
                   "7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t",
                   "https://www.youtube.com/watch?v=U0D3AOldjMU")
#Place movies in arary
movies = [babyDriver, rogueOne, spiderman]

#Pass array to open movies funciton to create webpage
fresh_tomatoes.open_movies_page(movies)

