$(function () {
    //Json data by api call for order table
    $.get(orderListApiUrl, function (response) {
        if(Array.isArray(response)){
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, order) {
                totalCost += parseFloat(order.totalCost); // Ensure 'totalCost' is correct
                table += '<tr>' +
                    '<td>'+ order.date +'</td>' +
                    '<td>'+ order.orderNo +'</td>' +
                    '<td>'+ order.customerName +'</td>' +
                    '<td>'+ order.totalCost.toFixed(2) +' Rs</td></tr>'; // Ensure 'totalCost' is correct

            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Rs</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});