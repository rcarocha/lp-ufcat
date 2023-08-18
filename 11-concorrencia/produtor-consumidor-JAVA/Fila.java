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


   try { Thread.sleep(tempoINFERIOR + (aleat % tempoSUPERIOR)); }
   catch (InterruptedException e) {}
}



private ArrayList<Integer> fila;

public static int MAX_FILA = 75;

public Fila() {
   this.fila = new ArrayList<Integer>();
}

public synchronized void deposita(int item) {
   while (this.fila.size() >= MAX_FILA) {
      System.out.println("-- MAXIMO da fila --");
      try {
      wait();}  catch (InterruptedException e) {
      }   
   }
   this.fila.add(item);
   notifyAll();
}

public synchronized int retira() {
   while (this.fila.size() == 0) {
      System.out.println("-- fila VAZIA --");
      try {
         wait();
      }  catch (InterruptedException e) {
      } 
   }
   
   Integer retornado = this.fila.remove(0);
   notifyAll();
   return retornado;
}

public static void main(String[] a){
    Fila f = new Fila();
    Consumidor c = new Consumidor("0", f);
    c.start();
    Produtor[] vP = new Produtor[10];
    for (int i = 0; i < 10; i++) {
       Produtor p = new Produtor(String.valueOf(i), f);
       vP[i] = p;
    }
    
    for (int i = 0; i < 10; i++) {
      vP[i].start();
    }

}
}
