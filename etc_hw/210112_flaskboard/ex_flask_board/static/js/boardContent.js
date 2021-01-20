console.log('js 연결 확인');

boardContentId = document.querySelector('#board_content_id').value;
console.log('boardContentId : ' + boardContentId);

getCommentList();

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

//테스트
// document.querySelector('#test_btn_commentList').addEventListener('click', function(e){
//     getCommentList();
// });

function makeCommentList(data){
    var comment_container = document.querySelector('#comment_container');
    comment_container.innerHTML = '';
    // console.log('makeCommentList..');
    // console.log(data['commentListData']);
    var listData = data['commentListData'];
    for(var i=0; i<listData.length ; i++){
        var div = document.createElement('div');
        div.classList.toggle('comment_container');
        var span1 = document.createElement('span');
        var span2 = document.createElement('span');
        span1.innerText = listData[i]['member_nickname'];
        span2.innerText = listData[i]['comment_body'];
        span1.classList.toggle('comment_col_container_01');
        span2.classList.toggle('comment_col_container_02');
        div.append(span1);
        div.append(span2);
        comment_container.append(div);
    }
}

// 댓글 목록을 가져옴
function getCommentList(){
    var bid = document.querySelector('#board_content_id').value;
    fetch('/comment/list',{
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body : JSON.stringify({
            "board_content_id":bid
        })
    }).then((res)=>res.json())
    .then((data)=>{
        // console.log('commentList...')
        // console.log(data);
        makeCommentList(data);
    });
}