$(function () {
    $("#submit-btn-list").on("click",function (event) {
        event.preventDefault();
        const $this = $(this);
        const user = $("input[name='user']").val();
        const password = $("input[name='password']").val();
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
    $("#submit-btn-price").on("click",function (event) {
        event.preventDefault();
        const $this = $(this);
        const user = $("input[name='user']").val();
        const password = $("input[name='password']").val();
        $this.off('click');
        $this.attr("disabled",'disabled');
        zyajax.post({
        url:"/getdataprice",
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
    $("#submit-btn-income").on("click",function (event) {
        event.preventDefault();
        const $this = $(this);
        const user = $("input[name='user']").val();
        const password = $("input[name='password']").val();
        const id_ = $("input[name='ID']").val();
        console.log(id_)
        $this.off('click');
        $this.attr("disabled",'disabled');
        zyajax.post({
        url:"/getdataincome",
        data:{user,password,id_},
        success:function (result) {
            if(result['code']===200){
                console.log('ok');
                $this.on('click');
                $this.prop("disabled", false);
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