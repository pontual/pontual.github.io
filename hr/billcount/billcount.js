var calcButton = document.getElementById("calcButton");
var resetButton = document.getElementById("resetButton");

var billCount = {
  '100': document.getElementById("ct100"),
  '50': document.getElementById("ct50"),
  '20': document.getElementById("ct20"),
  '10': document.getElementById("ct10"),
  '5': document.getElementById("ct5"),
  '2': document.getElementById("ct2"),
  '1': document.getElementById("ct1"),
};

var billTotal = {
  '100': document.getElementById("tot100"),
  '50': document.getElementById("tot50"),
  '20': document.getElementById("tot20"),
  '10': document.getElementById("tot10"),
  '5': document.getElementById("tot5"),
  '2': document.getElementById("tot2"),
  '1': document.getElementById("tot1"),
};

calcButton.addEventListener("click", function() {
  reset();
  consumeList();
  computeTotals();
});

resetButton.addEventListener("click", function() {
  reset();
  document.getElementById("paymentList").value = "";
});


function reset() {
  for (bill in billCount) {
    billCount[bill].innerHTML = "0";
    billTotal[bill].innerHTML = "0"; 
    document.getElementById("grandTotal").innerHTML = "0";
    document.getElementById("paymentCount").innerHTML = "0";
  }
}

function getCount(bill) {
  return parseInt(billCount[bill].innerHTML, 10);
}

function addTo(bill, amount) {
  billCount[bill].innerHTML = getCount(bill) + amount;
}

function countForPayment(payment) {
  var bills = [100, 50, 20, 10, 5, 2, 1];

  bills.forEach(function(bill) {
    while (payment >= bill) {
      addTo(bill.toString(), 1)
      payment -= bill;
    }
  });
}

function consumeList() {
  var paymentListStr = document.getElementById("paymentList").value;
  var paymentList = paymentListStr.split("\n");
  var count = 0;
  
  paymentList.forEach(function(paymentStr) {
    var payment = parseInt(paymentStr, 10);
    countForPayment(payment);
    if (paymentStr.trim().length > 0) {
      count++;
    }
  });

  document.getElementById("paymentCount").innerHTML = count;
}

function computeTotals() {
  var bills = [100, 50, 20, 10, 5, 2, 1];
  var grandTotal = 0;

  bills.forEach(function(bill) {
    var billId = bill.toString();
    var currentBillTotal = parseInt(billCount[billId].innerHTML, 10) * bill;
    billTotal[billId].innerHTML = currentBillTotal;
    grandTotal += currentBillTotal;
  });

  document.getElementById("grandTotal").innerHTML = grandTotal;
}
