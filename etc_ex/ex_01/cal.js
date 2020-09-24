class Calculator extends HTMLElement{
    constructor(){
        super();
        this.render();
        this.setEvent();
    }
    render(){
        this.result = 0;
        this.value_array = ['(', ')', '%', 'AC', 7, 8, 9, '/', 4, 5, 6, '*', 1, 2, 3, '-', 0, '.', '=', '+'];
        this.componentList = [];
        this.rowList = [];
        this.resultArea = document.createElement('textarea');
        this.appendChild(this.resultArea);
        for (var i=0; i<20; i++ ){
            this.componentList[i] = document.createElement('button');
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
    setEvent(){
        this.addEventListener('click', function(e){
            console.log(e.target.value)
            this.resultArea.value = this.resultArea.value+e.target.value;
            
            //계산
            if(e.target.value == '='){
                let cal_result = this.calculate();
                this.resultArea.value = cal_result;
            }

            //초기화
            if(e.target.value == 'AC'){
                this.resultArea.value = '';
            }
        });
    }
    calculate(){
        let resultAreaValue = this.resultArea.value;
        let cal_unit = [0,];
        // console.log('check resultarea value in calculate ...' + this.resultArea.value);
        console.log('check resultarea value in calculate ...' + resultAreaValue);
        console.log('typecheck in calculate ' + typeof(resultAreaValue));

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
        return this.calculate_withCalUnit(cal_unit);
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
        console.log('return_value = ' + return_value );
        return return_value;
    }
    check_num(params) {
        return params.match(/[\d]/);
    }
}

customElements.define('custom-calculator', Calculator);