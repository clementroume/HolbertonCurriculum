// S'assure que le DOM est complètement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
  // Sélectionne l'élément avec l'ID "hello" dans lequel le message sera affiché
  const sayHello = document.querySelector('#hello');

  // Fonction asynchrone pour récupérer et afficher un message "Hello" depuis l'API
  async function getGreeting() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'; // URL de l'API

    try {
      // Envoie une requête GET à l'API
      const res = await fetch(url);

      // Vérifie si la requête a réussi
      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }

      // Convertit la réponse en JSON
      const data = await res.json();

      // Affiche le message "Hello" dans l'élément sélectionné
      sayHello.textContent = data.hello;
    } catch (error) {
      // Gère les erreurs en affichant un message d'erreur dans la console
      console.error('Failed to fetch greeting:', error);
      sayHello.textContent = 'Error loading greeting.';
    }
  }

  // Appelle la fonction pour récupérer et afficher le message
  getGreeting();
});
