// var mentos = 3
// console.log(mentos)

// integer, float, negative, 0
// 3 strings
// 2 boolean


// console.log(4)
// console.log(5.009)
// console.log(-5)
// console.log("mentos")
// console.log(true)
// console.log(false)

// var a = 7
// a = a + 3
// console.log(a)
// a -= 9
// console.log(a)

// var k = "abc"
// var z = "xyz"
// var y
//
// y = z
// z = k
// k = y
// console.log(k) //xyz
// console.log(z) //abc

// score = 87
//
// if (score > 90 && score < 100)console.log("A")
// if (score > 80 && score < 90)console.log("B")
// if (score > 70 && score < 80)console.log("C")
//
// if (score > 90 ) {
//   console.log("A")
// }
// else if (score > 80){
//   console.log("B")
// }
// else if (score > 70){
//   console.log("C")
// }
// else if (score > 60){
//   console.log("D")
// }
// else {
//   console.log("F")
// }


// var count = 5
//
// while (count>0){
//   console.log(count)
//   count -=1
// }

// var num = 5
// var result = 1
// while (num>0){
//   result = result * num
//   num -=1
// }
// console.log(result)


// var fi = 0
// var fi2 = 1
// while (fi < 10000){
//   var fi3 = fi + fi2
//   fi2 = fi
//   fi = fi3
//
//   console.log(fi3)
// }
//
// var x = 1
// var num = 5
//
// function fibo(num){
//   if (x<num){
//     x = x + (x-1)
//   }
//   else {
//     return x
//   }
// }
// console.log(x)
//
// function add(a,b){
//   console.log(a+b+3)
//   return a+b
// }
// add (7,4)
// console.log(add(1,2))
// var meals = [8,3.5,0.3,]
function eat(done){
  var food = 0
  if (done < 1){
    food = ["starve",1]
  }
  else if (done < 5){
    food = ["ramyun",4.5]
    // mymoney -= 4.5
  }
  else if (done < 10){
    food = ["mcdonalds",6]
    // mymoney -= 6
  }
  else if (done < 20){
    food = ["curry",13]
    // mymoney -= 13
  }
  else {
    food = ["steak",40]
    // mymoney -=40
  }
  return food
}

var mymoney = 219
while (mymoney > 0){
  console.log(eat(mymoney)[0]+mymoney)
  mymoney -= eat(mymoney)[1]
}
