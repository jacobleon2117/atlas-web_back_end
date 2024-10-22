const express = require('express');
const app = express();
const port = 7865;

app.use(express.json());

app.get('/', (req, res) => {
    res.status(200).send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    const reMatch = /^\d+$/;
    const id = req.params.id;
    if (id.match(reMatch)) {
        res.status(200).send(`Payment methods for cart ID: ${id}`);
    } else {
        res.status(404).send('Cart not found');
    }
});

app.get('/payment-methods', (req, res) => {
    res.status(200).json({
        paymentMethods: ['Credit Card', 'PayPal', 'Bank Transfer']
    });
});

app.listen(port, () => {
    console.log(`API available on http://localhost:${port}`);
});
