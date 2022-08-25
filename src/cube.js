let operation = "cube";
let num = 6;
switch(operation) {
  case "square":
    console.log(num * num);
    break;
  case "cube":
    console.log(num * num * num);
    break;
  case "square root":
    console.log(Math.sqrt(num));
    break;
  default:
    console.log(num);
}