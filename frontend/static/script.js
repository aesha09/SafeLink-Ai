fetch('http://localhost:5000/history')
  .then(res => res.json())
  .then(data => {
    let table = "<tr><th>URL</th><th>Result</th><th>Date</th></tr>";
    data.forEach(row => {
      table += `<tr><td>${row[0]}</td><td>${row[1]}</td><td>${row[2]}</td></tr>`;
    });
    document.getElementById("history-table").innerHTML = table;
  });