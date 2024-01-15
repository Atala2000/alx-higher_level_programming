$(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, status) => {
    if (status === 'success') {
      $('#hello').text(data.hello);
    } else {
      console.error('Unsuccesful');
    }
  });
});

// $(document).ready(() => {
//     $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", (data, status) => {
//         if (status === "success" && data && data.hello) {
//             // Update the content of DIV#hello with the translation
//             $("#hello").text(data.hello);
//         } else {
//             console.error("Failed to fetch translation");
//         }
//     });
// });
