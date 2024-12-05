document.addEventListener('DOMContentLoaded', () => {
    const user = JSON.parse(localStorage.getItem('user'));

    if (user) {
        document.getElementById('login-btn').classList.add('d-none');
        document.getElementById('signup-btn').classList.add('d-none');
        document.getElementById('user-menu').classList.remove('d-none');
    }
});

function logout() {
    localStorage.removeItem('user');
    window.location.href = 'login.html';
}

window.onload = function () {
    // Função para buscar as quadras cadastradas
    function buscarQuadras(query = '') {
        axios.get('http://localhost:5000/quadra')
            .then(response => {
                const data = response.data;
                console.log(data); // Verifica o que está sendo retornado
                const quadrasContainer = document.getElementById('quadrasContainer');
                quadrasContainer.innerHTML = ''; // Limpa o container de quadras

                // Filtra as quadras conforme a pesquisa
                const filteredData = data.filter(quadra => {
                    return quadra.nomeQuadra.toLowerCase().includes(query.toLowerCase()) ||
                        quadra.localizacao.toLowerCase().includes(query.toLowerCase());
                });

                if (filteredData.length === 0) {
                    quadrasContainer.innerHTML = '<p>Nenhuma quadra encontrada.</p>';
                } else {
                    // Adiciona cada quadra à página
                    filteredData.forEach(quadra => {
                        const quadraCard = `
                            <div class="col-md-4 quadra-card">
                                <div class="card">
                                    <img src="${quadra.foto}" class="card-img-top" alt="${quadra.nomeQuadra}">
                                    <div class="card-body text-center">
                                        <h4 class="card-title">${quadra.nomeQuadra}</h4>
                                        <p class="card-text">${quadra.descricao}</p>
                                        <a href="detalhe.html?id=${quadra.id}" class="btn btn-primary">Reservar</a>
                                    </div>
                                </div>
                            </div>
                        `;
                        quadrasContainer.innerHTML += quadraCard;
                    });
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                // Exibe um erro na página
                const quadrasContainer = document.getElementById('quadrasContainer');
                quadrasContainer.innerHTML = '<p>Erro ao carregar as quadras.</p>';
            });
    }

    // Chama a função para carregar as quadras inicialmente
    buscarQuadras();

    // Adiciona evento de input para pesquisa
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', function (event) {
        const query = event.target.value;
        buscarQuadras(query);  // Chama a função de busca com o texto digitado
    });
};