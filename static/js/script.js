$(document).ready(function () {
    // Nav mobile initalization
    $('.sidenav').sidenav({
        /* closeOnClick: true,
        draggable: false, */
        edge: 'right',
    });

    // Parallax initalization
    $('.parallax').parallax();

    // Login and Register tabs
    $('.tabs').tabs();

    // Dropdown triger for nav bar
    $(".dropdown-trigger").dropdown();

    // Select dropdown initalization
    $('select').formSelect();

    // Character counter initalization
    $('input#recipe_name,#recipe_cuisine,#recipe_cooking_time,#recipe_prep_time,         #recipe_ingredients,#recipe_method,#recipe_image').characterCounter();

    /* 
        Dropdown menus validation
        Check if user select any option 
        Code copied from Code Institute lesson
        https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js

    */

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

});