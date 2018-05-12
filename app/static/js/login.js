$("#login").on('click',function(){
      $.ajax({
        type: "GET",
        url: "/login",
        dataType: "json",
        data:{
          user: $("#username").val(),
          password: $("#password").val()
        },
        success: function(data){
           if(JSON.stringify(data))
              alert("Success");
           else
              alert("Fail");

        },
        error: function(){
            alert("Network error");
        }
      })
});