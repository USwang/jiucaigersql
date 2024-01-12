$(function () {
    $("#submit-btn-list").on("click",function (event) {
        event.preventDefault();
        alert("点击")
        var $this = $(this);
        var user = $("input[name='user']").val();
        var password = $("input[name='password']").val();
        $this.off('click');
        $this.attr("disabled",'disabled');
        zyajax.post({
        url:"/getdatalist",
        data:{user,password},
        success:function (result) {
            if(result['code']===200){
                console.log('ok');
            }else {
                // 如果异常则返回 url:"/getdatalist"返回的的message
                alert(result['message']);
                $this.on('click');
                $this.prop("disabled", false);
            }
        }
        })
    });
});