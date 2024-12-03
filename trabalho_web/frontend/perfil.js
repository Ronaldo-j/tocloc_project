// Função para buscar e exibir o nome do usuário após o login
function buscarUsuarioLogado() {
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: 'usuario@exemplo.com',  // Aqui você pode pegar dinamicamente o email do usuário logado
            password: 'senhaSegura'        // E a senha do usuário (não é o ideal passar a senha dessa forma, mas para o exemplo está OK)
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Verifique o que está sendo retornado
        if (data.user) {
            document.getElementById('nomeUsuario').innerText = data.user.nomeUsuario;
        } else {
            alert('Usuário não encontrado ou credenciais incorretas');
        }
    })
    .catch(error => {
        console.error('Erro ao buscar usuário:', error);
    });
}

// Chamar a função ao carregar a página
window.onload = buscarUsuarioLogado;
