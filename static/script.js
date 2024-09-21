function handleOrderAction(orderType, tableId){
    console.log("${orderType} button clicked");

    const data = { 
        "order_type" : orderType,
        "quantity" : 10,
        "price" : 100
    }

    fetch("/add_order",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert("Order added successfully");
        console.log("Success:", data);

        updateTable(tableId, data[`${orderType.toLowerCase()}_orders`]); // quite shite i must say
    })
    .catch((error) => {
        console.error("Error:", error);
    });

}

function handleBuyAction(){ handleOrderAction("Buy", "buy-table"); }

function handleSellAction(){ handleOrderAction("Sell", "sell-table"); } 

function updateTable(tableId, orders){
    const tableBody = document.querySelector(`#${tableId} tbody`);
    tableBody.innerHTML = "";

    console.log(Object.values(orders));

    Object.values(orders).forEach(order => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${order["ID"]}</td>
            <td>${order["Date"]}</td>
            <td>${order["Price"]}</td>
            <td>${order["Quantity"]}</td>`;
        tableBody.appendChild(row);
    });
}