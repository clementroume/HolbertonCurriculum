// Sélectionne l'élément de liste avec la classe "my_list"
const list = document.querySelector('.my_list');

// Sélectionne le bouton avec l'id "add_item"
const button = document.querySelector('#add_item');

// Ajoute un gestionnaire d'événement "click" au bouton
button.addEventListener('click', () => {
  // Ajoute un nouvel élément <li> à la liste
  list.innerHTML += `<li>Item</li>`;
});
