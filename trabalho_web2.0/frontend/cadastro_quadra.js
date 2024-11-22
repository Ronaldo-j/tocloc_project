document.getElementById("formCadastroQuadra").addEventListener("submit", function(event) {
    event.preventDefault();

    // Coleta os dados do formulário
    const nomeQuadra = document.getElementById("nomeQuadra").value;
    const precoQuadra = document.getElementById("precoQuadra").value;
    const localizacaoQuadra = document.getElementById("localizacaoQuadra").value;
    const descricaoQuadra = document.getElementById("descricaoQuadra").value;

    // Objeto com os dados
    const dados = {
        nomeQuadra: nomeQuadra,
        preco: precoQuadra,
        localizacao: localizacaoQuadra,
        descricao: descricaoQuadra
    };

    // Envio para o backend
    fetch("http://localhost:5000/quadra", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        // Exibe mensagem de sucesso ou erro
        const mensagemDiv = document.getElementById("mensagem");
        if (response.ok) {
            mensagemDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
            document.getElementById("formCadastroQuadra").reset(); // Limpa o formulário
        } else {
            mensagemDiv.innerHTML = `<div class="alert alert-danger">Erro: ${data.error}</div>`;
        }
    })
    .catch(error => {
        const mensagemDiv = document.getElementById("mensagem");
        mensagemDiv.innerHTML = `<div class="alert alert-danger">Erro: ${error.message}</div>`;
    });
});