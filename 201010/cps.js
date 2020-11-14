var count = 0
var game_start = false
var start_time = 0
var click_count = 0

// function click(){
//   if (game_start) == true:
//     click_count += 1
//   else if (start_time + 5000 < timestamp){
//     click_count = click_count
// }


function cpsMain(){
  var d = new Date()
  var timestamp = d.getTime()
  game_reset = false
  if (game_start == false) {
    game_start = true
    start_time = timestamp
    document.getElementById("start_time").innerHTML = start_time
  }
  else if (start_time + 5000 < timestamp){
    alert("game Finished!\n"+"Total Clicks : " + click_count)
  }
  click_count = click_count  + 1
  document.getElementById("time").innerHTML = timestamp
  document.getElementById("clicks").innerHTML = click_count

}

function reset(){
  start_time = 0
  click_count = 0
  game_start = false
  document.getElementById("start_time").innerHTML = start_time
  document.getElementById("time").innerHTML = start_time
  document.getElementById("clicks").innerHTML = click_count
}
