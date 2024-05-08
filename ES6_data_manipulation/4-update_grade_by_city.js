export default function updateStudentGradeByCity(arr, city, newGrades) {
    const filteredStudents = arr.filter((student) => student.location === city);
  
    const gradedStudents = filteredStudents.map((student) => {
      const studentGrade = newGrades.filter((grade) => grade.studentId === student.id);
  
      if (studentGrade.length !== 0) {
        Object.assign(student, { grade: studentGrade[0].grade });
      } else {
        Object.assign(student, { grade: 'N/A' });
      }
    return student;
  });
return gradedStudents;
}
