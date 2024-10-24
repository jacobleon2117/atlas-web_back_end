const calculateNumber = (type, a, b) => {
    const roundedA = Math.round(a); // Round a to the nearest integer
    const roundedB = Math.round(b); // Round b to the nearest integer

    switch (type) {
        case 'SUM':
            return roundedA + roundedB; // Return the sum of roundedA and roundedB
        case 'SUBTRACT':
            return roundedA - roundedB; // Return the difference
        case 'DIVIDE':
            if (roundedB === 0) {
                return 'Error'; // Handle division by zero
            }
            return Math.round(roundedA / roundedB); // Return the rounded result of the division
        default:
            throw new Error('Invalid operation type'); // Handle invalid operation type
    }
};

module.exports = calculateNumber;
