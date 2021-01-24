console.log('js 연결 확인');

let current_board_id = -1;
let current_page = 1;
makeBoardList();

// 임시 페이징
document.querySelector('#input_paging').addEventListener('keyup',(e)=>{
    current_page = document.querySelector('#input_paging').value;
    console.log('210119 : ' + document.querySelector('#input_paging').value);
    getDataAndMakeBoardContentList();
});

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
        event_click_boardList(e);
    }
});

// 게시판글쓰기 버튼 클릭시에
document.querySelector('#container_btn_boardWrite').addEventListener('click', function(e){
    if(e.target.matches('#btn_boardWrite')){
        location.href='/render/boardWrite?board_id='+current_board_id;    
    }
})

// 게시판글목록의 행클릭시에
document.querySelector('#board_content_container').addEventListener('click', function(e){
    if(e.target.matches('#board_content_container td')){
        var boardContentId = e.target.parentElement.dataset.boardContentId;
        location.href = '/render/boardContent/'+boardContentId;
    }
});

// 각 게시판의 글 목록 데이터를 불러와서 테이블 형식으로 만듬
function getDataAndMakeBoardContentList(){
    fetch('/board/list', {
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body : JSON.stringify({
            "board_id":current_board_id,
            "page":current_page
        })
    }).then((res)=>res.json())
    .then((data)=>{
        // console.log(data);
        checkAuthority(data);
        makeBoardContentList(data);
    });
}

// 각 게시판의 글 목록을 불러온 리스트를 테이블 형식으로 만듬
function makeBoardContentList(data){
    let boardListData = data['boardListData'];
    let boardContentContainerList = document.querySelector('#board_content_container');
    let columnList = ['board_content_num', 'member_name', 'board_content_title', 'board_content_regdatetime'];
    let columnNameList = ['글번호', '닉네임', '제목', '등록시간'];
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    boardContentContainerList.innerHTML = '';

    let theadtr = document.createElement('tr');
    for(var i=0; i<columnList.length; i++){
        var th = document.createElement('th');
        th.innerText = columnNameList[i];
        th.classList.toggle('table-c'+(i));
        theadtr.append(th);
    }
    thead.append(theadtr);

    for(var i=0; i<boardListData.length; i++)
    {
        // console.log(boardListData[i]);
        var tr = document.createElement('tr');
        tr.dataset.boardContentId = boardListData[i]['board_content_id'];
        tr.classList.toggle('board_contentRow');
        if(boardListData[i]['board_content_deleted']=='N'){
            for (var j=0; j<columnList.length; j++){
                var td = document.createElement('td');
    
                // 답글 추가 전
                // td.innerText = boardListData[i][columnList[j]];
                
                // 답글_01
                if(j==2){
                    var tempString = '';
                    for(var k=0; k< parseInt(boardListData[i]['depth']) ; k++ ){
                        tempString +='ㄴ';
                    }
                    td.innerText = tempString+boardListData[i][columnList[j]];
                }else{
                    td.innerText = boardListData[i][columnList[j]];
                }
                td.classList.toggle('table-c'+(j));
                tr.append(td);
            }
        }else{
            for (var j=0; j<columnList.length; j++){
                var td = document.createElement('td');
        
                // 답글 추가 전
                // td.innerText = boardListData[i][columnList[j]];
                
                // 답글_01
                if(j==2){
                    var tempString = '';
                    for(var k=0; k< parseInt(boardListData[i]['depth']) ; k++ ){
                        tempString +='ㄴ';
                    }
                    td.innerText = tempString+'삭제된 글입니다.';
                }else{
                    td.innerText = '--';
                }
                td.classList.toggle('table-c'+(j));
                tr.append(td);
            }
        }

        tbody.append(tr);
    }

    table.append(thead);
    table.append(tbody);
    boardContentContainerList.append(table);
}

// 게시판목록을 불러와서 게시판 버튼생성
function makeBoardList(){
    fetch('/boardList', {
        method : 'GET'
    }).then(res => res.json())
    .then((data) =>{
        let boardListContainer = document.querySelector('#boardList');

        for(var i=0; i<data['boardList'].length; i++){
            var divelement = document.createElement('div');
            var button = document.createElement('button');
            button.dataset.boardId = data['boardList'][i]['board_id'];
            button.innerText = data['boardList'][i]['board_name'];
            divelement.append(button);
            boardListContainer.append(divelement);
        }         
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
    return data;
}

async function getCurrentAuthorityData(){
    res = await fetch('/authority/getList')
    data = await res.json();
    return data;    
}

async function event_click_boardList(e){
    board_id = e.target.dataset.boardId;
    current_board_id = board_id;
    document.querySelector('#current_board_name_container').innerText = e.target.innerText;
    current_page = 1;

    document.querySelector('#container_btn_boardWrite').innerHTML = '';

    var current_authority_data = await getCurrentAuthorityData();
    if(current_authority_data['authority_board'][board_id]["authority_board_content_read"]==0){
        document.querySelector('#board_content_container').innerHTML = '';
        alert('게시판 조회 권한이 없습니다.');
    }else{
        getDataAndMakeBoardContentList();
        if( (current_authority_data['authority_board'][board_id]["authority_board_content_write"]==1) || (current_authority_data['authority_board'][board_id]["authority_board_content_write"]==2) ){
            var btn = document.createElement('button');
            btn.setAttribute('id', 'btn_boardWrite');
            btn.innerText = '게시판 글쓰기';
            document.querySelector('#container_btn_boardWrite').append(btn);
        }
    }
    
}

function checkAuthority(data){
    if( 'code' in data  ){
        if(data['code'] == '22'){
            location.href='/render/notice_required_authority';
        }
    }    
}