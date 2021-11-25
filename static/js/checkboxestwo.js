var expanded = false;
function showCheckboxestwo() 
{

  var checkboxes = document.getElementById("checkboxestwo");

    
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
