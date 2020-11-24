$(document).ready(function () {
    $('.sidenav').sidenav({
        closeOnClick: true,
        draggable: true,
        edge: 'right',
    });

    $('.parallax').parallax();
    $('.tabs').tabs();
    $(".dropdown-trigger").dropdown();
});