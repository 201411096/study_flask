console.log('js 연결 확인')

let btn_signup = document.querySelector('#btn_signup');
let btn_login = document.querySelector('#btn_login');

btn_signup.addEventListener('click', function(){
    location.href = '/render/signup'
});

btn_login.addEventListener('click', function(){
    fetch('/member/login', {
        method : 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body : JSON.stringify({
            "member_id" : document.querySelector('#id').value,
            "member_pw" : document.querySelector('#pw').value
        })
    }).then(res => res.json())
    .then(data => {
        console.log('/member/login complete ...');
        console.log(data);
        console.log(data['code']);

        if(data['code']=='1'){
            console.log('login success');
            // location.href = '/render/login';
        }else if(data['code']=='0'){
            console.log('login fail');
            alert('로그인 실패');
        }
    });
});