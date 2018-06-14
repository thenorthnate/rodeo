function makePlot(x, y) {
  var ctx = document.getElementById("myChart");
  console.log(x);
  console.log(y);
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: x,
      datasets: [{
        data: y,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false,
      }
    }
  });
}
