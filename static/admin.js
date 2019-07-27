$(document).ready(function() {
  $.get("/all_items", function(data) {
    console.log(data);

    data = JSON.parse(data);

    data.forEach(x => {
      $("#item-list").append(`
                <div>
                    <div>Item Name: ${x[1]}</div>
                    <div>Item Price: ${x[2]}</div>
                    <div data-itemid=${x[0]} id="del-${
        x[0]
      }" class="del-items">Delete</div>
                </div>
            `);
    });
  });

  $(document).on("click", ".del-items", function(e) {
      console.log('clicked!');
    var itemId = $(this).data("itemid");
    console.log(itemId);
    $.post("/delete_item", { itemId: itemId }, function(data) {
        $(this).parent().html("");
    });
  });

  $("#new-item-button").click(function(e) {
    e.preventDefault();
    var itemName = $("#item-name").val();
    var itemPrice = $("#item-price").val();
    $.post("/new_item", { itemName: itemName, itemPrice: itemPrice }, function(
      data
    ) {
      $("#item-list").append(`
                <div>
                    <div class="item-name">${itemName}</div>
                    <div class="item-price">${itemPrice}</div>
                </div>
            `);
    });
  });
});
