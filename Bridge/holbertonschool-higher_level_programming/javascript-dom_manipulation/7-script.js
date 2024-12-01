// Sélectionne l'élément avec l'id "list_movies"
const moviesList = document.querySelector('#list_movies');

// Fonction asynchrone pour récupérer et afficher les titres des films
async function getMoviesList() {
  // URL de l'API Star Wars contenant les informations sur les films
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  try {
    // Envoie une requête GET à l'API
    const res = await fetch(url);

    // Vérifie si la requête a réussi
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }

    // Convertit la réponse en JSON
    const data = await res.json();

    // Extrait les titres des films de la réponse
    const titles = data.results.map((film) => film.title);

    // Ajoute chaque titre dans une nouvelle balise <li> dans l'élément <ul>
    titles.forEach((title) => {
      const listItem = document.createElement('li');
      listItem.textContent = title;
      moviesList.appendChild(listItem);
    });
  } catch (error) {
    // Affiche un message d'erreur en cas de problème
    console.error('Failed to fetch movie data:', error);
    moviesList.innerHTML = '<li>Error loading movies.</li>';
  }
}

// Appelle la fonction pour exécuter la logique
getMoviesList();
