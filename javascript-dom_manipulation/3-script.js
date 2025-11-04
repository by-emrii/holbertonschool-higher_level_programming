const toggleHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', () => {
  header.className = header.className === 'red' ? 'green' : 'red';
});
