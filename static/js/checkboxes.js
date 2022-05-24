let expanded = false;


function showCheckboxestwo() {
    let checkboxestwo2 = document.getElementById('checkboxestwo');
    let checkboxes1 = document.getElementById('checkboxes');


    if (!expanded) {
        document.getElementById('side-bar-script').style.height = "232px";
        checkboxestwo2.style.display = "block";
        checkboxes1.style.display = "none";
        expanded = true;
    } else {
        document.getElementById('side-bar-script').style.height = "100%";
        checkboxestwo2.style.display = "none";
        checkboxes1.style.display = "none";
        expanded = false;
    }
}



function showCheckboxes() {
    let checkboxes = document.getElementById('checkboxes');
    let checkboxestwo = document.getElementById('checkboxestwo');


    if (!expanded) {
        document.getElementById('side-bar-script').style.height = "232px";
        checkboxes.style.display = "block";
        checkboxestwo.style.display = "none";
        expanded = true;
    } else {
        document.getElementById('side-bar-script').style.height = "100%";
        checkboxes.style.display = "none";
        checkboxestwo.style.display = "none";
        expanded = false;
    }
}