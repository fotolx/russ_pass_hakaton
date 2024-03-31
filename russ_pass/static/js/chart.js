const ctx = document.getElementById('analizator-Chart').getContext('2d');

fetch(window.location.href+'/chart/', {
    method: 'GET', 
    headers: {
        'Content-Type': 'application/json',
    },
})
.then(response => response.json())
.then(data => {

    const jsonPeriods = JSON.parse(data.periods.replace(/'/g, "\"")); 
    const jsonData = JSON.parse(data.data).map(Number); 
    const jsonMsgs = JSON.parse(data.msgs_sent).map(Number);

    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: jsonPeriods,
            datasets: [{
                label: 'Received messages',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                data: jsonData
            },
            {
                label: 'Sent messages',
                backgroundColor: 'rgba(255, 116, 85, 0.3)',
                borderColor: 'rgba(255, 116, 85, 1)',
                borderWidth: 1,
                data: jsonMsgs,
            },]
        },
        options: {
            indexAxis: 'x',
            barPercentage: 0.85, 
            categoryPercentage: 0.85
        }
    });
})
.catch(error => console.error('Error fetching from server', error));







