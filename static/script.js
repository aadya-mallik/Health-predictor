function predict(){
let sleep = document.getElementById("sleep").value;
let exercise = document.getElementById("exercise").value;
let junk = document.getElementById("junk").value;
let stress = document.getElementById("stress").value;
document.getElementById("result").innerText = "Predicting...";
fetch("/predict",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
sleep:sleep,
exercise:exercise,
junk:junk,
stress:stress
})
})
.then(response => response.json())
.then(data=>{
document.getElementById("result").innerText = data.prediction;
})
.catch(error=>{
document.getElementById("result").innerText = "Error occurred";
console.log(error);
});

}