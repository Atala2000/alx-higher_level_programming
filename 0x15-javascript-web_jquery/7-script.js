$(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
    if (status == 'success') {
      $('#character').text(data.name);
    } else {
      console.error('Failed to fetch');
    }
  });
});
