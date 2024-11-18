function logarUsuario() {
    const email = document.querySelector('input[name="email"]').value;
    const password = document.querySelector('input[name="password"]').value;

    axios.post('http://localhost:5000/login', { email, password })
        .then(response => {
            // Armazena informações do usuário no LocalStorage
            localStorage.setItem('user', JSON.stringify(response.data.user));
            // Redireciona para a página inicial
            window.location.href = 'home.html';
        })
        .catch(error => {
            alert(error.response.data.error || "Erro ao realizar login");
        });
}
