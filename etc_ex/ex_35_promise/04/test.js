// Promise.race(iterable)

function myPromise(promiseName, myFlag, time){
    return new Promise( (resolve, reject) =>{
        if(myFlag === 0){
            reject(new Error("myFlag === 0 ..."));
        }else{
            setTimeout(
                function(){resolve(time)}, time*1000
            );
        }
    });
}

var promise_01 = myPromise('promise_01', 1, 6)
.then( (result) => { console.log(result); return result; } );

var promise_02 = myPromise('promise_02', 1, 9)
.then( (result) => {
    console.log(result);
    return result;
});

var promise_03 = myPromise('promise_03', 1, 2)   // 에러발생시 해당 에러를 같이 반환함
// var promise_03 = myPromise('promise_03', 1, 2)
.then( (result) => { 
    console.log(result);
    return result;
}).catch( (result)=>{
    console.log(result);
    return result;
});

myPromiseList = [promise_01, promise_02, promise_03];

Promise.race(myPromiseList)
.then( (value) => {
    console.log('value(Promise.race)  : ' + value); // 가장 먼저 완료된 결과값(에러일 경우 에러를 반환)
})