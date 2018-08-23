function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajaxLogin(){

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", document.getElementsByName("csrfmiddlewaretoken")[0].value);
          }
    }
    });
    var csrfmiddlewaretoken=document.getElementsByName("csrfmiddlewaretoken")[0].value
    var input1 = document.getElementById("input1").value;
    var day2 = new Date(Date.parse(input1+":59".replace(/-/g,"/")));
    var day1 = new Date();
    var dateDiff = day2.getTime() - day1.getTime();//时间差的毫秒数
    var dayDiff = Math.floor(dateDiff / (24 * 3600 * 1000));//计算出相差天数
    if (dayDiff >= 1){
        $.ajax({
            url: "regist",
            type: "POST",
           data: {
            //    csrfmiddlewaretoken:csrfmiddlewaretoken,
               input1:input1},
            dataType: "json",
            success: function(data) {
                rec = data['rec'];
                if(rec==1){
                    var json = {
						title:"选择",
						msg:"是否跳转到倒计时界面?",
						buttons:[
							{ 
                                title:"Call",color:"red",click:function(){
                            } 
                            },
							{ 
                                title:"OK",click:function(){
                                    window.location.href='time';
                                } 
                            }
						]
					}
                    $.alertView(json);
                }
           }
        });
    }else{
        $.alertView("最少要比现在多一天以上");
    }
    
}
