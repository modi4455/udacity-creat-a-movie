#store datails of movies and display them in website
#we should import media "class" anf fresh tomatoes to display movie in website
import media
import fresh_tomatoes
def film():
	#creates nine movie , initialising these objects with title ,story line,
	# released year, movie type , rating ,poster and youtube trailer 
	room= media.Movie("Room",
	 "story of A young boy is raised within the confines of a small shed.source: IMDB",
	 "2015",
	 "drama",
	 "R",
	 "https://ia.media-imdb.com/images/M/MV5BMjE4NzgzNzEwMl5BMl5BanBnXkFtZTgwMTMzMDE0NjE@._V1_SY1000_SX675_AL_.jpg",
	 "https://www.youtube.com/watch?v=E_Ci-pAL4eE")
	gone_girl =media.Movie("Gone Girl", 
		"With his wife's disappearance having become the focus of an intense media circus.source: IMDB",
		"2014",
		"crime, drama, mystrey",
		"R",
		"https://ia.media-imdb.com/images/M/MV5BYjgwY2E1N2QtNDJkMi00YzE4LThiYTItYWI5YmE4NWMzMGFhXkEyXkFqcGdeQXVyMjU3OTA4NzQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
	me_before_you = media.Movie("Me Before You",
		"A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of. source: IMDB",
	    "2016", 
	    "drama , romance",
	    "PG-13" ,
	    "https://ia.media-imdb.com/images/M/MV5BMTQ2NjE4NDE2NV5BMl5BanBnXkFtZTgwOTcwNDE5NzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
	    "https://www.youtube.com/watch?v=Eh993__rOxA")
	gifted= media.Movie("gifted", 
		"Frank, a single man raising his child prodigy niece Mary, is drawn into a custody battle with his mother.source: IMDB", 
		"2017", 
		"drama",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BMjQ2NDU3NDE0M15BMl5BanBnXkFtZTgwMjA3OTg0MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=tI01wBXGHUs")
	her= media.Movie("Her",
		"In a near future, a lonely writer develops an unlikely relationship with an operating system designed to meet his every need.source: IMDB", 
		"2013", 
		"drama, romance,sci-fi",
		"R" ,
		"https://ia.media-imdb.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_UX182_CR0,0,182,268_AL_.jpg", 
		"https://www.youtube.com/watch?v=WzV6mXIOVl4")
	The_Imitation_Game= media.Movie("The Imitation Game",
		"During World War II, the English mathematical genius Alan Turing tries to crack the German Enigma code with help from fellow mathematicians. source: IMDB",
		"2014",
		"Biography, Drama, History ",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BOTgwMzFiMWYtZDhlNS00ODNkLWJiODAtZDVhNzgyNzJhYjQ4L2ltYWdlXkEyXkFqcGdeQXVyNzEzOTYxNTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/results?search_query=The+Imitation+Game")
	your_name= media.Movie("Your Name",
		"Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart? source: IMDB",
		"2016",
		"Animation, Drama, Fantasy",
		"PG",
		"https://ia.media-imdb.com/images/M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcxYThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=s0wTdCQoc2k")
	The_help= media.Movie("The Help",
		"An aspiring author during the civil rights movement of the 1960s decides to write a book detailing the African American maids' point of view . source: IMDB",
		"2011",
		"drama",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BMTM5OTMyMjIxOV5BMl5BanBnXkFtZTcwNzU4MjIwNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=l0dWCXCjX9o")
	metres_down = media.Movie("47 metres down",
		"Two sisters vacationing in Mexico are trapped in a shark cage at the bottom of the ocean. With less than an hour of oxygen left and great white sharks circling nearby, they must fight to survive.source: IMDB",
		"2017",
		"Adventure, Drama, Horror ",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BOGJlNDJkZmEtMjUwNS00ZWViLWIyZGEtN2Y5ZjZlNDE1NWJkXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=ddYSGGJAKOk")
	Nocturnal_Animals= media.Movie("Nocturnal Animals",
		"A wealthy art gallery owner receives a draft of her ex-husband's new novel, a violent thriller she interprets as a veiled threat and a symbolic revenge tale. source: IMDB",
		"2016",
		"Crime, Drama, Romance",
		"R",
		"https://ia.media-imdb.com/images/M/MV5BMTYwMzMwMzgxNl5BMl5BanBnXkFtZTgwMTA0MTUzMDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=-H1Ii1LjyFU")
	The_Fault_in_Our_Stars= media.Movie("The Fault in Our Stars",
		"Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam. source: IMDB",
		"2014",
		"drama, romance",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BMjA4NzkxNzc5Ml5BMl5BanBnXkFtZTgwNzQ3OTMxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=9ItBvH5J6ss")
	The_Theory_of_Everything= media.Movie("The Theory of Everything",
		"A look at the relationship between the famous physicist Stephen Hawking and his wife.source: IMDB",
		"2014",
		"Biography, Drama, Romance",
		"PG-13",
		"https://ia.media-imdb.com/images/M/MV5BMTAwMTU4MDA3NDNeQTJeQWpwZ15BbWU4MDk4NTMxNTIx._V1_UX182_CR0,0,182,268_AL_.jpg",
		"https://www.youtube.com/watch?v=Salz7uGp72c")
	#store the movie names in a list
	Movies=[room, gone_girl, me_before_you,gifted, her, The_Imitation_Game,
	your_name ,The_help ,metres_down ,Nocturnal_Animals ,The_Fault_in_Our_Stars ,
	The_Theory_of_Everything]
	#open the movies website in the browser, featuring the movies above.
	fresh_tomatoes.open_movies_page(Movies)
film()