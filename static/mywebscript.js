let historyData = [];

function analyzeEmotion() {

    let text = document.getElementById("textInput").value;

    if(text.trim() === ""){
        document.getElementById("result").innerHTML =
        "Please enter some text.";
        return;
    }

    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`)
    .then(response => response.json())
    .then(data => {

        let emoji = "😐";

        if(data.dominant_emotion.includes("joy"))
            emoji = "😊";

        else if(data.dominant_emotion.includes("sadness"))
            emoji = "😢";

        else if(data.dominant_emotion.includes("anger"))
            emoji = "😡";

        else if(data.dominant_emotion.includes("fear"))
            emoji = "😨";

        else if(data.dominant_emotion.includes("disgust"))
            emoji = "🤢";

        else if(data.dominant_emotion.includes("Tie"))
            emoji = "🎭";
        else if(data.dominant_emotion.includes("surprise"))
            emoji = "😲";

        else if(data.dominant_emotion.includes("love")) 
            emoji = "❤️";
        
        else emoji = "😐";

        document.getElementById("emoji").innerHTML = emoji;

        document.getElementById("result").innerHTML = `
        <h3>Emotion Analysis Result</h3>

        😊 Joy: ${data.joy}<br>
        😢 Sadness: ${data.sadness}<br>
        😡 Anger: ${data.anger}<br>
        😨 Fear: ${data.fear}<br>
        🤢 Disgust: ${data.disgust}<br><br>

        <b>Dominant Emotion:</b>
        ${data.dominant_emotion}
        `;

        historyData.unshift(
            `${emoji} "${text}" → ${data.dominant_emotion}`
        );

        updateHistory();

    });
}

function updateHistory(){

    let html = "";

    historyData.forEach(item => {
        html += `<div class="history-item">${item}</div>`;
    });

    document.getElementById("historyList").innerHTML = html;
}

function toggleTheme(){
    document.body.classList.toggle("dark");
}

function startVoiceInput(){

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if(!SpeechRecognition){
        alert("Speech Recognition not supported.");
        return;
    }

    const recognition =
        new SpeechRecognition();

    recognition.start();

    recognition.onresult = function(event){

        document.getElementById("textInput").value =
            event.results[0][0].transcript;
    };
}