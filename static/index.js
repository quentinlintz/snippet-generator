function generateSnippet() {
    var languageSelect = document.getElementById('language');
    var taskInput = document.getElementById('task');
    var outputArea = document.getElementById('outputArea');
    var generateButton = document.querySelector('button[type="button"]');
    var timeLabel = document.getElementById('timeLabel');

    languageSelect.disabled = true;
    taskInput.disabled = true;
    generateButton.disabled = true;

    outputArea.textContent = "Loading...";

    var startTime = Date.now();

    fetch('/generate-snippet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ language: languageSelect.value, task: taskInput.value }),
    })
        .then(response => response.json())
        .then(data => {
            var endTime = Date.now();
            var timeToGenerate = (endTime - startTime) / 1000;

            outputArea.textContent = data.code.trim();
            timeLabel.textContent = `Took ${timeToGenerate.toFixed(2)} seconds!`
        })
        .catch((error) => {
            console.error('Error:', error);
            outputArea.textContent = "An error occurred. Please try again.";
        })
        .finally(() => {
            languageSelect.disabled = false;
            taskInput.disabled = false;
            generateButton.disabled = false;
        });
}