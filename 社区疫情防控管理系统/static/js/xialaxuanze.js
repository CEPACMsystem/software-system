function chy(obj){
    var rr = $("input[type='radio']:checked").val();
    if(rr =="小区居民"){
        document.getElementById("patent1").style.display="";
        document.getElementById("patent2").style.display="";
    }
}
function chn(obj){
    var rr = $("input[type='radio']:checked").val();
    if(rr =="物业管理员" || rr =="访客"){
        document.getElementById("patent1").style.display="none";
        document.getElementById("patent2").style.display="none";
    }
}