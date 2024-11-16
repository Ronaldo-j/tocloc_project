async function cadastrarUsuario() {
    const nomeUsuario = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = { nomeUsuario, email, password };

    try {
        const response = await fetch('http://127.0.0.1:5000/user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.status === 201) {
            alert(result.message);
        } else {
            alert(`Erro: ${result.error || result.message}`);
        }
    } catch (error) {
        alert('Erro ao conectar com o servidor.');
        console.error(error);
    }
}