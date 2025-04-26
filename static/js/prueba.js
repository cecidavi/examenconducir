const totalQuestions = document.querySelectorAll('.question-container').length;
let currentQuestion = 1;
let timer = 60;
let interval;

function showQuestion(index) {
    document.querySelectorAll('.question-container').forEach(q => q.classList.remove('active'));
    const question = document.getElementById(`q${index}`);
    if (question) {
        question.classList.add('active');
        resetTimer();
        updateProgress(index);
    } else {
        // No hay más preguntas
        clearInterval(interval);
        document.getElementById('submitBtn').classList.remove('d-none');
        document.getElementById('timer').classList.add('d-none');
        document.getElementById('progressText').classList.add('d-none');
    }
}

function resetTimer() {
    clearInterval(interval);
    timer = 60;
    document.getElementById('timer').textContent = timer;

    interval = setInterval(() => {
        timer--;
        document.getElementById('timer').textContent = timer;
        if (timer <= 0) {
            nextQuestion();
        }
    }, 1000);
}

function nextQuestion() {
    clearInterval(interval);
    currentQuestion++;
    showQuestion(currentQuestion);
}

function updateProgress(index) {
    const progressText = document.getElementById('progressText');
    if (progressText) {
        progressText.textContent = `Pregunta ${index} de ${totalQuestions}`;
    }
}

// Avanzar al cambiar la respuesta
document.getElementById('examForm').addEventListener('change', () => {
    setTimeout(nextQuestion, 500);
});

// Mostrar la primera pregunta
showQuestion(currentQuestion);
