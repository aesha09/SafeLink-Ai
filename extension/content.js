chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
  const url = tabs[0].url;
  fetch('https://your-flask-backend-url/scan', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({url})
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'malicious') {
      alert('Warning: This website is potentially malicious!');
    }
  });
});