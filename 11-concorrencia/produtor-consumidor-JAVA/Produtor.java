public class Produtor extends Thread{

   public final static int MAX = 10;


   private String nome;
   private Fila fila;

   public Produtor(String nome, Fila fila) {
      this.nome = nome;
      this.fila = fila;
   }

   public void run() {
     for (int i = 0; i < MAX; i++) {
        Fila.esperaTempo();
        this.fila.deposita(i);
        System.out.println(">> Produtor [" + nome  + "] depositou " + String.valueOf(i));
     }
   }
}
