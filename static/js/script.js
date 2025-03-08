document.getElementById("generateBtn").addEventListener("click", function () {
    fetch("/generate")
        .then(response => response.json())
        .then(data => {
            document.getElementById("lyricSnippet").innerText = data.lyrics;
            document.getElementById("generateBtn").dataset.songTitle = data.song_title;
            document.getElementById("resultMessage").innerText = "";
        })
        .catch(error => {
            console.error("Error fetching lyrics:", error);
            document.getElementById("lyricSnippet").innerText = "Failed to fetch lyrics. Please try again.";
        });
});

document.getElementById("checkBtn").addEventListener("click", function () {
    const userGuess = document.getElementById("userGuess").value;
    const songTitle = document.getElementById("generateBtn").dataset.songTitle;

    fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ guess: userGuess, song_title: songTitle })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultMessage").innerText = data.message;
    })
    .catch(error => {
        console.error("Error checking answer:", error);
        document.getElementById("resultMessage").innerText = "Failed to check answer. Please try again.";
    });
});