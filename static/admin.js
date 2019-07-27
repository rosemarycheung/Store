$( document ).ready(function() {
    $.get('/all_items', function(data) {
        console.log(data);

        data = JSON.parse(data);

        data.forEach((x) => {
            $('#item-list').append(`
                <div>
                    <div>Item Name: ${x[1]}</div>
                    <div>Item Price: ${x[2]}</div>
                </div>
            `);
        });

    });

    $('#new-item-button').click(function(e) {
        e.preventDefault();
        var itemName = $('#item-name').val();
        var itemPrice = $('#item-price').val();
        $.post('/new_item', {itemName: itemName, itemPrice: itemPrice}, function(data) {
            $('#item-list').append(`
                <div>
                    <div class="item-name">${itemName}</div>
                    <div class="item-price">${itemPrice}</div>
                </div>
            `);
        });
    });
});
