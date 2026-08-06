let chartInstance = null;

// Executa ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
  // Define o mês e ano atual no input (Passo 1 do UC04)
  const hoje = new Date();
  const ano = hoje.getFullYear();
  const mes = String(hoje.getMonth() + 1).padStart(2, '0');
  
  document.getElementById('mesAnoSelect').value = `${ano}-${mes}`;
  carregarDashboard();
});

async function carregarDashboard() {
  const mesAno = document.getElementById('mesAnoSelect').value;
  if (!mesAno) return;

  const [ano, mes] = mesAno.split('-');

  try {
    // Faz a chamada GET para o seu servidor FastAPI
    const response = await fetch(`http://127.0.0.1:8000/analise/dashboard/?mes=${mes}&ano=${ano}`);
    const resultado = await response.json();

    const chartContainer = document.getElementById('chartContainer');
    const avisoVazio = document.getElementById('avisoVazio');

    // Trata o Fluxo Alternativo 4a (Sem dados encontrados)
    if (!resultado.sucesso || resultado.dados.length === 0) {
      chartContainer.style.display = 'none';
      avisoVazio.style.display = 'block';
      return;
    }

    // Exibe o gráfico e oculta o aviso
    chartContainer.style.display = 'block';
    avisoVazio.style.display = 'none';

    // Atualiza o total no meio do gráfico
    document.getElementById('totalAgendamentos').textContent = resultado.total_agendamentos;

    // Renderiza o gráfico com os dados recebidos do backend
    renderizarGrafico(resultado.dados);

  } catch (erro) {
    console.error('Erro ao conectar com a API:', erro);
  }
}

function renderizarGrafico(dadosServicos) {
  const ctx = document.getElementById('meuGrafico').getContext('2d');

  // Se já existir um gráfico criado previamente, destrói antes de criar o novo
  if (chartInstance) {
    chartInstance.destroy();
  }

  const labels = dadosServicos.map(item => item.servico);
  const valores = dadosServicos.map(item => item.total);

  chartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        data: valores,
        backgroundColor: [
          '#9F66E9',
          '#0284c7',
          '#38bdf8',
          '#818cf8',
          '#cbd5e1'
        ],
        borderWidth: 2,
        borderColor: '#ffffff',
        cutout: '72%' // Espaço interno para criar o visual de rosca igual da imagem
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            usePointStyle: true,
            boxWidth: 8,
            padding: 15
          }
        }
      }
    }
  });
}