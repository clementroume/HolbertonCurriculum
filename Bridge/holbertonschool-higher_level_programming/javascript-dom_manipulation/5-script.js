// Sélectionne l'élément <header>
const header = document.querySelector('header');

// Sélectionne le bouton avec l'id "update_header"
const button = document.querySelector('#update_header');

// Ajoute un gestionnaire d'événements "click" au bouton
button.addEventListener('click', () => {
  // Modifie le contenu texte de l'élément <header>
  header.textContent = 'New Header!!!';
});
