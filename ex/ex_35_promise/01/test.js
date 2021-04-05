// Promise.resolve()
// Promise.reject()
// Promise.prototype.then()
// Promise.prototype.catch()

function divide(numA, numB){
    return new Promise( (resolve, reject) =>{
        if(numB === 0){
            reject(new Error("unable to divide by 0."));
        }else{
            resolve(numA / numB)
        }
    });
}

divide(8, 2)
.then( (result) => {console.log("result(success) : ", result)} )
.catch( (error) => {console.log("result(error) : ", error)} )

divide(8, 0)
.then( (result) => {console.log("result(success) : ", result)} )
.catch( (error) => {console.log("result(error) : ", error)} )