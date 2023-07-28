function offset(el) {
    var rect = el.getBoundingClientRect(),
    scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
}

var $window = $(window);
var contentTop = $("#head-inscription").offset();
var contentStart = contentTop - $window.height();
var contentEnd = contentTop + $("#head-inscription").height();

$window.scroll(function() {
    var div = document.querySelector('#head-inscription');
    var divOffset = offset(div);
    var scrollTop = $window.scrollTop();
    if(scrollTop + $("#header").outerHeight()/1.5 < (divOffset.top + $("#head-inscription").height())) {
            clearInterval(timer);
            hide();
  } else {
            clearInterval(timer);
            document.getElementById("header-inscription").style.visibility = "visible";
            show();
  }
});

let timer 
function hide(){
    clearInterval(timer);
     timer = setInterval(function() {
        if (parseFloat(window.getComputedStyle(document.getElementById("header-inscription")).getPropertyValue("opacity")) <= 0){
            clearInterval(timer);
            document.getElementById("header-inscription").style.visibility = "hidden";
        } 
        else {
            document.getElementById("header-inscription").style.opacity = parseFloat(window.getComputedStyle(document.getElementById("header-inscription")).getPropertyValue("opacity"))-0.025;
        }
      }, 5);
}

function show(){
    clearInterval(timer);
    timer = setInterval(function() {
        if (parseFloat(window.getComputedStyle(document.getElementById("header-inscription")).getPropertyValue("opacity")) >= 1){
            clearInterval(timer);
        } 
        else {
            document.getElementById("header-inscription").style.opacity = parseFloat(window.getComputedStyle(document.getElementById("header-inscription")).getPropertyValue("opacity"))+0.02;
        }
      }, 5);
}