"use strict";

var billList = [100, 50, 20, 10, 5, 2, 1];
var billListIncreasing = Array.prototype.slice.call(billList).reverse();

var calcButton = document.getElementById("calcButton");
var resetButton = document.getElementById("resetButton");

// reference to HTML elements, "count", "total", and "subtotal"
function billElem(type, denom) {
  return document.getElementById(type + denom.toString());
}
function reset() {
  billList.forEach(function(bill) {
    billElem("count", bill).innerHTML = "0";
    billElem("total", bill).innerHTML = "0"; 
    billElem("subtotal", bill).innerHTML = "0"; 
    document.getElementById("grandTotal").innerHTML = "0";
    document.getElementById("paymentCount").innerHTML = "0";
  });
}

function getCount(bill) {
  return parseInt(billElem("count", bill).innerHTML, 10);
}

function addTo(bill, amount) {
  billElem("count", bill).innerHTML = getCount(bill) + amount;
}

function countForPayment(payment) {
  billList.forEach(function(bill) {
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
  var grandTotal = 0;

  billListIncreasing.forEach(function(bill) {
    var billId = bill.toString();
    var currentBillTotal = parseInt(billElem("count", billId).innerHTML, 10) * bill;
    billElem("total", billId).innerHTML = currentBillTotal;
    grandTotal += currentBillTotal;

    billElem("subtotal", billId).innerHTML = grandTotal;
  });

  document.getElementById("grandTotal").innerHTML = grandTotal;
}

calcButton.addEventListener("click", function() {
  reset();
  consumeList();
  computeTotals();
});

resetButton.addEventListener("click", function() {
  reset();
  document.getElementById("paymentList").value = "";
});

// set fields to zero 
reset();
