const eye = document.getElementById('eye');
const passwordInput = document.getElementById('password');

eye.addEventListener('click', () => {
  const currentType = passwordInput.type;

  if (currentType == 'password') {
    passwordInput.type = 'text';
    eye.src = 'assets/eye.svg';
  } else {
    passwordInput.type = 'password';
    eye.src = 'assets/eye-closed.svg';
  }
});
