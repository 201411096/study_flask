console.log('js 연결 확인');

document.addEventListener('click', (e)=>{
    console.log('event.targetId : ' + e.target.id);
    if(e.target.id === 'btn_logout'){
        location.href = '/member/logout'
    }else if(e.target.id === 'btn_login'){
        location.href = '/render/login'
    }else if(e.target.id === 'btn_signup'){
        location.href = '/render/signup'
    }
});