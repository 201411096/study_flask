console.log('tree.js connected ... ')

class Tree extends HTMLElement{
    constructor(){
      console.log('constructor...')
      super();
    }
    connectedCallback(){
      console.log('connectedcallback...');
      this.renderRootData();
      this.render();
      this.setEvent();
    }
    render(){

    }
    setEvent(){

    }

    async createElement(element_data){
      
    }

    async renderRootData(){
      var result = await this.getData('select * from tree_table where pid=0');
      console.log('check in method(getRootData)' + JSON.stringify(result));
      
      

      return result;
    }

    async getData(args_query){
      let response_fetch = await fetch('/raw_sql?query='+args_query);
      let myJson = await response_fetch.json();
      console.log('check myJson in getData : ' + myJson)
      return myJson;
    }

    async editData(args_query){
      let response_fetch = await fetch('/raw_sql_iud?query='+args_query);
      let myJson = await response_fetch.json();
      return myJson;
    }
}

customElements.define('custom-tree', Tree);