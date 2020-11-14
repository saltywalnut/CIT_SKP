var count = 0
var game_start = false
var start_time = 0
var click_count = 0
var duration = 500
var playData = []

// function click(){
//   if (game_start) == true:
//     click_count += 1
//   else if (start_time + 5000 < timestamp){
//     click_count = click_count
// }

function lb(record){
  return '<span >'+ record.name+' / </span>'+'<span >'+ record.count+' 회 / </span>'+'<span >'+ moment(record.time).format("YYYY년 MM월 DD일 HH시 mm분 ss초")+'</span>'+'<br/>'

}

function cpsMain(){
  var t = new Date()
  var timestamp = t.getTime()
  var userName = document.forms["userForm"]["userName"].value;
  game_reset = false
  // if (userName == '') {
  //   alert ("please enter a username.")
  //   return
  // }

  if (game_start == false) {
    game_start = true
    start_time = timestamp
    document.getElementById("start_time").innerHTML = start_time
  }
  else if (start_time + duration < timestamp){
    alert("game Finished!\n"+ userName +"'s Clicks : " + click_count)
    // document.getElementById("userName").innerHTML = userName + " / "
    // document.getElementById("clickss").innerHTML = click_count + "회 / "
    // document.getElementById("timerecord").innerHTML = moment().format("YYYY년 MM월 DD일 HH시 mm분 ss초")
    playData.push({name : userName, count : click_count, time: timestamp})
    reset()
    document.getElementById("test").innerHTML = playData.map(lb).join('')
    console.log(playData)
    return
  }
  click_count = click_count  + 1
  document.getElementById("time").innerHTML = timestamp
  document.getElementById("clicks").innerHTML = click_count
  // document.getElementById("t").innerHTML = playData
  document.getElementById("test").innerHTML = playData.map(lb).join('')

}

function reset(){
  start_time = 0
  click_count = 0
  game_start = false
  document.getElementById("start_time").innerHTML = start_time
  document.getElementById("time").innerHTML = start_time
  document.getElementById("clicks").innerHTML = click_count
  document.getElementById("userInput").value = ""
}
