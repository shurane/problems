var removeOuterParentheses = function(S) {
    var count = 0;
    arr = S.split("");
    for(let i = 0; i < arr.length; i++){
        if(arr[i]==="("){
            if(count === 0){
                arr.splice(i, 1);
                i--;
            }
            count ++;
        }
        else if(arr[i]===")"){
            if(count === 1){
                arr.splice(i,1);
                i--;
            }
            count --;
        }
    }
    return arr.join("");
};

console.log(removeOuterParentheses("(()())(())"));