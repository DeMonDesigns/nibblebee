$(document).ready(function () {
    $('.toggle_icon').click(function () {
        $('#toggle_menu').toggleClass('toggle_open');
    });
    $('.prof_img').click(function () {
        $('#toggle_profile').toggleClass('toggle_open');
    });
    $('.search_icon').click(function () {
        $('.toggle_search').toggleClass('fullwidth');
        $('.search_input').toggleClass('fullwidth');
        $('.logo').toggleClass('hide');
        $('.profile').toggleClass('hide');
        $('.search_input').toggleClass('hide');
    });
});
