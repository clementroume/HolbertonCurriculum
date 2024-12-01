// Sélectionne l'élément <header> dans le DOM
const header = document.querySelector('header');

// Sélectionne le bouton ayant l'id "toggle_header"
const button = document.querySelector('#toggle_header');

// Ajoute un gestionnaire d'événement "click" au bouton
button.addEventListener('click', () => {
  // Bascule entre les classes "green" et "red" pour l'élément <header>
  header.classList.toggle('green'); // Ajoute ou enlève "green"
  header.classList.toggle('red'); // Ajoute ou enlève "red"
});
