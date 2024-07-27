/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(num: number[][]): void {
    let a=num.length
    for (let i=0; i<a; i++){            
        for (let j=i; j<a; j++){
            let temp=num[i][j]
            num[i][j]=num[j][i]
             num[j][i]= temp
        }
    }
    for (let i=0; i<a; i++){
        for (let j=0; j<a/2; j++){
            let temp2=num[i][j]
            num[i][j]=num[i][a-j-1]
             num[i][a-j-1]= temp2
        }
    }

};



// 1 4 7   7 4 1
// 2 5 8
// 3 6 9 

