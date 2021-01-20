console.log('js 연결 확인');

boardContentId = document.querySelector('#board_content_id').value;
console.log('boardContentId : ' + boardContentId);

getCommentList();

document.querySelector('#btn_index').addEventListener('click', function(e){
    location.href='/render/index'
});

//답글달기 클릭이벤트
document.querySelector('#btn_replyContent').addEventListener('click', function(e){
    bpid = document.querySelector('#board_content_id').value;
    bid = document.querySelector('#board_id').value;
    location.href='/render/boardWrite?board_id='+bid+'&board_content_pid='+bpid;
});

//댓글달기 클릭이벤트
document.querySelector('#comment_write_btn').addEventListener('click', function(e){
    var bid = document.querySelector('#board_content_id').value;
    var comment_body = document.querySelector('#comment_write_textfield').value;
    var dataObject = {
        "board_content_id":bid,
        "comment_body":comment_body        
    }
    if(document.querySelector('#comment_container div.selected_comment') != null){
        dataObject['comment_pid']=document.querySelector('#comment_container div.selected_comment').dataset.commentId;
    }
    fetch('/comment/write',{
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body : JSON.stringify(dataObject)
        // body : JSON.stringify({
        //     "board_content_id":bid,
        //     "comment_body":comment_body
        // })
    }).then((res)=>res.json())
    .then((data)=>{
        console.log(data);
        getCommentList();
    });
});

//댓글 클릭이벤트
document.querySelector('#comment_container').addEventListener('click', function(e){
    // console.log('comment_container...')
    if(e.target.parentElement.matches('#comment_container div.comment_container')){
        // console.log('click');
        if(e.target.parentElement.classList.contains('selected_comment')){
            e.target.parentElement.classList.toggle('selected_comment');
        }else{
            var containers = document.querySelectorAll('div.comment_container');
            for (var i=0; i<containers.length; i++){
                containers[i].classList.remove('selected_comment');
            }
            e.target.parentElement.classList.toggle('selected_comment');
        }
    }
});

function makeCommentList(data){
    var comment_container = document.querySelector('#comment_container');
    comment_container.innerHTML = '';
    // console.log('makeCommentList..');
    // console.log(data['commentListData']);
    var listData = data['commentListData'];
    for(var i=0; i<listData.length ; i++){
        var div = document.createElement('div');
        div.classList.toggle('comment_container');
        div.dataset.commentId = listData[i]['comment_id'];
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