$(function() {

    $(".btn").click(function(e) {
        console.log("create");

        $.ajax({
            type: "POST",
            url: "ajax_send/",
            success: function (response) {
                $(".contant").text("Ajax OK");
            }
        });

        return false;
    });
});