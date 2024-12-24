const topbar = document.querySelector('.top-bar');
const hamburguer = document.querySelector('.hamburguer');

hamburguer?.addEventListener('click', () => {
  topbar?.classList.toggle('active');
});