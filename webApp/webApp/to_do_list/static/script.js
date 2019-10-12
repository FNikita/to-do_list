$(function() {

    $(".btn").click(function(e) {
        console.log("create");

        $.ajax({
            type: "POST",
            url: "/add-task/",
            success: function (response) {
                $(".contant").text("Ajax OK");
            }
        });

        return false;
    });
});