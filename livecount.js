var updateCount = function() {
    var textbox = $("#inputText");
    var text_value = textbox.val();
    var text_length = text_value.length;
    var countElement = $("#charCount");
    countElement.text(text_length);
};

var textbox = $("#inputText");  // Selecting the correct element
textbox.on("input", updateCount);