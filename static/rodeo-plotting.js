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

var y0 = [];
var y1 = [];

for (var i = 0; i < 50; i ++) {
	y0[i] = Math.random();
	y1[i] = Math.random() + 1;
}

var trace1 = {
  y: y0,
  type: 'box'
};

var trace2 = {
  y: y1,
  type: 'box'
};

var data = [trace1, trace2];

Plotly.newPlot('plotlyPlot', data);
