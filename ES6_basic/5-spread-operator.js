export default function concatArrays(array1, array2, string) {
  const newArr = [...array1, ...array2, ...string];
  return newArr;
}
