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
    const urlParams = new URLSearchParams(window.location.search);
    const quadraId = urlParams.get('id');

    if (quadraId) {
        axios.get(`http://localhost:5000/quadra/${quadraId}`)
            .then(response => {
                const data = response.data;
                const quadraDetailsContainer = document.getElementById('quadraDetails');
                quadraDetailsContainer.innerHTML = `
                    <h2>${data.nomeQuadra}</h2>
                    <img src="${data.foto}" class="img-fluid" alt="${data.nomeQuadra}">
                    <p><strong>Localização:</strong> ${data.localizacao}</p>
                    <p><strong>Descrição:</strong> ${data.descricao}</p>
                    <form id="reservaForm">
                        <label for="dataReserva">Selecione a data:</label>
                        <input type="date" id="dataReserva" name="dataReserva" class="form-control" required>
                        <label for="horaReserva" class="mt-3">Selecione o horário:</label>
                        <input type="time" id="horaReserva" name="horaReserva" class="form-control" required>
                        <button type="submit" class="btn btn-success mt-3">Reservar agora</button>
                    </form>
                `;
                document.getElementById('reservaForm').addEventListener('submit', (e) => {
                    e.preventDefault();
                    reservarQuadra(quadraId);
                });
            })
            .catch(error => {
                console.error('Erro:', error);
                document.getElementById('quadraDetails').innerHTML = '<p>Erro ao carregar os detalhes da quadra.</p>';
            });
    }
};

function reservarQuadra(quadraId) {
    const dataReserva = document.getElementById('dataReserva').value;
    const horaReserva = document.getElementById('horaReserva').value;

    const user = JSON.parse(localStorage.getItem('user'));
    if (!user) {
        alert('Você precisa estar logado para fazer uma reserva.');
        window.location.href = 'login.html';
        return;
    }

    axios.post('http://localhost:5000/reserva', {
        user_id: user.id,
        quadra_id: quadraId,
        horario: `${dataReserva} ${horaReserva}`
    })
    .then(response => {
        const data = response.data;
        if (response.status === 200) {
            alert(data.message);
            window.location.href = 'minhas_reservas.html';
        } else {
            alert(data.error || 'Ocorreu um erro ao processar sua reserva.');
        }
    })
    .catch(error => {
        console.error('Erro ao reservar:', error);
        alert('Ocorreu um erro inesperado. Por favor, tente novamente.');
    });
}
