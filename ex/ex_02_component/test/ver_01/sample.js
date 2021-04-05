class Calculator extends HTMLElement{
    constructor(id){
        super();
        this.caller_component_id = id;
        this.render();
        this.setStyle();
        this.setEvent();
        this.setEvent2();
    }

    check_num(params) {
        return params.match(/[\d .]/);
    }
    numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    render(){
        this.calculator_body = document.createElement('custom-calculator')
        this.calculator_body.setAttribute('data-calculator_id', this.caller_component_id);
        this.calculator_body.setAttribute('class', 'hide');
        this.result = 0;
        this.value_array = ['(', ')', '%', 'AC', 7, 8, 9, '/', 4, 5, 6, '*', 1, 2, 3, '-', 0, '.', '=', '+'];
        this.componentList = [];
        this.rowList = [];
        this.resultArea = document.createElement('textarea');
        this.resultArea.setAttribute('id', 'calculator_resultarea');
        this.appendChild(this.resultArea);
        for (var i=0; i<20; i++ ){
            this.componentList[i] = document.createElement('button');
            this.componentList[i].setAttribute('class', 'calculator');
            this.componentList[i].setAttribute('value', this.value_array[i]);
            this.componentList[i].appendChild(document.createTextNode(this.value_array[i]));
            if(i%4==0){
                this.rowList[parseInt(i/4)] = document.createElement('div');
            }
            this.rowList[parseInt(i/4)].appendChild(this.componentList[i]);
        }

        for(var i=0; i<this.rowList.length; i++){
            this.appendChild(this.rowList[i]);
        }
    }

    setStyle(){
        // var style = document.createElement('style');
        // document.head.appendChild(style);
        // style.sheet.insertRule(
        // `button.calculator{
        //     width: 40px;
        //     height: 40px;
        // }
        // custom-calculator{
        //     position : absolute;
        //     display: none;
        // }
        // custom-calculator.hide{
        //     display:none;
        // }
        // custom-calculator.show{
        //     display:block;
        // }`
        // );
        var style = document.createElement('style');
        document.head.appendChild(style);
        style.sheet.insertRule('button.calculator{ width : 40px; height : 40px; }', 0);
        style.sheet.insertRule('custom-calculator{ position : absolute; display: none; }', 1);
        style.sheet.insertRule('custom-calculator{ display:none; }', 2);
        style.sheet.insertRule('custom-calculator{ display:block; }', 3);
    }

    setEvent(){
        this.addEventListener('click', function(e){
            if(e.target.matches('button.calculator')){
                console.log(e.target.value)
                this.resultArea.value = this.resultArea.value+e.target.value;
                
                //계산
                if(e.target.value == '='){
                    let cal_result = this.calculate();
                    this.resultArea.value = cal_result;

                    this.dispatchEvent(new CustomEvent('custom_01', {
                        "detail": this.resultArea.value,
                        bubbles:true
                    }));
                }
                //초기화
                if(e.target.value == 'AC'){
                    this.resultArea.value = '';
                    this.dispatchEvent(new CustomEvent('custom_01', {
                        "detail": this.resultArea.value,
                        bubbles:true
                    }));
                }
                this.statusFunc();
            }
        });
    }

    setEvent2(){
        let calculator_element = document.querySelector('[data-calculator_id="'+this.caller_component_id+'"]');

        document.addEventListener('click', function(e){                
            // 버튼을 눌렀을 경우(필수)에 계산기가 열려있지 않거나(undefined 혹은 ''), 열려있는 계산기를 부른 버튼과 동일한 버튼일 경우(계산기를 닫는 경우)
            if(e.target.matches('#'+this.caller_component_id)  && ( Calculator.caller_element==='' || Calculator.caller_element===undefined || Calculator.caller_element===this.caller_component_id ) ){
                // 계산기를 부착할 element
                let target_attach_component = document.querySelector('[data-calculator="'+ e.target.id +'"]');

                // 계산기의 제어권을 갖는 버튼의 id를 저장(해당 버튼의 id는 버튼과 묶여있는 input의 data-calculator 속성으로 찾을 수 있음)
                Calculator.caller_element = e.target.id;
                
                // show -> hide로 갈 경우 caller_element 초기화
                if(calculator_element.classList.contains('show')){ 
                    Calculator.caller_element = '';
                }

                // show, hide 토글링
                calculator_element.classList.toggle('hide');
                calculator_element.classList.toggle('show');

                // caculator 위치 이동
                calculator_element.style.top = target_attach_component.getBoundingClientRect().bottom +'px';
                calculator_element.style.left = target_attach_component.getBoundingClientRect().left +'px';
                
                // 버튼 클릭시에 target_attach_component의 값이 전달됨
                document.querySelector('#calculator_resultarea').value=target_attach_component.value;
            }
        });

        //input 이벤트 시 계산기에 변화를 주는 이벤트
        document.addEventListener('input', function(e){
            // 계산기의 제어권을 가는 element의 id(버튼의 id가 담겨있음) 와 같은 input을 찾아감(input의 data-calculator 속성을 제어권을 갖는 버튼의 id와 같음)
            if(document.getElementById(e.target.id).getAttribute('data-calculator') === Calculator.caller_element){
                document.querySelector('#calculator_resultarea').value=document.getElementById(e.target.id).value;
            }
        });

        //계산 완료 시에 input에 영향을 주는 이벤트
        document.addEventListener('custom_01', function(e){
            document.querySelector('[data-calculator="'+ Calculator.caller_element +'"]').value = e.detail;
            Calculator.statusFunc();
        });
    }

    statusFunc(){
        let resultAreaValue = this.resultArea.value.replaceAll(',', '');
        let resultValue = '';
        let cal_unit = [0,];

        for (var i=0; i<resultAreaValue.length; i++){
            if(this.check_num(resultAreaValue.charAt(i)) && i==0){
                cal_unit[0]=resultAreaValue.charAt(i);
            }else if(this.check_num(resultAreaValue.charAt(i))){
                cal_unit[cal_unit.length-1]=cal_unit[cal_unit.length-1]+resultAreaValue.charAt(i);
            }else{
                cal_unit.push(resultAreaValue.charAt(i));
                cal_unit.push('');
            }
        }
        for(var i=0; i<cal_unit.length; i++){
            if(this.check_num(cal_unit[i]))
                cal_unit[i]= this.numberWithCommas(cal_unit[i]);
        }
        for(var i=0; i<cal_unit.length; i++){
            resultValue += cal_unit[i];
        }
        this.resultArea.value = resultValue;
    }

    calculate(){
        let resultAreaValue = this.resultArea.value.replaceAll(',', '');
        let cal_unit = [0,];

        for (var i=0; i<resultAreaValue.length-1; i++){
            if(this.check_num(resultAreaValue.charAt(i)) && i==0){
                cal_unit[0]=resultAreaValue.charAt(i);
            }else if(this.check_num(resultAreaValue.charAt(i))){
                cal_unit[cal_unit.length-1]=cal_unit[cal_unit.length-1]+resultAreaValue.charAt(i);
            }else{
                cal_unit.push(resultAreaValue.charAt(i));
                cal_unit.push('');
            }
        }
        return this.cal_method(cal_unit);
    }

    calculate_withCalUnit(cal_unit){
        let return_value = 0;
        let temp_operator = '';

        if(cal_unit.length>=1 && this.check_num(cal_unit[0])){
            return_value = parseFloat(cal_unit[0]);
        }
        for(var i=1; i<cal_unit.length; i++){
            if(!this.check_num(cal_unit[i])){
                temp_operator = cal_unit[i];
            }else{
                switch(temp_operator){
                    case '+':
                        return_value += parseFloat(cal_unit[i]);
                        break;
                    case '-':
                        return_value -= parseFloat(cal_unit[i]);
                        break;
                    case '*':
                        return_value *= parseFloat(cal_unit[i]);
                        break;
                    case '/':
                        return_value /= parseFloat(cal_unit[i]);
                        break;
                    case '%':
                        return_value %= parseFloat(cal_unit[i]);
                        break;
                }
            }
        }
        return return_value;
    }

    cal_withEval(cal_unit){
        let cal_string = '';
        for(var i=0; i<cal_unit.length; i++){
            cal_string += cal_unit[i];
        }
        return eval(cal_string);
    }

    cal_withNewFunc(cal_unit){
        let cal_string = '';
        for(var i=0; i<cal_unit.length; i++){
            cal_string += cal_unit[i];
        }
        return new Function('return ' + cal_string)();
    }

    cal_method(cal_unit){
        return this.cal_withNewFunc(cal_unit);
        // return this.cal_withEval(cal_unit);
        // return this.calculate_withCalUnit(cal_unit);
    }
}

customElements.define('custom-calculator', Calculator);