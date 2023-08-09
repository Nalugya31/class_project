
var delete_btn1 = document.getElementById('mydelete_btn1');
var delete_btn2 = document.getElementById('mydelete_btn2');

function funki(){
    var del = confirm('Are you sure you want to delete?');
    if (del){
        alert('Your about to delete');
        delete_btn1.style.display=none;

    }
}


