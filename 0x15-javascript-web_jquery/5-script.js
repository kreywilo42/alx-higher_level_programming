///JQuery API that adds an <li> to <ul> on click
$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
});