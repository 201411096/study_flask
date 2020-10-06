console.log('tree.js connected ... ')

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

    getRootData(){
        this.getData()
    }

    getData(args_query){
        fetch('/raw_sql?query='+args_query)
        .then(function(response){
          return response.json()
        })
        .then(function (myJson){
          console.log('check in getData ...' + JSON.stringify(myJson));
        });
    }
    editData(args_query){
        fetch('/raw_sql_iud?query='+args_query)
        .then(function(response){
          return response.json()
        })
        .then(function (myJson){
          console.log('editData ajax complete ...');
        });
    }
}

customElements.define('custom-tree', Tree);