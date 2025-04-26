// static/js/dashboard.js

document.addEventListener('DOMContentLoaded', function () {
    const dataContainer = document.getElementById('data-container');
    const labels = JSON.parse(dataContainer.dataset.labels);
    const data = JSON.parse(dataContainer.dataset.calificaciones);

    const ctx = document.getElementById('graficaHistorial').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Calificaciones',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.7)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
});
