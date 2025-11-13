document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = data.hello;
      const div = document.getElementById('hello');
      div.innerHTML= hello;
    })
    .catch(error => console.error('error fetching hello: ', error));
});