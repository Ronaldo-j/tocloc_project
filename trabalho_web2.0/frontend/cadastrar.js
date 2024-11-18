async function cadastrarUsuario() {
    const nomeUsuario = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = { nomeUsuario, email, password };

    try {
        const response = await axios.post('http://127.0.0.1:5000/user', data);

        if (response.status === 201) {
            alert(response.data.message);
        } else {
            alert(`Erro: ${response.data.error || response.data.message}`);
        }
    } catch (error) {
        if (error.response) {
            // Erros de resposta do servidor
            alert(`Erro: ${error.response.data.error || error.response.data.message}`);
            console.error("Erro de resposta:", error.response.data);
        } else if (error.request) {
            // Erros na requisição (nenhuma resposta do servidor)
            alert("Erro: O servidor não respondeu.");
            console.error("Erro na requisição:", error.request);
        } else {
            // Outros erros
            alert("Erro ao conectar com o servidor.");
            console.error("Erro:", error.message);
        }
    }
}
