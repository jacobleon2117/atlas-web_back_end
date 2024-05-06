export default function createEmployeesObject(departmentName, employees) {
  const employeeObj = {
    [departmentName]: [...employees],
  };
  return employeeObj;
}
