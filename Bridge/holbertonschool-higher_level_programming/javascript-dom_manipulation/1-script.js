// Sélectionne l'élément <header> dans le DOM
const header = document.querySelector('header');

// Sélectionne le bouton ayant l'id "red_header"
const button = document.querySelector('#red_header');

// Ajoute un gestionnaire d'événement "click" au bouton
button.addEventListener('click', () => {
  // Change la couleur du texte de l'élément <header> en rouge (#FF0000) lorsque le bouton est cliqué
  header.style.color = '#FF0000';
});
