function boldIT( pro) {
  var a = document.getElementById(pro).style.fontWeight;
  if ( a == "bold" ){
    document.getElementById(pro).style.fontWeight = "normal";
  }
  if ( a != "bold" ){
    document.getElementById(pro).style.fontWeight = "bold";
  }
}


