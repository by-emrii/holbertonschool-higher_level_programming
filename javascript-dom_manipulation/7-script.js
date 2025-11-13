fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    const list = document.getElementById('list_movies');

    // use loop through each movie and append to title as li
    movies.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      list.appendChild(li);
    });
  })
  .catch(error => console.error('error fetching movies: ', error));
