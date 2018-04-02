$(document).ready(function () {

    $(document).on('click','.arrow-collapse',function () {
       var arrow = $(this);
       var sidebar = $('.sidebar');
       var main = $('main');
        if(arrow.hasClass('in')){
            arrow.removeClass('in');
            sidebar.removeClass('in');
            main.removeClass('col-md-12');
            main.addClass('col-md-10');
        } else{
            arrow.addClass('in');
            sidebar.addClass('in');
            main.addClass('col-md-12');
            main.removeClass('col-md-10');
        }
    });

});