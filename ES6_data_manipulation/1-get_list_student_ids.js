export default function getListStudentIds(arr) {
  if (Array.isArray(arr)) {
    return arr.map((res) => res.id);
  }
  return [];
}
