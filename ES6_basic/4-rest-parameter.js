export default function returnHowManyArguments(...args) {
  let total = 0;
  for (let i = 0; i < args.length; i += 1) {
    total += 1;
  }
  return total;
}
