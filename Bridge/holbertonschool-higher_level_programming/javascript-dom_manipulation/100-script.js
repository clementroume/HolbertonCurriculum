window.onload = function () {
  const addItemButton = document.querySelector('#add_item');
  const removeItemButton = document.querySelector('#remove_item');
  const clearListButton = document.querySelector('#clear_list');
  const list = document.querySelector('.my_list');

  // Ajouter un item
  addItemButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });

  // Retirer le dernier item
  removeItemButton.addEventListener('click', () => {
    const lastItem = list.lastElementChild;
    if (lastItem) {
      list.removeChild(lastItem);
    }
  });

  // Effacer toute la liste
  clearListButton.addEventListener('click', () => {
    list.innerHTML = '';
  });
};
