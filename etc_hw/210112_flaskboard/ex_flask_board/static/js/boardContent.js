console.log('js 연결 확인');

boardContentId = document.querySelector('#board_content_id').value;
console.log('boardContentId : ' + boardContentId);

document.querySelector('#btn_index').addEventListener('click', function(e){
    location.href='/render/index'
});

//답글
document.querySelector('#btn_replyContent').addEventListener('click', function(e){
    bpid = document.querySelector('#board_content_id').value;
    bid = document.querySelector('#board_id').value;
    location.href='/render/boardWrite?board_id='+bid+'&board_content_pid='+bpid;
});

//댓글
document.querySelector('#comment_write_btn').addEventListener('click', function(e){
    var bid = document.querySelector('#board_content_id').value;
    var comment_body = document.querySelector('#comment_write_textfield').value;
    fetch('/comment/write',{
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body : JSON.stringify({
            "board_content_id":bid,
            "comment_body":comment_body
        })
    }).then((res)=>res.json())
    .then((data)=>{
        console.log(data);
    });
});