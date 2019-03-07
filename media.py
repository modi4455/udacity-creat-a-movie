#define the movies class that cotain the details of movies
import webbrowser
class Movie():
	#This class provides a way to store movie related information.
    #Attributes:
        #title: A string to store the title of the movie.
        ##storyline: A string to store the basic plot of the movie.
        #release_year: A string to store the release date of the movie.
        #movie_type: A string  to store type of the movies.
        #VALAID_RATING:A string to store VALAID_RATING of each movie
        #poster_image_url: A string to store the URL of the movie poster.
        #trailer_youtube_url: A string to store the URL of the movie trailer.
	def __init__(self ,movie_title,movie_storyline, released_year,movie_type,VALAID_RATING,poster_image ,trailer_youtube):
		#Initialises Movie class instance variables
		self.title = movie_title
		self.storyline = movie_storyline
		self.released_year= str(int(released_year))
		self.type= movie_type
		self.VALAID_RATING= VALAID_RATING
		self.poster_image_url= poster_image
		self.trailer_youtube_url = trailer_youtube
	def show_trailer(self):
		#play the movie trailer in the web browser.
		webbrowser.open(self.trailer_youtube_url)
    
    	
        
