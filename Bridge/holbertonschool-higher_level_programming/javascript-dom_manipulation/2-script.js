// Sélectionne l'élément <header> dans le DOM
const header = document.querySelector('header');

// Sélectionne le bouton ayant l'id "red_header"
const button = document.querySelector('#red_header');

// Ajoute un gestionnaire d'événement "click" au bouton
button.addEventListener('click', () => {
  // Ajoute la classe CSS "red" à l'élément <header> lorsqu'on clique sur le bouton
  header.classList.add('red');
});
