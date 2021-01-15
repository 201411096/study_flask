console.log('js 연결 확인');

let btn_write = document.querySelector('#btn_write');
let btn_cancel = document.querySelector('#btn_cancel');

btn_cancel.addEventListener('click', function(){
    location.href = '/render/index';
});