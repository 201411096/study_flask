console.log('js 연결 확인');

makeBoardList();

document.querySelector('#authcontainer').addEventListener('click', (e)=>{
    console.log('event.targetId : ' + e.target.id);
    if(e.target.id === 'btn_logout'){
        location.href = '/member/logout'
    }else if(e.target.id === 'btn_login'){
        location.href = '/render/login'
    }else if(e.target.id === 'btn_signup'){
        location.href = '/render/signup'
    }
});

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
            console.log('check data(makeBoardList) ...');
            console.log(data['boardList'][i]);
            var divelement = document.createElement('div');
            var button = document.createElement('button');
            button.dataset.boardId = data['boardList'][i]['board_id'];
            button.innerText = data['boardList'][i]['board_name'];
            divelement.append(button);
            boardListContainer.append(divelement);
        }

         
    });
}