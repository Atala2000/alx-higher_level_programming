$(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, status) => {
    if (status === 'success') {
      // Assuming data.results is an array containing movie objects
      // Select the UL#list_movies element and append list items for each movie title
      $.each(data.results, (i, movie) => {
        $('#list_movies').append(`<li>${movie.title}</li>`);
      });
    }
  });
});
