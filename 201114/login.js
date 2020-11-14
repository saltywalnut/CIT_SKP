function login(){

  var userid = document.forms["userForm"]["userId"].value;
  var userPW = document.forms["userForm"]["userPW"].value;
  var realPW = "1234"
  var realid = "4321"
  // document.getElementById("username").innerHTML = name
  // alert(userid + "is the wrong username" + userPW + "is the wrong password")
  if (realPW === userPW && realid === userid){
    alert("로그인 성공!")
    document.getElementById('userImg').src = "fifa.png"
    document.getElementById('div').style = "background-color : SkyBlue;width:50%;margin:auto;text-align:center;margin-top:100px"
  }
  else {
    alert ("로그인 실패")
  }
}
// function pw(){
//
//   var userid = document.forms["userForm"]["userPW"].value;
//   // document.getElementById("username").innerHTML = name
//   alert(userid + "is the wrong password")
// }
