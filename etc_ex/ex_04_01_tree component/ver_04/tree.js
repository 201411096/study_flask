class Tree extends HTMLElement{
    constructor(){
        super();
    }
    connectedCallback(){
        this.render();
        this.setEvent();
    }
    render(){

    }
    setEvent(){

    }
    setData(){
        
    }
}
customElements.define('custom-tree', Tree);