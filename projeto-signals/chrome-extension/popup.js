document.getElementById('startBot').addEventListener('click', async () => {
  const currency = document.getElementById('currency').value;
  const response = await fetch(`http://127.0.0.1:5000/start_bot?currency=${currency}`);
  const data = await response.json();
  const signalsList = document.getElementById('signalsList');
  signalsList.innerHTML = '';
  if (data.signals) {
      data.signals.forEach(signal => {
          const listItem = document.createElement('li');
          listItem.textContent = `${signal.tipo} - ${signal.horario}`;
          signalsList.appendChild(listItem);
      });
  } else {
      signalsList.innerHTML = '<li>Erro ao obter sinais</li>';
  }
});
