// Generate the Table
function makeTable(data) {
  var header = [];
  for (var key in data) {
    if (data.hasOwnProperty(key)) {
      header.push(key);
    }
  }


  if (header.length > 0) {
    console.log(header);
    var feTable = document.getElementById("fileExcerptTable");
    var feHeader = feTable.createTHead();
    var feHeaderRow = feHeader.insertRow(0);

    for (var i = 0; i < header.length; i++) {
      var cell = feHeaderRow.insertCell(-1)
      cell.innerHTML = header[i];
    }
    for (var i = 0; i < 10; i++) {
      var row = feTable.insertRow(-1);
      for (var j = 0; j < header.length; j++) {
        var cell = row.insertCell(-1);
        cell.innerHTML = data[header[j]][i];
      }
    }
  } else {
    var feTable = document.getElementById("fileExcerptTable");
    var feHeader = feTable.createTHead();
    var feHeaderRow = feHeader.insertRow(0);
    var cell = feHeaderRow.insertCell(-1)
    cell.innerHTML = "No Data Found";
  }
}
