$(function() {
    var old_text, val_id, col_btn;
    var col_item_on_page = 7;
    var page_active = Math.ceil($("li").length / col_item_on_page)-1;

    function ajax_Send(new_url, new_data) {
        $.ajax({
            type: "POST",
            url: new_url,
            data: new_data,
            success: function (response) {
                
            }
        });
    }

    function add_task() {
        text = $("#text_input").val();
        if(text.trim() != "") {
            $("#text_input").val("");

            $.ajax({
            type: "GET",
            url: "/to_do_list/ajax-req/",
            data: {
                action: "add-task",
                text: text
            },
            success: function(data_res) {
                $("ul").append(
                `<li id="${data_res.id}">
                        <input class="done" type="checkbox"> 
                        <span class="li-item">${data_res.text}</span>                             
                        <button class="btn delete-btn"><i class="fa fa-trash trash"></i></button> 
                </li>`);

                count_task();
                paginationRender($("#select-type option:selected").val());
                if (page_active * col_item_on_page < col_btn * col_item_on_page) {
                    page_active = col_btn;
                } 
                display($("#select-type option:selected").val(), page_active);

                $(".delete-btn").click(function() {
                    val_id = $(this).parent().attr('id');
                    $(this).parent().remove();
                    count_task();
                    paginationRender($("#select-type option:selected").val());
                    if (page_active * col_item_on_page >= col_btn * col_item_on_page) {
                        page_active = col_btn;
                    }
                    display($("#select-type option:selected").val(), page_active);
                    ajax_Send("/to_do_list/ajax-req/", {action: "del", id: val_id});
                });
                
                $(".done").change( function() {
                    val_chek = $(this).is(":checked");
                    val_id = $(this).parent().attr('id');

                    if ($(this).is(":checked")) {
                        $(this).parent().children('span').addClass("complate");
                    } else {
                        $(this).parent().children('span').removeClass("complate");
                    }
                    count_task();
                    paginationRender($("#select-type option:selected").val());
                    display($("#select-type option:selected").val(), page_active);
                    ajax_Send("/to_do_list/ajax-req/", {action: "change_one", chek: val_chek, id: val_id});
                });
            }});

            if (page_active * col_item_on_page <= col_btn * col_item_on_page) {
                page_active++;
            }
            if ($("li").length == 0) {
                page_active = 0;
            }
        return false;
        }
    }

    function count_task() {
        let all_task = $("li").length;
        let complete_task = $(".done:checked").length;
        if(all_task === 0) {
            $("#all-task-count").text("0");
            $("#complate-task-count").text("0");
        } else {
            $("#all-task-count").text(all_task);
            $("#complate-task-count").text(complete_task);
        }
    }

    function display(type, page) {
        $("li").hide();
        if (col_btn < page && page != 0) {
            page--;
        }
        if (type == "all") {
                $("li").slice((page)*col_item_on_page, page*col_item_on_page + col_item_on_page ).show();
        } else if (type == "active")
            $(".done:not(:checked)").parent().slice((page)*col_item_on_page, page*col_item_on_page + col_item_on_page).show(); 
        else {
            $(".done:checked").parent().slice((page)*col_item_on_page, page*col_item_on_page + col_item_on_page).show();
            }
        }

    function renderBtn(col_batton) {
        i = 0;
        div_pagination = $("#pagination");
        str = '';
        if (col_batton > 0) {
            while (i <= col_batton) {
                str += `<button class='page' id='${i}'> ${i+1} </button>`;
                i += 1;
            }
        }
        div_pagination.html(str);
    }

    function paginationRender(type) {
        if (type=="all") {
            col_btn = Math.ceil($("li").length / col_item_on_page);
            if (col_btn * col_item_on_page < $("li").length ) {
                renderBtn(col_btn);
            } else {
                col_btn--;
                renderBtn(col_btn);
            }
        } else if(type == "active") {
            col_btn = Math.ceil($(".done:not(:checked)").parent().length / col_item_on_page);
            if (col_btn * col_item_on_page < $(".done:not(:checked)").parent().length)
                renderBtn(col_btn);
            else {
                col_btn--;
                renderBtn(col_btn);
            }
        } else if(type=="done") {
            col_btn = Math.ceil($(".done:checked").parent().length / col_item_on_page);
            if (col_btn * col_item_on_page < $(".done:checked").parent().length)
            renderBtn(col_btn);
            else {
                col_btn--;
                renderBtn(col_btn);
            }
        }
    }

    $(document).on("click", ".page", function() {
        display($("#select-type option:selected").val(), $(this).attr('id'));
        page_active = $(this).attr('id');
    });

    $(".done").change( function() {
        val_chek = $(this).is(":checked");
        val_id = $(this).parent().attr('id');

        if ($(this).is(":checked")) {
            $(this).parent().children('span').addClass("complate");
        } else {
            $(this).parent().children('span').removeClass("complate");
        }
        count_task();
        paginationRender($("#select-type option:selected").val());
        if (page_active * col_item_on_page >= col_btn * col_item_on_page) {
            page_active = col_btn;
        }
        display($("#select-type option:selected").val(), page_active);
        ajax_Send("/to_do_list/ajax-req/", {action: "change_one", chek: val_chek, id: val_id});
    });

    $("#check-all").change( function() {
        chech_all = $("#check-all").is(":checked");
        if(chech_all) {
            $(".done")
                .prop('checked', true)
                .parent()
                .children('span')
                .addClass("complate");
        } else {
            $(".done")
            .prop('checked', false)
            .parent()
            .children('span')
            .removeClass("complate");
        }
        count_task();
        paginationRender($("#select-type option:selected").val());
        display($("#select-type option:selected").val(), page_active);
        ajax_Send("/to_do_list/ajax-req/", {action: "change_all", chek: chech_all});
    });


    $(".delete-btn").click(function() {
        val_id = $(this).parent().attr('id');
        $(this).parent().remove();
        count_task();
        paginationRender($("#select-type option:selected").val());
        if (page_active * col_item_on_page < col_btn * col_item_on_page) {
            page_active = col_btn;
        }
        display($("#select-type option:selected").val(), page_active);
        ajax_Send("/to_do_list/ajax-req/", {action: "del", id: val_id});
    });

    $(".delete-btn-all").click(function() {
        chech_all = $("#check-all").is(":checked");
        $(".done:checked").parent().remove();
        count_task();
        ajax_Send("/to_do_list/ajax-req/", {action: "del-all", id: chech_all});
        paginationRender($("#select-type option:selected").val());
        display($("#select-type option:selected").val(), page_active);
    });

    $('.li-item').dblclick(function () { 
        val_id = $(this).parent().attr('id');
        old_text = $(this).text();
        edit = true;
        $(this).attr('contenteditable', true);
        $(this).focus();

        $(this).bind('keydown', function(e) { 
            if(e.keyCode==27 && edit){
                e.preventDefault();
                $(this).text(old_text);
            }
        });

        $(this).bind('keydown', function(e) {
            if(e.keyCode === 13) {
                $(this).blur();
            }
        });
    });

    $('.li-item').blur( function () {
        if ($(this).text() == "") {
            $(this).text(old_text);
        } else {
            ajax_Send('/to_do_list/ajax-req/', {action: 'edit-task', id: val_id ,text: $(this).text().trim()});
        }
        $(this).attr('contenteditable', false);
    });

    $("#select-type").change( function() {
        page_active = 0;
        paginationRender($("#select-type option:selected").val());
        display($("#select-type option:selected").val(), page_active);
    });

    $(document).on("click", ".submit-btn", function() {
        new_text = add_task();
        if (new_text) {
            ajax_Send("/to_do_list/ajax-req/", {action: "add-item", text: new_text});
        }
    });

    $("#text_input").keydown(function(e) {
        if(e.keyCode===13) {
            new_text = add_task();
            if (new_text) {
                ajax_Send("/to_do_list/ajax-req/", {action: "add-item", text: new_text});
            }
        }
    });

    count_task();
    paginationRender($("#select-type option:selected").val());
    display($("#select-type option:selected").val(), page_active);
});