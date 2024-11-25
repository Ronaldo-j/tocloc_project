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

async function carregarQuadras() {
    try {
        const response = await fetch('http://localhost:5000/quadra'); // URL do endpoint
        if (!response.ok) throw new Error("Erro ao carregar quadras");
        
        const quadras = await response.json();

        const quadrasContainer = document.getElementById('quadras-container');
        quadrasContainer.innerHTML = ''; // Limpa o container

        // Divide as quadras em grupos de 4
        for (let i = 0; i < quadras.length; i += 4) {
            const grupo = quadras.slice(i, i + 4);
            const isActive = i === 0 ? 'active' : ''; // Define a primeira como ativa

            // Cria um slide para cada grupo
            quadrasContainer.innerHTML += `
                <div class="carousel-item ${isActive}">
                    <div class="row">
                        ${grupo.map(quadra => `
                            <div class="col-md-3">
                                <div class="card mb-4">
                                    <img src="${quadra.foto}" alt="${quadra.nomeQuadra}" class="card-img-top img-fluid">
                                    <div class="card-body text-center">
                                        <h4 class="card-title">${quadra.nomeQuadra}</h4>
                                        <p class="card-text">${quadra.descricao}</p>
                                        <a href="detalhe.html?id=${quadra.id}" class="btn btn-secondary">Ver Detalhes</a>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>`;
        }
    } catch (error) {
        console.error("Erro ao carregar quadras:", error);
    }
}

// Carrega as quadras quando a página for carregada
document.addEventListener('DOMContentLoaded', carregarQuadras);


// Carrega as quadras quando a página for carregada
document.addEventListener('DOMContentLoaded', carregarQuadras);
