const login = document.getElementById('login');

if (login) {
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
            alert('Login efetuado com sucesso!');
            window.location.href = "agenda.html";
        } else {
            alert('E-mail ou senha inválidos');
        }
    });
}

const formCadastro = document.getElementById("form_cadastro");
if (formCadastro) {
    formCadastro.addEventListener('submit', async (event) => {
        event.preventDefault();
        const dados = {
            nome: document.getElementById('nome').value,
            email: document.getElementById('email').value,
            aniversario: document.getElementById('data').value,
            telefone: document.getElementById('telefone').value,
            senha: document.getElementById('senha').value,
            confir_senha: document.getElementById('confir_senha').value,
        };

        const resposta = await fetch('http://127.0.0.1:8000/Criar/criar/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        if (resposta.ok) {
            alert('Cadastro realizado');
            window.location.href = "agenda.html";
        } else {
            const erroDetalhado = await resposta.json();
            console.error('Erro retornado pela API:', erroDetalhado);
            alert('Erro no cadastro! Verifique o console do navegador.');
        }
    });
}