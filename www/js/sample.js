$(function(){
    $('#button').on({
        'click': function() {
            var xhr = new XMLHttpRequest();
            xhr.open( 'POST', 'http://localhost:8080', false );
            xhr.send('{ \"status\": 1 }');
            console.log(xhr.responseText);
            var json = JSON.parse( xhr.responseText ) ;
            alert(json["response"] );
            xhr.abort();
        },
        'mouseenter': function() {
            //$('#button').css("border","solid red");
        },
        'mouseleave': function() {
            //$('#button').css("border","");
        }
      });

});