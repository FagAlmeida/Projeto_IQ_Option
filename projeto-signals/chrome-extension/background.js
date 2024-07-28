chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'startBot') {
      fetch('http://127.0.0.1:5000/start_bot')
          .then(response => response.json())
          .then(data => {
              console.log('Bot started:', data);
          })
          .catch(error => {
              console.error('Error starting bot:', error);
          });
  }
});
