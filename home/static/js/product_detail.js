$(document).ready(function (){
    $('#show_details').click(function (){
        $('.content_discription').removeClass('visible').addClass('hidden');;
        $("#content_details").removeClass('hidden').addClass('visible');
    })
})
$(document).ready(function (){
    $('#show-description').click(function (){
        $('.content_details').removeClass('visible').addClass('hidden');
        $("#content_discription").removeClass('hidden').addClass('visible');
    })
})

