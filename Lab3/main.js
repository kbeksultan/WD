
$(document).ready(function(){
    setCurrentTime();
    setInterval(function(){setCurrentTime();},1000);
});
  
  
function setCurrentTime(){
    var d = new Date();
    var h = d.getHours();
    var m =d.getMinutes();

    if(h < 10 && m < 10){
        h = "0" + h;
        m = "0" + m;
    }
    document.getElementById('time').innerHTML = h + ":" + m;    
}



