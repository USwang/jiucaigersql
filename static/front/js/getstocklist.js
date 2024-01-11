$(function () {
    $("#submit-btn-list").on("click",function (event) {
        event.preventDefault();
        alert("一点击")
        var $this = $(this);
        var user = $("input[name='user']").val();
        var password = $("input[name='password']").val();
        console.log(user);
        if (!user_id || user_id === ""){
            window.location = "/login";
            return;
        }
        var content = $("#comment-textarea").val();
        var post_id = $this.attr("data-post-id");

        zyajax.post({
            url:"/comment",
            data:{content,post_id},
            success:function (result) {
                if(result['code']===200){
                    window.location.reload();
                }else {
                    alert(result['message']);
                }
            }
        })
    });
});