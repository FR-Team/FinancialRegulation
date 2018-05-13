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
          alert(JSON.stringify(data))
//           $("#password").val(JSON.stringify(data)[1])

        },
        error: function(){
            alert("Network error");
        }
      })
});

$("#register").on('click',function(){
      $.ajax({
        type: "GET",
        url: "/register",
        dataType: "json",
        data:{
          user: $("#username").val(),
          password: $("#password").val()
        },
        success: function(data){
          alert(JSON.stringify(data))
        },
        error: function(){
            alert("Network error");
        }
      })
});