document.getElementById("formCadastroQuadra").addEventListener("submit", function(event) {
    event.preventDefault();

    // Coleta os dados do formulário
    const id = this.dataset.quadraId; // Obtém o ID da quadra sendo editada
    const nomeQuadra = document.getElementById("nomeQuadra").value;
    const precoQuadra = document.getElementById("precoQuadra").value;
    const localizacaoQuadra = document.getElementById("localizacaoQuadra").value;
    const descricaoQuadra = document.getElementById("descricaoQuadra").value;
    const dadosQuadra = { nomeQuadra, preco: precoQuadra, localizacao: localizacaoQuadra, descricao: descricaoQuadra };
    if (id) {
        // Atualiza quadra existente
        fetch(`http://localhost:5000/quadra/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dadosQuadra)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || "Quadra atualizada com sucesso!");
            this.reset();
            delete this.dataset.quadraId; // Remove o ID após a atualização
            carregarQuadras();
        })
        .catch(error => console.error("Erro ao atualizar quadra:", error));
    } else {
        // FormData para suportar o envio de arquivos
        const formData = new FormData();
        formData.append("nomeQuadra", nomeQuadra);
        formData.append("preco", precoQuadra);
        formData.append("localizacao", localizacaoQuadra);
        formData.append("descricao", descricaoQuadra);

        // Adiciona o arquivo ao FormData
        const fotoQuadra = document.getElementById("fotoQuadra").files[0];
        if (fotoQuadra) {
            formData.append("foto", fotoQuadra);
        }

        // Envio para o backend
        fetch("http://localhost:5000/quadra", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const mensagemDiv = document.getElementById("mensagem");
            if (data.error) {
                mensagemDiv.innerHTML = `<div class="alert alert-danger">Erro: ${data.error}</div>`;
            } else {
                mensagemDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
                document.getElementById("formCadastroQuadra").reset(); // Limpa o formulário
            }
        })
        .catch(error => {
            const mensagemDiv = document.getElementById("mensagem");
            mensagemDiv.innerHTML = `<div class="alert alert-danger">Erro: ${error.message}</div>`;
        });
    }
    
});
function deletarQuadra(id) {
    if (confirm("Tem certeza de que deseja deletar esta quadra?")) {
        fetch(`http://localhost:5000/quadra/${id}`, {
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(`Erro: ${data.error}`);
            } else {
                alert(data.message);
                carregarQuadras(); // Atualiza a tabela
            }
        })
        .catch(error => console.error("Erro ao deletar quadra:", error));
    }
}

// Carregar quadras ao carregar a página
function carregarQuadras() {
    fetch("http://localhost:5000/quadra")
        .then(response => response.json())
        .then(quadras => {
            const tbody = document.querySelector("#quadraTable tbody");
            tbody.innerHTML = ""; // Limpa a tabela

            quadras.forEach(quadra => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${quadra.nomeQuadra}</td>
                    <td>${quadra.preco}</td>
                    <td>${quadra.localizacao}</td>
                    <td>${quadra.descricao}</td>
                    <td>
                        <button class="btn btn-warning btn-sm" onclick="abrirModalEdicao(${quadra.id})">Editar</button>
                        <button class="btn btn-danger btn-sm" onclick="deletarQuadra(${quadra.id})">Deletar</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error("Erro ao carregar quadras:", error));
}

// Abrir modal de edição com informações da quadra
function abrirModalEdicao(id) {
    fetch(`http://localhost:5000/quadra/${id}`)
        .then(response => response.json())
        .then(quadra => {
            document.getElementById("editQuadraId").value = id;
            document.getElementById("editNomeQuadra").value = quadra.nomeQuadra;
            document.getElementById("editPrecoQuadra").value = quadra.preco;
            document.getElementById("editLocalizacaoQuadra").value = quadra.localizacao;
            document.getElementById("editDescricaoQuadra").value = quadra.descricao;
            new bootstrap.Modal(document.getElementById("editModal")).show();
        })
        .catch(error => console.error("Erro ao carregar quadra para edição:", error));
}

// Salvar alterações
document.getElementById("btnSalvarEdicao").addEventListener("click", function () {
    const id = document.getElementById("editQuadraId").value;
    const nomeQuadra = document.getElementById("editNomeQuadra").value;
    const preco = document.getElementById("editPrecoQuadra").value;
    const localizacao = document.getElementById("editLocalizacaoQuadra").value;
    const descricao = document.getElementById("editDescricaoQuadra").value;

    fetch(`http://localhost:5000/quadra/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nomeQuadra, preco, localizacao, descricao })
    })
        .then(response => response.json())
        .then(data => {
            const mensagemDiv = document.getElementById("mensagem");
            if (data.error) {
                mensagemDiv.innerHTML = `<div class="alert alert-danger">Erro: ${data.error}</div>`;
            } else {
                mensagemDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
                carregarQuadras(); // Atualiza a tabela
                bootstrap.Modal.getInstance(document.getElementById("editModal")).hide();
            }
        })
        .catch(error => console.error("Erro ao salvar alterações:", error));
});

// Inicializar carregamento de quadras
carregarQuadras();
function editarQuadra(id) {
    fetch(`http://localhost:5000/quadra/${id}`, { method: "GET" })
        .then(response => response.json())
        .then(quadra => {
            document.getElementById("nomeQuadra").value = quadra.nomeQuadra;
            document.getElementById("precoQuadra").value = quadra.preco;
            document.getElementById("localizacaoQuadra").value = quadra.localizacao;
            document.getElementById("descricaoQuadra").value = quadra.descricao;

            // Adiciona um atributo para armazenar o ID da quadra que está sendo editada
            document.getElementById("formCadastroQuadra").dataset.quadraId = id;
        })
        .catch(error => console.error("Erro ao carregar quadra para edição:", error));
}
