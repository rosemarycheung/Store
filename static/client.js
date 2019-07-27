$(document).ready(function() {
  $.get("/all_items", function(data) {
    console.log(data);

    data = JSON.parse(data);

    data.forEach(x => {
      $("#item-list").append(`
                <div>
                    <div>Item Name: ${x[1]}</div>
                    <div>Item Price: ${x[2]}</div>
                </div>
            `);
    });
  });
});
