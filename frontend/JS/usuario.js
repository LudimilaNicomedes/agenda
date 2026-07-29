const login = document.getElementById('login');

login.addEventListener('submit', async (event) => {
    event.preventDefault(); 
    const dados = {
        email: document.getElementById('email').value,
        senha: document.getElementById('senha').value,

    };

    const response = await fetch('http://127.0.0.1:8000/login/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.ok) {
        const resultado = await response.json();
        alert('Login efetuado com sucesso!');
        window.location.href = "/agenda.html"

    } else {
        alert('E-mail ou senha inválidos');
    }

});
