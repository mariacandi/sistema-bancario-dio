# Criando um Sistema Bancário com Python

Este repositório foi feito com o objetivo de concluir o desafio de projeto "Criando um Sistema Bancário com Python" proposto pela [DIO](https://www.dio.me/) no Bootcamp Suzano - Python Developer.

## Descrição do projeto

De acordo com a aba Informações na interface da DIO:

"Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes."

## Objetivos

Essa primeira versão trabalha apenas com 1 usuário, não sendo necessário identificar o número da agência e conta bancária.

O usuário deve conseguir depositar valores positivos para a conta bancária, os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

Já nas operações de saque, o sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

A operação de extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem, deve ser exibido o salto atual da conta. Os valores devem ser exibidos utilizando o formato R$ XXX.XX (ex. R$ 1500.45).

## Resolução

Busquei resolver o exercício antes de ver a solução proposta pelo instrutor, portanto, meu código está disponível no arquivo `sistema-bancario.py`, enquanto a resolução do intrutor se encontra em `resolucao-instrutor.py`.

Na minha resolução, além das variáveis fornecidas no template do instrutor, adicionei também as variáveis `deposito` e `saque`, e removi a variável `extrato`, pois a maneira que implementei o extrato é diferente da que o instrutor utilizou.

## Erros e acertos

Durante a resolução do exercício, utilizei minhas próprias anotações para resolver as dúvidas que acabei tendo no meio do caminho. Muitas das respostas estavam anotadas, eu só precisava olhar para as anotações para refrescar a memória. Contudo, percebi que acabei esquecendo de adicionar a condição que impede o depósito de valores negativos, o que foi corrigido posteriormente.

Percebi que o jeito que usei para arredondar os valores do saldo é diferente do jeito que o instrutor usou. Durante a resolução do exercício, eu tinha esquecido que era possível fazer daquele jeito e acabei usando o método `round()`, que na realidade eu nem sabia que existia em Python mas já o conhecia do SQL. Uma breve busca no Google me mostrou como ele é utilizado em Python e acabei usando ele mesmo.

Eu testei todos os cenários possíveis: depositar, sacar um valor abaixo de 500, sacar um valor acima de 500, tentar sacar mais de 3 vezes, bem como verificar o extrato e sair do sistema. Parece estar funcionando tudo direitinho, porém, caso haja qualquer irregularidade, aceito sugestões!

## Agradecimentos

Gostaria de agradecer a Suzano pelo Bootcamp, à DIO pelos materiais incríveis e ao instrutor Guilherme Carvalho.