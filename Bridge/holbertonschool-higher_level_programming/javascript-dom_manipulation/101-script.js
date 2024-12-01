window.onload = () => {
  const translateButton = document.querySelector('#btn_translate');
  const languageSelect = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  // Fonction pour récupérer la traduction de "Hello"
  translateButton.addEventListener('click', async () => {
    const langCode = languageSelect.value;

    // Si une langue est sélectionnée, on fait une requête à l'API
    if (langCode) {
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
      const response = await fetch(url);
      const data = await response.json();

      // On affiche la traduction de "Hello"
      helloDiv.textContent = data.hello;
    } else {
      // Si aucune langue n'est sélectionnée, on efface le message
      helloDiv.textContent = '';
    }
  });
};
