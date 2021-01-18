console.log('js 연결 확인');

current_board_id = -1;
makeBoardList();

document.querySelector('#authcontainer').addEventListener('click', (e)=>{
    // console.log('event.targetId : ' + e.target.id);
    if(e.target.id === 'btn_logout'){
        location.href = '/member/logout'
    }else if(e.target.id === 'btn_login'){
        location.href = '/render/login'
    }else if(e.target.id === 'btn_signup'){
        location.href = '/render/signup'
    }
});

// 게시판리스트 안의 게시판 버튼을 클릭했을 경우
document.querySelector('#boardList').addEventListener('click', function(e){
    if(e.target.matches('#boardList > div > button')){
        console.log(e.target.dataset.boardId);
        board_id = e.target.dataset.boardId
        current_board_id = board_id;
        document.querySelector('#current_board_name_container').innerText = e.target.innerText;
    }
    fetch('/board/contentList', {
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body : JSON.stringify({
            "board_id":current_board_id
        })
    }).then((res)=>res.json())
    .then((data)=>{
        console.log(data);
    });
});

// 게시판글쓰기 버튼 클릭시에
document.querySelector('#btn_boardWrite').addEventListener('click', function(e){
    location.href='/render/boardWrite?board_id='+current_board_id
});

// 게시판목록을 불러와서 게시판 버튼생성
function makeBoardList(){
    fetch('/boardList', {
        method : 'GET'
    }).then(res => res.json())
    .then((data) =>{
        // console.log('check data(makeBoardList) ...');
        // console.log(data);
        // console.log('check length(boardList) : ' + data['boardList'].length);

        let boardListContainer = document.querySelector('#boardList');

        for(var i=0; i<data['boardList'].length; i++){
            // console.log('check data(makeBoardList) ...');
            // console.log(data['boardList'][i]);
            var divelement = document.createElement('div');
            var button = document.createElement('button');
            button.dataset.boardId = data['boardList'][i]['board_id'];
            button.innerText = data['boardList'][i]['board_name'];
            divelement.append(button);
            boardListContainer.append(divelement);
        }         
    });
}