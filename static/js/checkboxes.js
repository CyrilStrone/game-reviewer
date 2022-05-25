let expanded = false;





function showCheckboxestwo() {
    let childyear = document.getElementById('w3layouts-box-list__year').getElementsByTagName('li').length;
    let height = $('#checkbox_list_year').height();
    let checkboxestwo2 = document.getElementById('checkboxestwo');
    let checkboxes1 = document.getElementById('checkboxes');

    height = Math.floor(childyear / 5) * height + 20 + 50 + 30;



    if (!expanded) {
        document.getElementById('side-bar-script').style.height = (height) + "px";
        $('#side-bar-script').height(height);
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

    let childyear = document.getElementById('w3layouts-box-list__ganre').getElementsByTagName('li').length;
    let height = $('#checkbox_list_year').height();
    height = Math.ceil(childyear / 5) * height + 20 + 50 + 30;

    if (!expanded) {
        document.getElementById('side-bar-script').style.height = (height) + "px";
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