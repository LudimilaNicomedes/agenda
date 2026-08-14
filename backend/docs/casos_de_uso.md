Nome:UC01 - Login 
Descrição breve do caso de uso: O sistema permite que o usuário realize login para acessar funcionalidades restritas.
Algumas funcionalidades podem ser utilizadas sem autenticação. 
Pré-condição: Nenhuma. O login é necessário apenas para funcionalidades restritas.
Fluxo principal: 
Efetuar Login:
1 - O usuário solicita login no sistema 
2 - O sistema exibe o formulário de login
3 - O usuário informa o e-mail e senha 
4 - O sistema valida os dados
5 - O sistema concede acesso ás funcionalidades restritas (UC05)

Fluxo alternativo:
3a. E-mail inexistente
1 - O sistema identifica que o e-mail não foi encontrado na base de dados
2 - O sistema exibe uma mensagem de erro e oferece a opção de realizar o cadastro (UC02)

3b. Senha errada:
1 - O sistema identifica que a senha informada é incorreta
2 - O sistema informa que a senha é inválida e retorna ao passo 3 


Nome: UC02 - Cadastrar usuário
Fluxo principal: 				
Cadastrar:		
1 - O usuário solicita o cadastro no sistema
2 - O sistema exibe o formulário de cadastro
3 - O usuário informa o nome, e-mail, data de aniversário, telefone e uma senha
4 - O sistema solicita a confirmação da senha
5 - O usuário confirma a senha
6 - O sistema valida os dados
7 - O sistema cria a conta do usuário e concede acesso ás funcionalidades restritas (UC05)

Fluxo alternativo:
3a. Se o e-mail já existir:
1 - O sistema identifica que o e-mail já existe na base de dados 
2 - O sistema exibe uma mensagem de erro e retorna ao passo 2

3.b Telefone já cadastrado:  
1 - O sistema identifica que o telefone já existe na base de dados
2 - O sistema informa que esse número de telefone já foi cadastrado e retorna ao passo 2 

5a. Senhas não coincidem:
1 - O sistema identifica que as senhas informadas não coincidem
2 - O sistema exibe uma mensagem de erro e retorna ao passo 4 


Nome: UC03 - Agendar
Descrição: O usuário realiza agendamento de clientes no calendário
Pré-condição: Nenhuma.
1 - Sistema exibe o calendário atual e formulário
2 - O usuário solicita cadastro de clientes no sistema
3 - O sistema exibe formulário solicitando nome, telefone, horário e tipo de serviço
4 - O usuário preenche as informações solicitadas
5 - O sistema valida os dados
6 - O sistema salva agendamento e o exibe no calendário  

Fluxo alternativo:
4a. Se tiver algum campo que não foi preenchido: 
1 - O sistema identifica que há campos obrigatórios não preenchidos 
2 - O sistema alerta ao usuário sobre os campos e retorna ao passo 3


Nome: UC04 - Dashboard
Descrição: O sistema exibe uma análise completa dos agendamentos feitos pelo usuário
Pré-condição: Nenhuma
Fluxo principal:
1 - O sistema exibe uma análise do mês atual 
2 - O usuário solicita a visualização de outro mês
3 - O sistema solicita o mês e ano 
4 - O usuário preenche as informações solicitadas 
5 - O sistema exibe a análise do mês que o usuário solicitou

Fluxo alternativo:
4a. Se colocar um ano que não teve nenhum agendamento
1 - O sistema identifica que não houve nenhum agendamento feito 
2 - O sistema exibe uma mensagem "aviso de dados não encontrados" e solicita ao usuário que selecione outro período e retorna ao passo 2


Nome: UC05 - Consultar, Editar ou Excluir Agendamento
Descrição: O usuário consulta a lista de agendamentos para visualizar detalhes, alterar dados ou excluir um registro.
Pré-condição: Usuário autenticado no sistema.
Fluxo principal:
1 - O sistema exibe o campo de pesquisa e a lista de agendamentos.
2 - O usuário pesquisa e seleciona o agendamento desejado
3 - O sistema exibe os detalhes do agendamento com as opções de "Editar" e "Excluir"
4 - O usuário seleciona a opção "Editar"
5 - O sistema exibe o formulário preenchido e as opções de "Salvar" e "Cancelar".
6 - O usuário altera os campos desejados e seleciona "Salvar".
7 - O sistema valida os dados informados.
8 - O sistema salva as alterações e atualiza a exibição na agenda.

Fluxo alternativo: Cancelar edição (Passo 5)
1 - O usuário seleciona a opção "Cancelar".
2 - O sistema descarta as alterações e retorna ao Passo 3 do fluxo principal.

Fluxo alternativo 2: Excluir agendamento (Passo 3)
1 - O usuário seleciona a opção "Excluir".
2 - O sistema solicita confirmação: "Tem certeza de que deseja excluir este agendamento?".
3 - O usuário confirma a exclusão.
4 - O sistema remove o agendamento e atualiza a exibição na agenda.

Fluxo alternativo 3: Cancelar exclusão (Passo 3 do Fluxo alternativo 2)
1 - O usuário não confirma a exclusão.
2 - O sistema cancela a operação e retorna ao Passo 3 do fluxo principal.

Fluxo de exceção: Dados inválidos na edição (Passo 7)
1 - O sistema identifica dados incorretos ou campos obrigatórios vazios.
2 - O sistema exibe uma mensagem de alerta indicando os erros.
3 - O sistema mantém o formulário aberto (Passo 5) para correção.