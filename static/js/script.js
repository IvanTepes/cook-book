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
    $('#recipe-method, #recipe-ingredients').val('');
    M.textareaAutoResize($('#recipe-method, #recipe-ingredients'));

    // Character counter initalization
    $('input#recipe-name,#recipe-cuisine,#recipe-time,#recipe-size, textarea#textarea2').characterCounter();
});