class tree extends HTMLElement{
    constructor(){
        super();
        this.serverURL = `http://192.168.56.1:5000/dataFromDb`;
        console.log('js파일 연결 ...')
    }

    connectedCallback(){
        this.nodeIdArray = [];  // nodeId를 담아두는 배열
        this.nodeList = {};     // nodeElement를 담아두는 배열
        this.render();
        this.setEvent();
    }

    // 서버로부터 초기 트리 데이터를 받아와서 저장하는 함수
    async getDataFromServer(){
        // let response = await fetch('http://192.168.0.51:5000/dataFromServer');
        // let response = await fetch('http://192.168.56.1:5000/dataFromServer');
        let response = await fetch(this.serverURL+`?query=WITH recursive cte (id, pid, NAME, description) as(
                                        SELECT id, pid, NAME, description
                                        FROM tree_table
                                        WHERE pid=0
                                        UNION all
                                        SELECT a.id, a.pid, a.name, a.description
                                        FROM tree_table a
                                        INNER JOIN cte
                                        ON a.pid = cte.id)
                                    SELECT * FROM cte ORDER BY pid asc, id asc;`);
        let responseJson = await response.json();
        this.componentData = responseJson;
    }

    func1(){
        console.log('func1...')
    }

    // 트리를 시각화하는 함수(초기 트리 데이터를 가져와서 구성해줌)
    async render(){
        await this.getDataFromServer();
        this.constructTreeWithInitialData();
    }

    // 초기 데이터로 트리를 시각화하는 함수
    constructTreeWithInitialData(){
        for(var i=0; i<this.componentData.length; i++){
            let tempObject = this.componentData[i];
            this.addItem(tempObject.pid, tempObject);
        }
    }

    // args1에 해당하는 element의 바로 밑에 자식들에 args2에 해당하는 자식들이 있는지 확인하는 함수
    checkchildren(element, querySelector){
        let childNodeList = element.children;
        for(var i=0; i<element.children.length; i++){
            if(childNodeList[i].matches(querySelector)){
                return true; // 해당 element를 포함하고 있음
            }
        }
        return false; // 해당 element를 포함하고 있지 않음
    }

    setEvent(){
        this.customClickEventListener(); // click이벤트 처리
        this.customCheckEventListener(); // check이벤트 처리
    }

    // 클릭이벤트 처리함수
    customClickEventListener(){
        this.addEventListener('click', function(e){
            this.toggelingTreeNodeToShow(e);                // 노드를 펼치고 숨기는 함수                      
            this.dispatchTreeCheckEventFromClickEvent(e);
        });
        document.addEventListener('click', (e)=>{ //arrow function을 사용하지 않을 경우 this 바인딩 객체 문제
            this.addItemEventListener(e);
            this.updateItemEventListener(e);
            this.removeItemEventListener(e);
            this.moveItemEventListener(e);
            this.copyItemEventListener(e);
            this.checkRadioEventListener(e);
            this.checkItemEventListener(e);
            this.getSelectedIdEventListener(e);
            this.getSelectedItemEventListener(e);
        });
    }

    customCheckEventListener(){
        this.addEventListener('tree_checkEvent', function(e){
            this.customCheckEventHandler(e);
        });
    }

    checkItemRecursiveToUpperNode(element, checkedFlag){
        if(element != null){
            if(checkedFlag == 'checked'){
                let checkFlag = true;
                let elementChildrenLiList = element.nextElementSibling.children;
                for(var i=0; i<elementChildrenLiList.length; i++){
                    if(elementChildrenLiList[i].children[0].children[0].checked==false){
                        checkFlag=false;
                    }
                }
                if(checkFlag == true){
                    element.children[0].checked=true;
                    this.checkItemRecursiveToUpperNode(document.querySelector('div[data-id="'+element.nodeData.pid +'"]'), 'checked');
                }
                
            }else{
                let checkFlag = false;
                let elementChildrenLiList = element.nextElementSibling.children;
                for(var i=0; i<elementChildrenLiList.length; i++){
                    if(elementChildrenLiList[i].children[0].children[0].checked==false){
                        checkFlag=true;
                    }
                }
                if(checkFlag == true){
                    element.children[0].checked=false;
                    this.checkItemRecursiveToUpperNode(document.querySelector('div[data-id="'+element.nodeData.pid +'"]'), 'unchecked');
                }
            }
        }
    }

    customCheckEventHandler(event){
        let targetElement = document.querySelector('div[data-id="'+event.detail.id +'"]');
        let targetParentElement = document.querySelector('div[data-id="'+targetElement.nodeData.pid +'"]'); // 해당 element가 없다면 null
        let targetParentElementNextUlChildren = null;
        if(targetParentElement != null){
            targetParentElementNextUlChildren = targetParentElement.nextElementSibling.children; // li들이 들어있는 리스트가 나옴
        }

        if(event.detail.state === 'checked'){
            if(targetElement.nextElementSibling!=null){ // 하위 노드가 존재할 경우
                let targetElementChildrenCheckBoxList = targetElement.nextElementSibling.querySelectorAll('input[type="checkbox"]');
                for(var i=0; i<targetElementChildrenCheckBoxList.length; i++){
                    targetElementChildrenCheckBoxList[i].checked=true;
                }
            }
            this.checkItemRecursiveToUpperNode(targetParentElement, 'checked');                         
        }else{
            if(targetElement.nextElementSibling!=null){ // 하위 노드가 존재할 경우
                let targetElementChildrenCheckBoxList = targetElement.nextElementSibling.querySelectorAll('input[type="checkbox"]');
                for(var i=0; i<targetElementChildrenCheckBoxList.length; i++){
                    targetElementChildrenCheckBoxList[i].checked=false;
                }
            }
            this.checkItemRecursiveToUpperNode(targetParentElement, 'unchecked');
        }
    }

    // 직접 체크박스를 클릭했을 경우의 customEvent를 발생시키는 메소드
    dispatchTreeCheckEventFromClickEvent(event){
        if(event.target.matches('input[type="checkbox"]')){
            let eventResult = {};
            eventResult.id = event.target.parentElement.dataset.id;
            if(event.target.checked== false || event.target.checked == undefined){
                eventResult.state = 'unchecked';
            }else{
                eventResult.state = 'checked';
            }
            this.dispatchTreeCheckEvent(eventResult);
        }
    }

    // customEvent를 발생시키는 메소드 => checkItem()과 직접 체크했을 경우에 부름(클릭이벤트)
    dispatchTreeCheckEvent(eventResult){
        this.dispatchEvent(new CustomEvent('tree_checkEvent', {
            detail : eventResult,
            bubbles : true
        }));
    }

    checkItemEventListener(event){
        if(event.target == document.querySelector('#checkCheckBoxButton')){
            let id = parseInt(event.target.parentElement.children[0].value);
            this.checkItem(id);
        }
    }

    checkItem(id){
        let targetNode = document.querySelector('div[data-id="'+ id +'"]');
        let targetNodeCheckBox = targetNode.querySelector('input[type="checkbox"]');
        let eventResult = {};
        eventResult.id = id;
        if(targetNodeCheckBox.checked== false || targetNodeCheckBox.checked == undefined){
            targetNodeCheckBox.checked=true;
            eventResult.state = 'checked';
        }else{
            targetNodeCheckBox.checked=false;
            eventResult.state = 'unchecked';
        }
        this.dispatchTreeCheckEvent(eventResult);
    }

    checkRadioEventListener(event){
        if(event.target == document.querySelector('#checkRadioButton')){
            let id = parseInt(event.target.parentElement.children[0].value);
            this.checkRadio(id);
        }                    
    }

    checkRadio(id){
        let targetNode = document.querySelector('div[data-id="'+ id +'"]');
        let targetNodeRadio = targetNode.querySelector('input[type="radio"]');
        if(targetNodeRadio.checked== false || targetNodeRadio.checked == undefined){
            targetNodeRadio.checked=true;
        }else{
            targetNodeRadio.checked=false;
        }
    }

    // addItem() 작동을 확인하는 이벤트 리스너
    addItemEventListener(event){
        if(event.target == document.querySelector('#addItemCheckButton')){
            let elementData = {
                'id' : parseInt(event.target.parentElement.children[0].value),
                'pid' : parseInt(event.target.parentElement.children[1].value),
                'NAME' : event.target.parentElement.children[2].value,
                'description' : event.target.parentElement.children[3].value
            };
            let pid = event.target.parentElement.children[1].value;
            this.addItem(pid, elementData);
        }
    }

    // updateItem() 작동을 확인하는 이벤트 리스너
    updateItemEventListener(event){
        if(event.target == document.querySelector('#updateItemCheckButton')){
            let elementData = {
                'id' : parseInt(event.target.parentElement.children[0].value),
                'pid' : parseInt(event.target.parentElement.children[1].value),
                'NAME' : event.target.parentElement.children[2].value,
                'description' : event.target.parentElement.children[3].value
            };
            let id = event.target.parentElement.children[0].value;
            this.updateItem(id, elementData);
        }
    }

    // removeItem() 작동을 확인하는 이벤트 리스너
    removeItemEventListener(event){
        if(event.target == document.querySelector('#removeItemCheckButton')){
            this.removeItem(parseInt(event.target.parentElement.children[0].value));
        }
    }

    // moveItem() 작동을 확인하는 이벤트 리스너
    moveItemEventListener(event){
        if(event.target == document.querySelector('#moveItemCheckButton')){
            this.moveItem(parseInt(event.target.parentElement.children[0].value), parseInt(event.target.parentElement.children[1].value));
        }
    }

    // copyItem() 작동을 확인하는 이벤트 리스너
    copyItemEventListener(event){
        if(event.target == document.querySelector('#copyItemCheckButton')){
            this.copyItem(parseInt(event.target.parentElement.children[0].value), parseInt(event.target.parentElement.children[1].value));
        }
    }

    toggelingTreeNodeToShow(event){
        if(event.target.matches('div.tree_node')){
            event.target.classList.toggle('show');
        }
    }

    getSelectedIdEventListener(event){
        if(event.target.matches('#getSelectedIdButton')){
            let id = this.getSelectedId();
            console.log('returned id by getSelectedId() : ' + id);
        }

    }
    getSelectedItemEventListener(event){
        if(event.target.matches('#getSelectedItemButton')){
            let elementData = this.getSelectedItem();
            console.log('returned id by getSelectedItem() ... ');
            console.log(elementData);
        }
    }

    getSelectedId(){
        return parseInt(this.querySelector('input[type="radio"]:checked').parentElement.nodeData.id);
    }

    getSelectedItem(){
        return this.querySelector('input[type="radio"]:checked').parentElement.nodeData;
    }

    addItem(pid, elementData){
        let tempElement = document.createElement('div');
        tempElement.innerText = elementData['NAME'];
        tempElement.setAttribute('data-id', elementData['id']);
        tempElement.setAttribute('class', 'tree_node');
        tempElement.nodeData = elementData;
        
        if(!this.nodeIdArray.includes(elementData['pid'])){
            this.appendChild(tempElement);
        }else{ // pid가 존재하는 경우에 ...
            if(this.nodeList[pid].nextElementSibling==null || this.nodeList[pid].nextElementSibling.matches('ul') ==false){       //ul 태그가 존재하지않는다면 ...
                let tempUl = document.createElement('ul');
                let tempLi = document.createElement('li');
                tempLi.appendChild(tempElement);
                tempUl.appendChild(tempLi);
                this.nodeList[pid].after(tempUl);       
            }else{                                                              //ul 태그가 있다면 ...                                                 
                let tempLi = document.createElement('li');
                tempLi.appendChild(tempElement);
                this.nodeList[pid].nextElementSibling.appendChild(tempLi);
            }
        }
        this.addCheckBoxButton(tempElement);
        this.addRadioButton(tempElement);                    
        this.nodeIdArray.push(elementData.id);
        this.nodeList[elementData.id] = tempElement; // id, element 쌍으로 객체에 저장
    }

    updateItem(id, elementData){
        let targetElement = document.querySelector('div[data-id="'+id+'"]');
        targetElement.innerText = elementData['NAME'];
        targetElement.nodeData = elementData;
        this.addCheckBoxButton(targetElement);
        this.addRadioButton(targetElement);
    }

    removeItem(id){
        let targetElement = document.querySelector('div[data-id="'+id+'"]');

        if(targetElement.parentElement.matches('tree-component')){ // 최상위 노드일 경우
            return; // 노드 삭제 안함
        }else{
            if(targetElement.parentElement.parentElement.children.length>1){ // 형제 노드가 있는 경우
                console.log('형제 있음')
                targetElement.parentElement.remove();
            }else{ // 형제 노드가 없는 경우
                console.log('형제 없음')
                targetElement.parentElement.parentElement.remove();
            }
        }
    }
    moveItem(id, pid){
        let targetElement = document.querySelector('div[data-id="'+id+'"]');
        let childNodeOfTargetElement = null; // 하위노드가 존재할수도 존재하지 않을 수도 있음
        let targetNextParentElement = document.querySelector('div[data-id="'+pid+'"]'); // 상위 노드가 될 노드
        let liToBeDeleted = targetElement.parentElement;

        if(targetElement.parentElement.matches('tree-component')){// 최상위 노드일 경우
            return; // 이동안함
        }

        if(targetElement.nextElementSibling !=null && targetElement.nextElementSibling.matches('ul')==true){ // 하위노드가 있는지 없는지 확인
            childNodeOfTargetElement = targetElement.nextElementSibling;
        }

        if(targetNextParentElement.nextElementSibling == null || targetNextParentElement.nextElementSibling.matches('ul') == false){// 상위 노드가 될 노드에게 하위 노드가 존재하지 않을 경우
            let tempUl = document.createElement('ul');
            let tempLi = document.createElement('li');
            tempLi.appendChild(targetElement);
            if(childNodeOfTargetElement!=null){             // 하위노드가 존재할 경우 같이 붙임
                tempLi.appendChild(childNodeOfTargetElement);
            }
            tempUl.appendChild(tempLi);
            targetNextParentElement.after(tempUl); 
        }else{
            let tempLi = document.createElement('li');
            tempLi.appendChild(targetElement);
            if(childNodeOfTargetElement!=null){            // 하위노드가 존재할 경우 같이 붙임
                tempLi.appendChild(childNodeOfTargetElement);
            }
            targetNextParentElement.nextElementSibling.appendChild(tempLi);
        }

        liToBeDeleted.remove(); // 기존 위치에서 targetElement를 감싸고 있던 li태그를 제거
    }

    copyItem(id, pid){
        let targetElement = document.querySelector('div[data-id="'+id+'"]');
        let copiedTargetElement = null; // 복사된 노드들의 루트 div
        let childNodeOfTargetElement = null; // 하위노드가 존재할수도 존재하지 않을 수도 있음
        let targetNextParentElement = document.querySelector('div[data-id="'+pid+'"]'); // 상위 노드가 될 노드

        if(targetElement.parentElement.matches('tree-component')){// 최상위 노드일 경우
            return; // 이동안함
        }

        if(targetElement.nextElementSibling !=null && targetElement.nextElementSibling.matches('ul')==true){ // 하위노드가 있는지 없는지 확인
            childNodeOfTargetElement = targetElement.nextElementSibling;
        }

        if(targetNextParentElement.nextElementSibling == null || targetNextParentElement.nextElementSibling.matches('ul') == false){// 상위 노드가 될 노드에게 하위 노드가 존재하지 않을 경우
            let tempUl = document.createElement('ul');
            let tempLi = document.createElement('li');
            copiedTargetElement = targetElement.cloneNode(true);
            copiedTargetElement.nodeData = targetElement.nodeData;  // 복사 시에 element에 담겨져 있는 노드 데이터도 같이 복사함
            tempLi.appendChild(copiedTargetElement);
            if(childNodeOfTargetElement!=null){             // 하위노드가 존재할 경우 같이 붙임
                tempLi.appendChild(childNodeOfTargetElement.cloneNode(true));
            }
            tempUl.appendChild(tempLi.cloneNode(true));
            targetNextParentElement.after(tempUl.cloneNode(true)); 
        }else{
            let tempLi = document.createElement('li');
            copiedTargetElement = targetElement.cloneNode(true);
            copiedTargetElement.nodeData = targetElement.nodeData;  // 복사 시에 element에 담겨져 있는 노드 데이터도 같이 복사함
            tempLi.appendChild(copiedTargetElement);
            if(childNodeOfTargetElement!=null){            // 하위노드가 존재할 경우 같이 붙임
                tempLi.appendChild(childNodeOfTargetElement.cloneNode(true));
            }
            targetNextParentElement.nextElementSibling.appendChild(tempLi.cloneNode(true));
        }
        this._changeDataInCopiedItem(copiedTargetElement);
    }
    // nodeData가 reference로 넘어왔을 수도 있음
    // nodeList 관리?...
    
    _changeDataInCopiedItem(targetElement){ // 복사된 노드들의 id와 pid들을 바꿔주는 함수
        
    }

    _createId(){ // id값 생성해주는..

    }

    addCheckBoxButton(element){
        let tempElement = document.createElement('input');
        tempElement.setAttribute('type', 'checkbox');
        element.prepend(tempElement);                    
    }

    addRadioButton(element){
        let tempElement = document.createElement('input');
        tempElement.setAttribute('type', 'radio');
        tempElement.setAttribute('name', this.dataset.group);
        element.appendChild(tempElement);
    }

}
customElements.define('tree-componenet', tree);