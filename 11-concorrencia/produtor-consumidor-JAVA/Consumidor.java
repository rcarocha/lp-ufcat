public class Consumidor extends Thread{

    public final static int MAX = 10;

    private Fila fila;
    private String nome;

    public Consumidor(String nome, Fila fila) {
       this.fila = fila;
       this.nome = nome;
    }
    
    public void run() {
        for (int i = 0; i < MAX; i++) {
           int retirado = this.fila.retira();
           System.out.println("<< Processo [" + nome  + "] retirou " + String.valueOf(retirado));
        }
    }

}
