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
4a. Se tiver algum campo que não for preenchido: 
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