
button = document.querySelector("#calc")
console.log(button)
button.addEventListener("click", fetchFibo)


function fetchFibo() {
    let n = document.querySelector("#n").value
    algorithm = document.querySelector("input[name=method]:checked").value
    fetch("/calculate")
    .then( data => data.json())
    .then( data => alert(data.x))
}
