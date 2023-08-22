import java.util.ArrayList;
import java.util.Random;

public class Fila {

  private static Random random = new Random();

  public static void esperaTempo() {
    int SUPERIOR = 100;
    int aleat = Fila.random.nextInt(SUPERIOR);
    // System.out.println(aleat);

    int tempoSUPERIOR = 50; // milissegundos
    int tempoINFERIOR = 1; // milissegundos

    try {
      Thread.sleep(tempoINFERIOR + (aleat % tempoSUPERIOR));
    } catch (InterruptedException e) {}
  }

  private ArrayList < Integer > fila;

  public static int MAX_FILA = 75;

  public Fila() {
    this.fila = new ArrayList < Integer > ();
  }

  public synchronized void deposita(int item) {
    while (this.fila.size() >= MAX_FILA) {
    
      // Mensagem na saida de erro para nao interferir no reporta-concorrencia
      //System.err.println("-- MAXIMO da fila --");

    }
    this.fila.add(item);
  }

  public synchronized int retira() {
    while (this.fila.size() == 0) {
    
      // Mensagem na saida de erro para nao interferir no reporta-concorrencia
      //System.err.println("-- fila VAZIA --");
    }

    Integer retornado = this.fila.remove(0);
    return retornado;
  }

  public static void main(String[] a) {
    String nomesTarefas = "";
    
    Fila f = new Fila();
    
    Consumidor c = new Consumidor("0-consumidor", f);
    nomesTarefas = nomesTarefas + "0-consumidor;";
   
    Produtor[] vP = new Produtor[10];
    for (int i = 0; i < 10; i++) {
      String nomeProdutor = String.valueOf(i) + "-produtor";
      Produtor p = new Produtor(nomeProdutor, f);
      
      nomesTarefas = nomesTarefas + nomeProdutor + ";";
      
      vP[i] = p;
    }
    
    System.out.println(nomesTarefas);


    for (int i = 0; i < 10; i++) {
      vP[i].start();
    }

    c.start();

  }
}
