console.log('js 연결 확인');

let boardContentId = document.querySelector('#board_content_id').value;
let boardId = document.querySelector('#board_id').value;
console.log('boardContentId : ' + boardContentId);

getCommentList();

document.querySelector('#btn_index').addEventListener('click', function(e){
    location.href='/render/index'
});

// 버튼 컨테이너 클릭이벤트
document.querySelector('#button_container').addEventListener('click', function(e){
    if(e.target.matches('button#btn_update')){
        console.log('수정버튼 클릭이벤트 확인');
        location.href='/render/boardUpdate?board_content_id='+document.querySelector('#board_content_id').value;
    }else if(e.target.matches('button#btn_delete')){
        console.log('삭제버튼 클릭이벤트 확인');
        dataObject = {
            "board_content_id":document.querySelector('#board_content_id').value,
            "board_id":boardId
        }
        fetch('/board/delete',{
            method : 'POST',
            headers : {
                'Content-Type':'application/json',
            },
            body : JSON.stringify(dataObject)            
        }).then( (res) => (res.json()) )
        .then( (data) => {
            console.log(data);
            if(data['code'] == '1' ){
                location.href='/render/index';
            }
        });
    }else if(e.target.matches('#btn_replyContent')){
        bpid = document.querySelector('#board_content_id').value;
        bid = document.querySelector('#board_id').value;
        location.href='/render/boardWrite?board_id='+bid+'&board_content_pid='+bpid;
    }
});

//댓글 클릭이벤트
document.querySelector('#comment_write_container').addEventListener('click', function(e){
    if(e.target.matches('#comment_write_btn')){
        event_commentWrite();
    }
})

//댓글달기 클릭이벤트
function event_commentWrite(){
    var bid = document.querySelector('#board_content_id').value;
    var comment_body = document.querySelector('#comment_write_textfield').value;
    var dataObject = {
        "board_content_id":bid,
        "comment_body":comment_body,
        "board_id":boardId        
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
    }).then((res)=>res.json())
    .then((data)=>{
        console.log(data);
        getCommentList();
    });    
}

//댓글 클릭이벤트
document.querySelector('#comment_container').addEventListener('click', function(e){
    // 행단위 댓글 클릭시에
    if(e.target.parentElement.matches('#comment_container div.comment_container')){
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

    //삭제버튼 클릭이벤트
    if(e.target.matches('button.btn_delete_comment')){
        var btnData = e.target.dataset;
        console.log('btnData ..');
        console.log(btnData);
        fetch('/comment/delete',{
            method : 'POST',
            headers : {
                'Content-Type':'application/json',
            },
            body : JSON.stringify({
                "comment_id":btnData['commentId'],
                "board_id":boardId
            })
        }).then(res => res.json())
        .then( (data) => {
            console.log('fetch delete_comment completed');
            console.log(data);
            checkAuthority(data);
            if(data['code']==1){
                console.log('data[code]=1...');
                getCommentList();
            }else{
                console.log('data[code]=0...');
            }
        });
    }
});

async function makeCommentList(data){
    var current_member_data = await getCurrentMemberData();
    var current_authority_data = await getCurrentAuthorityData();
    var current_member_id = current_member_data['data'][0]['member_id'];

    var comment_container = document.querySelector('#comment_container');
    comment_container.innerHTML = '';
    var listData = data['commentListData'];
    for(var i=0; i<listData.length ; i++){
        if(listData[i]['comment_deleted']=='N'){
            var flag_deleteBtn = 0;
            if(current_authority_data['authority_board'][boardId]['authority_board_content_delete'] == '2'){
                flag_deleteBtn = 1;
            }else if(current_authority_data['authority_board'][boardId]['authority_board_content_delete'] == '1'){
                if(current_member_id == listData[i]['member_id']){
                    flag_deleteBtn = 1;
                }
            }            
            var div = document.createElement('div');
            div.classList.toggle('comment_container');
            div.dataset.commentId = listData[i]['comment_id'];
            div.dataset.memberId = listData[i]['member_id'];
            var span1 = document.createElement('span');
            var span2 = document.createElement('span');
            span1.innerText = listData[i]['member_nickname'];
            
            //댓글의 댓글 표시
            var tempString='';
            for(var k=0; k<listData[i]['depth']; k++){
                tempString+='ㄴ'
            }
            span2.innerText = tempString + listData[i]['comment_body'];
            span1.classList.toggle('comment_col_container_01');
            span2.classList.toggle('comment_col_container_02');
            div.append(span1);
            div.append(span2);
            if(flag_deleteBtn == 1){
                var span3 = document.createElement('span');
                var button = document.createElement('button');
                button.classList.toggle('btn_delete_comment');
                button.dataset.commentId = listData[i]['comment_id'];
                button.innerText='삭제하기';
                span3.append(button);
                div.append(span3);
            }
            comment_container.append(div);
        }else{
            var div = document.createElement('div');
            div.classList.toggle('comment_container');
            div.dataset.commentId = listData[i]['comment_id'];
            div.dataset.memberId = listData[i]['member_id'];
            var span1 = document.createElement('span');
            var span2 = document.createElement('span');
            span1.innerText = '--';

            //댓글의 댓글 표시
            var tempString='';
            for(var k=0; k<listData[i]['depth']; k++){
                tempString+='ㄴ'
            }
            span2.innerText = tempString + '삭제된 댓글입니다.';
            // span2.innerText = '삭제된 댓글입니다.';
            span1.classList.toggle('comment_col_container_01');
            span2.classList.toggle('comment_col_container_02');
            div.append(span1);
            div.append(span2);  
            comment_container.append(div);          
        }

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
            "board_content_id":bid,
            "board_id":boardId
        })
    }).then((res)=>res.json())
    .then((data)=>{
        checkAuthority(data);
        makeCommentList(data);
    });
}

async function getCurrentMemberData(){
    res = await fetch('/member/getCurrentMemberData', {
        method : 'GET',
        headers : {
            'Content-Type':'application/json',
        }        
    });
    data = await res.json();
    // console.log('getCurrentMemberData() ...');
    // console.log(data);
    return data;
}

async function getCurrentAuthorityData(){
    res = await fetch('/authority/getList')
    data = await res.json();
    // console.log('getCurrentAuthorityData() ...');
    // console.log(data);
    return data;    
}

function checkAuthority(data){
    if( 'code' in data  ){
        if(data['code'] == '22'){
            location.href='/render/notice_required_authority';
        }
    }    
}