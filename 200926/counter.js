var count = 0

function increase(num){
  document.getElementById("but").innerHTML = num;
}

function countNum(){
  count = count + 1
  document.getElementById("but").innerHTML = count;

}

function oddNum(){
  count = 3
    document.getElementById("but").innerHTML = count;
}

function reset(){
  count = 0
  document.getElementById("but").innerHTML =  count
}
