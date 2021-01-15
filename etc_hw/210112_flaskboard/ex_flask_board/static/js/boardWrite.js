console.log('js 연결 확인');

let btn_write = document.querySelector('#btn_write');
let btn_cancel = document.querySelector('#btn_cancel');

btn_cancel.addEventListener('click', function(){
    location.href = '/render/index';
});

btn_write.addEventListener('click', function(){
    fetch('/board/write', {
        method : 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body : JSON.stringify({
            "board_content_pid" : document.querySelector('#board_content_pid').value,
            "board_content_title" : document.querySelector('#board_content_title').value,
            "board_content_body" : document.querySelector('#board_content_body').value
        })
    });
})