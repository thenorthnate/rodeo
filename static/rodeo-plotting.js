function makePlot1(x, y) {
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

/*
Dynamically add plotting element!
function addElement () {
  // create a new div element
  var newDiv = document.createElement("div");
  newDiv.id = "someID";
  // and give it some content
  var newContent = document.createTextNode("Hi there and greetings!");
  // add the text node to the newly created div
  newDiv.appendChild(newContent);

  // add the newly created element and its content into the DOM
  var currentDiv = document.getElementById("div1");
  document.body.insertBefore(newDiv, currentDiv);
}
*/

function makePlot(data) {
  var x0 = data["0"];
  var y0 = data["1"];

  var trace1 = {
    x: x0,
    y: y0,
    mode: 'markers',
    type: 'scatter'
  };
  var data = [trace1];
  Plotly.newPlot('plotlyPlot', data);
}
