import { readDatabase } from '../utils.js';

export class StudentsController {
    static async getAllStudents(req, res) {
        const dbName = process.argv[2];
        try {
            const studentsByField = await readDatabase(dbName);
            const responseLines = ['This is the list of our students'];

            Object.keys(studentsByField)
                .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
                .forEach(field => {
                    const names = studentsByField[field];
                    responseLines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
                });

            res.status(200).send(responseLines.join('\n'));
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const dbName = process.argv[2];
        const { major } = req.params;

        if (!['CS', 'SWE'].includes(major)) {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const studentsByField = await readDatabase(dbName);
            const names = studentsByField[major] || [];
            res.status(200).send(`List: ${names.join(', ')}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
