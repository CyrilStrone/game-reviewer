var expanded = false;
document.getElementById('checkboxes').style.display = "none";
function showCheckboxes() 
{

  var checkboxes = document.getElementById("checkboxes");

    
  if (!expanded) {
  	document.getElementById('side-bar-script').style.height = "232px";
    checkboxes.style.display = "block";
    expanded = true;
  } 
  else {
  	document.getElementById('side-bar-script').style.height = "100%";
    checkboxes.style.display = "none";
    expanded = false;
  }
}
