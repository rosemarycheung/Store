$(document).ready(function() {
  $.get("/all_items", function(data) {
    console.log(data);

    data = JSON.parse(data);

    data.forEach((x) => {
        console.log(x);
      $("#item-list").append(`
                <div class="item">
                    <img class="item-image" src="${x[3]}"/>
                    <div class="item-name">${x[1]}</div>
                    <div class="item-price">$${x[2]}</div>
                </div>
                
            `);
    });
  });
});
