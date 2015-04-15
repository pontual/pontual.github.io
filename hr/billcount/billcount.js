var calcButton = document.getElementById("calcButton");
var resetButton = document.getElementById("resetButton");

var totals = {
  '50': document.getElementById("ct50"),
  '20': document.getElementById("ct20"),
  '10': document.getElementById("ct10"),
  '5': document.getElementById("ct5"),
  '2': document.getElementById("ct2"),
  '1': document.getElementById("ct1"),
};

calcButton.addEventListener("click", function() {
  reset();
  consumeList();
});

resetButton.addEventListener("click", function() {
  reset();
  document.getElementById("paymentList").value = "";
});


function reset() {
  for (bill in totals) {
    totals[bill].innerHTML = "0";
  }
}

function getCount(bill) {
  return parseInt(totals[bill].innerHTML, 10);
}

function addTo(bill, amount) {
  totals[bill].innerHTML = getCount(bill) + amount;
}

function countForPayment(payment) {
  var bills = [50, 20, 10, 5, 2, 1];

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

  paymentList.forEach(function(payment) {
    countForPayment(parseInt(payment, 10));
  });
}
