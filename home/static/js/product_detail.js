$("#show-description").click(function () {
        $('.content_details').removeClass('visible').addClass('hidden');
        $('.content_reviews').removeClass('visible').addClass('hidden');
        $("#content_discription").removeClass('hidden').addClass('visible');
        $(this).css("border-bottom", "2px solid yellow");

        if ($('#show-details').css("border-bottom", "2px solid yellow")) {
            $('#show-details').css("border-bottom", "1px solid #3b3b3bee");
        }
        if ($('#show-reviews').css("border-bottom", "2px solid yellow")) {
            $('#show-reviews').css("border-bottom", "1px solid #3b3b3bee");
        }
    }
)
$("#show-details").click(function () {

    $('.content_discription').removeClass('visible').addClass('hidden');
    $(".content_details").removeClass('hidden').addClass('visible');
    $('.content_reviews').removeClass('visible').addClass('hidden');

    $(this).css("border-bottom", "2px solid yellow");
    if ($('#show-description').css("border-bottom", "2px solid yellow")) {
        $('#show-description').css("border-bottom", "1px solid #3b3b3bee");
    }
    if ($('#show-reviews').css("border-bottom", "2px solid yellow")) {
        $('#show-reviews').css("border-bottom", "1px solid #3b3b3bee");
    }

})
$("#show-reviews").click(function () {
    $('.content_discription').removeClass('visible').addClass('hidden');
    $('.content_details').removeClass('visible').addClass('hidden');
    $(".content_reviews").removeClass('hidden').addClass('visible');
    $(this).css("border-bottom", "2px solid yellow");
    if ($('#show-description').css("border-bottom", "2px solid yellow")) {
        $('#show-description').css("border-bottom", "1px solid #3b3b3bee");
    }
    if ($('#show-details').css("border-bottom", "2px solid yellow")) {
        $('#show-details').css("border-bottom", "1px solid #3b3b3bee");
    }
})


$(document).ready(function () {
    $(".toggle-more").click(function (event) {
        event.preventDefault();
        var $shortContent = $(this).siblings(".short-content");
        var $moreContent = $(this).siblings(".more-content");

        if ($moreContent.is(":visible")) {
            $(this).text("مطالعه بیشتر");
            $shortContent.show();
            $moreContent.slideUp();
        } else {
            $(this).text("بستن");
            $shortContent.hide();
            $moreContent.slideDown();
        }
    });
});


$('#show-more-colors').click(function () {
    // نمایش تمام رنگ‌های پنهان و پنهان کردن رنگ اول
    $('.color-swatch.hidden').removeClass('hidden');
    $('.color-first').addClass('hidden');
    $('.more-colors-button').addClass('hidden');
    $('#hide-more-colors').removeClass('hidden')

});

$('#hide-more-colors').click(function () {
    // نمایش تمام رنگ‌های پنهان و پنهان کردن رنگ اول
    $('.color-first.hidden').removeClass('hidden');
    $('.color-swatch').addClass('hidden');
    $('.hide-colors-butto').addClass('hidden');
    $('#show-more-colors').removeClass('hidden')
});



