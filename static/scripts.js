function predictMood() {
    event.preventDefault();
    var text = document.getElementById("inputText").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict_mood", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("mood").innerText = "Mood: " + response.mood;
        }
    };
    var data = JSON.stringify({ text: text });
    xhr.send(data);
    return false;
}
