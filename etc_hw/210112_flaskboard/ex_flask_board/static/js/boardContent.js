console.log('js 연결 확인');

boardContentId = document.querySelector('#board_content_id').value;
console.log('boardContentId : ' + boardContentId);

document.querySelector('#btn_index').addEventListener('click', function(e){
    location.href='/render/index'
});

document.querySelector('#btn_replyContent').addEventListener('click', function(e){
    bpid = document.querySelector('#board_content_id').value;
    bid = document.querySelector('#board_id').value;
    location.href='/render/boardWrite?board_id='+bid+'&board_content_pid='+bpid;
})