
function insert(num) {
    var display = document.getElementById('result');
    
    if (display.getAttribute("data-result") === "true") {
        display.innerHTML = num;
        display.setAttribute("data-result", "false"); 
    } else {
        display.innerHTML += num; 
    }
}


function clean() {
    var display = document.getElementById('result');
    display.innerHTML = "";
    display.setAttribute("data-result", "false"); 
}


function del() {
    var display = document.getElementById('result').innerHTML;
    document.getElementById('result').innerHTML = display.substring(0, display.length - 1);
}


function calc() {
    var display = document.getElementById('result');
    var expression = display.innerHTML;
    
    if (expression) {
        display.innerHTML = eval(expression); 
        display.setAttribute("data-result", "true"); 
    } else {
        display.innerHTML = "void";
    }
}
