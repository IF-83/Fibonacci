
button = document.querySelector("#calc")
button.addEventListener("click", fetchFibo)


function fetchFibo() {
    let n = document.querySelector("#n").value
    algorithm = document.querySelector("input[name=method]:checked").value
    fetch("/calculate?n="+n+"&method="+algorithm)
    .then( data => data.json())
    .then( data => {
        output_par = document.querySelector("div#output p")
        output_area = document.querySelector("div#output input")
        if (data.err) {
            output_par.innerHTML = data.err
            output_area.value = "ERROR"
        } else {
            output_par.innerHTML = `The ${data.n}<sup>th</sup> Fibonacci number has been calculated in ${data.sec} seconds. The result has ${data.digits} digits and its approximate value is ${data.float_rep}.<br>You can copy the exact number from the box below:`
            output_area.value = data.fib
        }
     })
}
