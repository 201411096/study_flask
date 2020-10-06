document.getElementById('button1').addEventListener('click', function(e){
    console.log('button1 ... clickEvent');
    let query = 'select * from tree_table'
    fetch('/raw_sql?query='+query)
    .then(function(response){
      return response.json()
    })
    .then(function (myJson){
      console.log(JSON.stringify(myJson));
    });
  });
  document.getElementById('button2').addEventListener('click', function(e){
    console.log('button2 ... clickEvent');
    let query = 'insert into tree_table values(11,2, "node9", "ex_des")'
    fetch('/raw_sql_iud?query='+query)
    .then(function(response){
      return response.json()
    })
    .then(function (myJson){
      console.log('button2 ajax complete ...');
    });
  });