// Create an array of movie objects.
// Each movie should have a title, rating, and hasWatched properties.
// Iterate through the array and print out something that looks like:
// 	You have watched "In Bruges" - 5 Stars
// 	You have watched "Frozen" - 4.5 Stars
// 	You have watched "Mad Max Fury Road" - 5 Stars
// 	You have watched "Lex Miserables" - 3.5 Stars

var movies = [
	{
		title: "The Final Master",
		rating: 4.5,
		hasWatched: true
	},
	{
		title: "Mad Max Fury Road",
		rating: 5,
		hasWatched: false
	},
	{
		title: "Moana",
		rating: 4,
		hasWatched: true
	},
	{
		title: "Pets",
		rating: 3.5,
		hasWatched: true
	},
];

movies.forEach(function(element){
	console.log(buildString(element));
});

function buildString(movie) {
	var result = "You have";
	if (movie.hasWatched === false){
		result += " not";
	};
	result += " watched ";
	result += "\"" + movie.title + "\"";
	result += " - " + movie.rating + " stars";
	return result
};