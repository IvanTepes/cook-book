$(document).ready(function () {
    $('.sidenav').sidenav();

    /* 
        https://stackoverflow.com/questions/37207668/how-do-i-open-a-materialize-sidenav-on-the-right-instead-of-the-left 
    */
    $('.button-collapse').sidenav({
        closeOnClick: true,
        draggable: true,
        edge: 'right',
      }
    );

});