console.log('js 연결 확인');

boardContentId = document.querySelector('#board_content_id').value;
console.log('boardContentId : ' + boardContentId);

document.querySelector('#btn_index').addEventListener('click', function(e){
    location.href='/render/index'
});