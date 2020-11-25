$(document).ready(function () {
    // Nav mobile initalization
    $('.sidenav').sidenav({
        closeOnClick: true,
        draggable: true,
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

    // Resize window for method and integriends
    $('#recipe_method, #recipe_ingredients').val('');
    M.textareaAutoResize($('#recipe_method, #recipe_ingredients'));

    // Character counter initalization
    $('input#recipe_name,#recipe_cuisine,#recipe_cooking_time,#recipe_size').characterCounter();
});