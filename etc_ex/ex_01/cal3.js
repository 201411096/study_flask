class Calculator extends HTMLElement{
    constructor(){
        super();
        this.render();
        this.setEvent();
    }

    check_num(params) {
        return params.match(/[\d .]/);
    }
    numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    render(){
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
                }
                this.statusFunc();
            }
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