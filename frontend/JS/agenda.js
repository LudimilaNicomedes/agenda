document.getElementById('form-agenda').addEventListener('submit', async (event) => {
    event.preventDefault(); 
    const dados = {
        nome: document.getElementById('nome').value,
        telefone: document.getElementById('telefone').value,
        data_hora: document.getElementById('data_hora').value,
        servico: document.getElementById('servico').value
    };

    const response = await fetch('http://127.0.0.1:8000/agendar/agendar/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.status === 422) {
        alert('Por favor, preencha todos os campos obrigatórios corretamente!');
        return;
    }
    
    if (response.ok) {
        const resultado = await response.json();
        alert('Cliente cadastrado com sucesso!');
    } else {
        alert('Erro ao cadastrar agendamento.');
    }
});


document.addEventListener("DOMContentLoaded", function() {
    // Verifique o ID exato que você usou no HTML
    flatpickr("#meu-calendario", {
        inline: true,          // Mantém o calendário visível
        locale: "pt",          // Português
        dateFormat: "Y-m-d",
        // Certifique-se de que não há nenhuma opção 'wrap: true' aqui,
        // a menos que você esteja usando um input container específico.
    });
});