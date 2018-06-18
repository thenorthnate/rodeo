document.getElementById("inputFile").onchange = function() {listFiles()};

function listFiles() {
  var fileInput = document.getElementById('inputFile');
  var selectedFileList = document.getElementById("selectedFiles");
  while (selectedFileList.hasChildNodes()) {
    selectedFileList.removeChild(selectedFileList.firstChild);
  }

  if ("files" in fileInput) {
    if (fileInput.files.length == 0) {
      var node = document.createElement("li");
      var textnode = document.createTextNode("No files selected");
      node.appendChild(textnode);
      selectedFileList.appendChild(node);
    } else {
      for (var i = 0; i < fileInput.files.length; i++) {
        var txt = ""
        var node = document.createElement("li");
        var file = fileInput.files[i];
        if ("name" in file) {
          txt += file.name;
        }
        if ("size" in file) {
          var fSize = file.size;
          if (fSize > 1000) {
            txt += " (" + fSize/1000 + " kB)";
          } else {
            txt += " (" + fSize + " bytes)";
          }

        }
        var textnode = document.createTextNode(txt);
        node.appendChild(textnode);
        selectedFileList.appendChild(node);
      }
    }
  } else {
    if (fileInput.value == "") {
      var node = document.createElement("li");
      var textnode = document.createTextNode("Select one or more files");
      node.appendChild(textnode);
      selectedFileList.appendChild(node);
    } else {
      var node = document.createElement("li");
      var textnode = document.createTextNode("Files not supported by your browser");
      node.appendChild(textnode);
      selectedFileList.appendChild(node);
    }
  }
}
