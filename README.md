# Desafio Sistema bancário em Python
Desafio de criação de sistema bancário em Python através da plataforma [Dio.me](https://web.dio.me/home)

## Requisitos v1
 * ### Operação de depósito
   * Deve ser possível depositar valores positivos na conta bancária.
   * Todos os depósitos devem ser armazenados em uma variável e exibidos na operação "extrato".
 
 * ### Operação de saque
   * O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não possua saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
   * Todos os saques devem ser armazenados em uma variável e exibidos na operação "extrato".

  * ### Operação de extrato
    * Essa operaçao deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
    * Os valores devem ser exibidos usando o formato R$ XXX.XX

## Requisitos v2
 * ### Objetivo geral
   * Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

 * ### Desafio
   * Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário).

 * ### Saque
   * A função "saque" deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero saques, limite saques. Sugestão de retorno: saldo e extrato.

 * ### Depósito
   * A função de depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

 * ### Extrato
   * A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

 * ### Novas funções
   * Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

 * ### Criar usuário (cliente)
   * O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.

 * ### Criar conta corrente
   * O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

 * ### Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
