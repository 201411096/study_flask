console.log('js 연결 확인')

let btn_cancel = document.querySelector('#btn_cancel');
let btn_confirm = document.querySelector('#btn_confirm');

btn_cancel.addEventListener('click', function(){
    location.href = '/render/login'
});

btn_confirm.addEventListener('click', function(){
    fetch('/member/signup', {
        method : 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body : JSON.stringify({
            "member_id" : document.querySelector('#id').value,
            "member_pw" : document.querySelector('#pw').value,
            "member_name" : document.querySelector('#name').value,
            "member_birthday" : document.querySelector('#date').value,
            "member_phonenumber": document.querySelector('#phonenumber').value,
            "member_nickname" : document.querySelector('#nickname').value
        })
    }).then(res => res.json())
    .then(data => {
        console.log('/member/signup complete ...');
        console.log(data);
        // console.log(data['code']);
        
        if(data['code']=='1'){
            console.log('signup success');
            location.href = '/render/login';
        }else if(data['code']=='0'){
            console.log('signup fail');
            alert('회원가입 실패');
        }
    });
});