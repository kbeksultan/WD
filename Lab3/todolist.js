var list = document.getElementById('list');
var myInput = document.getElementById('myInput');
var myBtn = document.getElementById('addBtn');

var newElement = function(e)
{
    if(myInput.value !== "")
    {
        var newLi = document.createElement('li');

        var checkBox = document.createElement('input');
        checkBox.type = "checkbox";
        checkBox.className = "checks";
        checkBox.onclick = onBoxClick;

        var span = document.createElement('span');
        span.className = "mySpan";
        span.appendChild(checkBox);

        var myImg = document.createElement('img');
        myImg.className = "image";
        myImg.src = "redbin.png";
        myImg.onclick = deletes;

        var txt = document.createElement('p');
        txt.innerHTML = myInput.value;
        
        
        span.appendChild(txt);
        newLi.appendChild(span);
        newLi.appendChild(myImg);
        
        list.appendChild(newLi);
        myInput.value = "";
        
    }
};

var onBoxClick = function(e)
{
    if(e.target.checked)
    {
        var current = e.target.parentNode;
        current.className = "newClass";
    }
    else{
        var current = e.target.parentNode;
        current.className = "mySpan";
    }
    console.log(e.target);
};
 
var deletes  = function(e)
{
    var bigLi = event.target.parentNode;
    bigLi.remove();
}