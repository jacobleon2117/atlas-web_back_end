const express = require('express');
const app = express();
const port = 7865;

app.use(express.json());

app.get('/', (req, res) => {
    res.status(200).send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    const id = req.params.id;
    if (!isNaN(id)) {
        res.status(200).send(`Payment methods for cart ${id}`);
    } else {
        res.status(404).send('Cart not found');
    }
});

app.post('/login', (req, res) => {
    const { userName } = req.body;
    if (!userName) {
        res.status(400).send('Missing username');
        return;
    }
    res.status(200).send(`Welcome ${userName}`);
});

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});

module.exports = app;