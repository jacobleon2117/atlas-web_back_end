const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`total is: ${total}`);
    return total;
}

module.exports = sendPaymentRequestToApi;