// Sélectionne l'élément avec l'id "character"
const character = document.querySelector('#character');

// Fonction asynchrone pour récupérer et afficher le nom du personnage
async function getCharacterName() {
  // URL de l'API Star Wars contenant les informations sur le personnage
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  try {
    // Envoie une requête GET à l'API
    const res = await fetch(url);

    // Vérifie si la requête a réussi
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }

    // Convertit la réponse en JSON
    const data = await res.json();

    // Ajoute le nom du personnage à l'élément sélectionné
    character.innerText += data.name;
  } catch (error) {
    // Affiche un message d'erreur en cas de problème
    console.error('Failed to fetch character data:', error);
    character.innerText = 'Error loading character name.';
  }
}

// Appelle la fonction pour exécuter la logique
getCharacterName();
