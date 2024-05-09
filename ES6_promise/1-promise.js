export default function getFullResponseFromAPI(bool) {
    const response = new Promise((res, rej) => {
      if (bool === true) {
        res({
          status: 200,
          body: 'Success',
        });
      } else {
        rej(new Error('The fake API is not working currently'));
      }
    });
 return response;
}
