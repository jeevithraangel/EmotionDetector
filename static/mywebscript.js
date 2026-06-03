function analyzeEmotion() {
    let text = document.getElementById("textInput").value;

    fetch(`/emotionDetector?textToAnalyze=${text}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById("result").innerHTML =
            `<h3 class="result-title">Emotion Analysis Result</h3>${data}`;
    })
    .catch(error => {
        document.getElementById("result").innerHTML =
            "Error: Unable to analyze emotion";
    });
}