const abrirModal = (elementoModal) => {
  const modalFechar = elementoModal.querySelector('.modal-fechar');

  elementoModal.style.display = 'flex';
  const eventoFechar = modalFechar.addEventListener('click', () => {
    modalFechar.removeEventListener('click', eventoFechar);

    elementoModal.style.display = 'none';
  });
};

document.querySelectorAll('.nota').forEach((item) => {
  item.addEventListener('click', () => {
    const elementoModal = item.parentElement.querySelector('.modal');

    abrirModal(elementoModal);
  });
});
