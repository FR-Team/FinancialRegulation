$("#login").on('click',function(){
      $.ajax({
        type: "GET",
        url: "/login",
        dataType: "json",
        data:{
          user: $("#username").val(),
          password: $("#password").value()
        },
        succcess: function(data){
           if(data.succcess){
                alert("Success!");
           }
           else{
              alert("Fail");
           }
        }
        error: function(){
            alert("Network error");
        }
      })
});