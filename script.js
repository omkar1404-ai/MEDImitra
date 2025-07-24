async function send() {
    const inputField = document.getElementById("userInput");
    const input = inputField.value.trim();
    if (!input) return;

    const chatBox = document.getElementById("messages");

    // Append user message
    chatBox.innerHTML += `<div class='msg user'><strong>You:</strong> ${input}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    showTyping();

    try {
        const response = await fetch("/get_diagnosis", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: input })
        });

        const data = await response.json();
        removeTyping();
        chatBox.innerHTML += `<div class='msg bot'><strong>Bot:</strong> ${data.response}</div>`;
        speak(data.response); // For voice output
        inputField.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        removeTyping();
        chatBox.innerHTML += `<div class='msg bot'><strong>Bot:</strong> Something went wrong. Try again later.</div>`;
        console.error("Fetch error:", error);
    }
}

// Typing animation
function showTyping() {
    const chatBox = document.getElementById("messages");
    chatBox.innerHTML += `<div class='msg bot' id='typing'>Bot: <span class='dots'>●●●</span></div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
function removeTyping() {
    const typingElem = document.getElementById("typing");
    if (typingElem) typingElem.remove();
}

// Voice output
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}

// Speech input (microphone)
function startVoiceInput() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) return alert("Speech recognition not supported in this browser.");

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById("userInput").value = transcript;
        send();
    };

    recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
    };
}
