document.addEventListener('DOMContentLoaded', () => {
    const user = JSON.parse(localStorage.getItem('user'));

    if (user) {
        document.getElementById('login-btn').classList.add('d-none');
        document.getElementById('signup-btn').classList.add('d-none');
        document.getElementById('logout-btn').classList.remove('d-none');
    }
});

function logout() {
    localStorage.removeItem('user');
    window.location.href = 'login.html';
}
