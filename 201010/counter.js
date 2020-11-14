var count = 0

function increase(num){
  document.getElementById("but").innerHTML = num;
}

function countNum(){
  count = count + 1
  document.getElementById("but").innerHTML = count;

}

function oddNum(){
  count = count + 1
  odd = count * 2 - 1

    document.getElementById("odd").innerHTML = odd;
}

function dice(){
  diceNum = Math.floor (Math.random() *6) + 1


  document.getElementById("dice").innerHTML = diceNum;
}

function date(){
  var d = new Date()
  document.getElementById("time").innerHTML = d.getTime()}

function reset(){
  count = 0
  document.getElementById("but").innerHTML =  count
}
