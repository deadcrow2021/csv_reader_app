const file_form = document.getElementById('file_form')

file_form.addEventListener('submit', e => {
    e.preventDefault()
    let file = document.getElementById("id_csv_file").files[0]
    console.log(file)

    let formData = new FormData()
    formData.append('file', file)

    fetch('http://127.0.0.1:8000/create/', {
    method: 'POST',
    body: formData
}).then(
    response => response.json()
    ).then(
      success => console.log(success)
      ).catch(
        error => console.log(error)
        );
      })
      
      
let get_data_button = document.getElementById('get_data')
let block = document.getElementById('wrapper')
let table_block = document.getElementById('deals')

get_data_button.addEventListener('click', (e) => {
  e.preventDefault()
  fetch('http://127.0.0.1:8000/deals/', {
    method: 'GET',
  }).then(
    response => response.json()
  ).then(result => {
    console.log(result[0])
    table_block.classList.remove('hide')
    result.forEach(element => {
      table_block.innerHTML += `<tr>
      <td>${element['customer']}</td>
      <td>${element['item']}</td>
      <td>${element['total']}</td>
      <td>${element['quantity']}</td>
      <td>${new Date(element['date']).toLocaleString()}</td>
    </tr>`
    });
  })
})
