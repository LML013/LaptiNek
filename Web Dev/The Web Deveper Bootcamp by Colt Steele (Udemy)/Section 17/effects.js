// $("button").on("click", function(){
// 	$("div").fadeToggle(500, function(){
// 		// $(this).remove();
// 	});
// });


// $("button").on("click", function(){
// 	$("div").slideDown();
// });

$("button").on("click", function(){
	$("div").slideToggle(1000, function(){
		console.log("SLIDE IS DONE!");
	});
});