$(document).ready(function() {
    const colors = [
        'rgb(255 ,104 ,195,  0.12)',
        'rgb(106,119,182,0.12)',
        'rgb(33 ,33, 33 , 12%)',
        'rgb(133, 223, 210 , 0.12)',
        'rgba(255, 228 ,33 , 12%)'
    ];

    $('.item').each(function() {
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        $(this).find('.overlay').css('background-color', randomColor);
    });
});