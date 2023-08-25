# Laboratório 11.4: Passagem de Mensagens em Go e problema do Produtor-Consumidor

Nesta tarefa você irá verificar o funcionamento de sincronização em Go, utilizando passagem de mensagens pela construção **channel** oferecida pela linguagem. Todos os códigos aqui discutidos estão em [`produtor-consumidor-GO`](produtor-consumidor-GO/)

Observe que os primeiros códigos não devem ser utilizados junto com `reporta-concorrencia.py`, pois eles são geram uma saída compatível com o programa. Como a linguagem Go deve ser novidade para a maioria dos alunos, os primeiros códigos serão construídos do zero pelo professor com o objeto de familiar os alunos com a sintaxe e funcionamento da linguagem. Assim, depois será mais simples se concentrar exclusivamente na primitiva de sincronização na discussão do código.


Os códigos estão assim organizados:


1. [`produtor-consumidor-0.go`](produtor-consumidor-GO/produtor-consumidor-0.go): programa inicial para compreensão da estrutura e sintaxe de programa Go e contato inicial com `channel` e gorotinas.
2. [`produtor-consumidor-3.go`](produtor-consumidor-GO/produtor-consumidor-3.go): uma versão Go do produtor-consumidor tentando reproduzir a estrutura do código feito em Java e Python.
3. [`produtor-consumidor-c1.go`](produtor-consumidor-GO/produtor-consumidor-c1.go): versão utilizando apenas channels para implementação da solução, e com consumidor executando indefinidamente.
4. [`produtor-consumidor-c2.go`](produtor-consumidor-GO/produtor-consumidor-c2.go): modificação da versão anterior, utilizando diversas gorotinas para `num_prod` produtores e `num_cons` consumidores. Código ajustado para filtragem da saída pelo `reporta-concorrencia.py`.


## Compilação e Execução do Código

Para compilar o código você deve utilizar o seguinte comando no diretório onde estão os fontes

        go run programa.go

## Documentação Adicional de Auxilio

* Pacote com lista ligada [`container/list`](https://pkg.go.dev/container/list)

## Tarefas

1. Acompanhe o professor na construção do código `produtor-consumidor-0.go`.
2. Execute o código `produtor-consumidor-0.go` e experimente fazer com que uma das gorotinas deixe de ser uma gorotina. O que ocorre? Consegue explicar a origem do problema?
3. Qual a diferença entre as duas formas de usar um channel abaixo, **do ponto de vista** do propósito e efeito na sincronização?
   * `a := make(chan bool)`
   * `a := make(chan bool, 10)`
4. Por que não é necessário garantir o acesso exclusivo (como em `synchronized` na versão Java) para o código final do produtor-consumidor?
5. *Caso dê tempo*, discutiremos
   * A construção `select` pelo exemplo [aqui](https://go.dev/talks/2012/concurrency.slide#36).
   * o código de [*Concurrency is not Parallelism*](https://go.dev/talks/2012/waza.slide#1)
