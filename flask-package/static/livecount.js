// Create a new function
var livecount = function() {
	// Everything in old livecount.jd
	var updateCount = function() {
	    var textbox = $("#inputText");
	    var text_value = textbox.val();
	    var text_length = text_value.length;
	    var countElement = $("#charCount");
	    countElement.text(text_length);
	};

	var textbox = $("#inputText");  // Selecting the correct element
	textbox.on("input", updateCount);
};

// Register the new function to the ready event of document 
$(document).on("ready", livecount);