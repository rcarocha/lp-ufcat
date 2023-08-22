# Laboratório 11.3: Monitores em Java e problema do Produtor-Consumidor

Nesta tarefa você irá verificar o funcionamento de monitores em Java para resolver o problema do produtor-consumidor. Todos os códigos aqui discutidos estão em [`produtor-consumidor-JAVA`](produtor-consumidor-JAVA/)

Observe que esses código não seguem a estrutura dos códigos Python. Por exemplo, há várias tarefas produtoras.

Os códigos estão assim organizados:

* [`Consumidor.java`](produtor-consumidor-JAVA/Consumidor.java): thread que consome diversos item na fila.
* [`Fila.java`](produtor-consumidor-JAVA/Fila.java): implementa a fila para armazenamento dos dados produzidos.
* [`Produtor.java`](produtor-consumidor-JAVA/Produtor.java): thread que cria diversos itens e armazena na fila.

Observe que inicialmente há 10 produtores e 1 consumidor que tenta consumir 10 dados.

Não há nenhuma primitiva de sincronização no código e a estrutura de dados utilizada (`ArrayList`) **não** é thread-safe.

## Compilação e Execução do Código

Para compilar o código você deve utilizar o seguinte comando no diretório onde estão os fontes

        javac -cp . *.java

Para executar o código, utilize a linha de comando

        java -cp . Fila | python3 reporta-concorrencia.py

## Tarefas

1. Execute o código e veja os possíveis problemas no funcionamento do produtor e consumidor. Execute várias vezes, pois a saída pode ser diferente (para diminuir o tamanho da fonte do terminal utilize `Ctrl-Shift-(-)`). Você consegue identificar a origem desses problemas?
2. Resolva o problema de acesso simultâneo às funções da fila, usando `synchronized` nos respectivos métodos. Após essa modificação, o que ocorre com a saída? Por que esse problema ocorre?
3. Notifique as threads quando à espera por recursos utilizando as primitivas de monitores `notify` (use `notifyAll`) e `wait`. Observe que o `wait` precisa ser utilizado no contexto de tratamento de exceção, como no código abaixo

```Java
try {
   wait();
} catch (InterruptedException e) {}
```

   Observe o comportamento do código. Experimente a inclusão de atrasos no código (método `esperaTempo()` de `Fila`) para se certificar do comportamento do código.


há muito mais produtores que consumidores e, por isso, o resultado da execução irá (ou deveria) travar um dos conjuntos de processos se a fila atingir o seu máximo ou mínimo.
