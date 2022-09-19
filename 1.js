/* Kyu  : 8
 * Link : https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
 * Description : A function that checks if two characters are the same
 */

//Function
function sameCase(a, b){

    const regex = /[a-z]/i;
    let n = a.search(regex) + b.search(regex);

    if(n<0){
        return -1;//Not a letter
    }
    if(
        (a.toLowerCase() == a && b.toLowerCase() == b)
        ||
        (a.toUpperCase() == a && b.toUpperCase() == b)
    )
        return 1;//Same Case
    if(
        (a.toLowerCase() == a && b.toUpperCase() == b)
        ||
        (a.toUpperCase() == a && b.toLowerCase() == b)
    )
        return 0;//Different Case
}

//Test
let output = sameCase("S","Y");
console.log(output);