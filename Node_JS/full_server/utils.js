import fs from 'fs/promises';

export const readDatabase = async (filePath) => {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.trim().split('\n').filter(line => line.trim() !== '');

        const studentsByField = {};
        lines.slice(1).forEach(line => {
            const [firstName, , , field] = line.split(',');
            if (field) {
                if (!studentsByField[field]) {
                    studentsByField[field] = [];
                }
                studentsByField[field].push(firstName);
            }
        });

        return studentsByField;
    } catch (error) {
        throw new Error(error);
    }
};
