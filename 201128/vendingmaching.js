function buy(button){
  if (button === 1){
   return ["candy",2,30]
 }
  if (button === 2){
    return ["rice",10,500]
  }
  if (button === 3){
    return ["chocolate",3,70]
}
}
console.log(buy(2))

function analyze(product){
  x = product[2]/product[1]
  return x
}
// console.log(analyze(["egg",10,70]))
console.log(analyze(buy(3)))
