function redirect(thisUrl) {
  window.location = thisUrl;
}

function snackbar(thisUrl) {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar")

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  setTimeout(function(){ redirect(thisUrl);,1000);
}