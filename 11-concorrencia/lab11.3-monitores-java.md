# Laboratório 11.3: Monitores em Java e problema do Produtor-Consumidor

Nesta tarefa você irá verificar o funcionamento de monitores em Java para resolver o problema do produtor-consumidor. Todos os códigos aqui discutidos estão em [`produtor-consumidor-JAVA`](produtor-consumidor-JAVA/)

Observe que esses código não seguem a estrutura dos códigos Python. Por exemplo, há várias tarefas produtoras.

Os códigos estão assim organizados:

* [`Consumidor.java`](produtor-consumidor-JAVA/Consumidor.java): thread que consome diversos item na fila.
* [`Fila.java`](produtor-consumidor-JAVA/Fila.java): implementa a fila para armazenamento dos dados produzidos.
* [`Produtor.java`](produtor-consumidor-JAVA/Produtor.java): thread que cria diversos itens e armazena na fila.
