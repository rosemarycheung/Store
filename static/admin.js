$(document).ready(function() {
  $.get("/all_items", function(data) {
    console.log(data);

    data = JSON.parse(data);

    data.forEach(x => {
      $("#item-list").append(`
                <div>
                    <div>Item Name: ${x[1]}</div>
                    <div>Item Price: ${x[2]}</div>
                    <img src="${x[3]}" style="max-height: 100px; max-width: 100px;"/>
                    <button data-itemid=${x[0]} id="del-${
        x[0]
      }" class="del-items">Delete</button>
                </div>
            `);
    });
  });

  $(document).on("click", ".del-items", function(e) {
    console.log("clicked!");
    var itemId = $(this).data("itemid");
    console.log(itemId);
    var context = $(this);
    $.post("/delete_item", { itemId: itemId }, function(data) {
      context.parent().html("");
    });
  });

  $("#new-item-button").click(function(e) {
    e.preventDefault();
    var itemName = $("#item-name").val();
    var itemPrice = $("#item-price").val();
    var form_data = new FormData($("#new-item")[0]);
    form_data.append("itemName", itemName);
    form_data.append("itemPrice", itemPrice);
    console.log(form_data);
    $.ajax({
      type: "POST",
      url: "/new_item",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      success: function(data) {
        $("#item-list").append(`
          <div>
              <div class="item-name">Item Name: ${itemName}</div>
              <div class="item-price">Item Price: ${itemPrice}</div>
              <button data-itemid=${data} id="del-${data}" class="del-items">Delete</button>
                        </div>
          </div>
      `);
      }
    });
  });
});
