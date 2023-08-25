package main

import ("fmt"
        "strconv"
        "time")

const MAX = 5
const MAXIMO_ATRASO = 10 // millissegundos

type Fila struct {
    canalFila chan int
}


func NewFila() Fila {
    canalFila := make(chan int, MAX)
    return Fila{canalFila}
}

func (fila Fila) Deposita(item int) {
    fila.canalFila <- item

}

func (fila Fila) Retira() int {
    item := <-fila.canalFila
    return item
}

func produtor(nome string, fila Fila, terminado chan bool) {
    numero := 10
    for i := 0; i < numero; i++ {
       fmt.Printf("%s;%d\n", nome, i)
       fila.Deposita(i)
    }
    terminado <- true
}

func consumidor(nome string, fila Fila, terminado chan bool) {

    for {
        item := fila.Retira()
        fmt.Printf("%s;%d\n", nome, item)
        time.Sleep(2 * time.Second)
    }
}


func main() {

    fila := NewFila()

    terminado := make(chan bool)

    num_prod := 2
    num_cons := 5

    for i := 0; i < num_prod; i++ {
        fmt.Printf("%d-produtor;",i)
    }
    for i := 0; i < num_cons; i++ {
        fmt.Printf("%d-consumidor;",i)
    }

    fmt.Println()

    for i := 0; i < num_prod; i++ {
        go produtor(strconv.Itoa(i) + "-produtor", fila, terminado)
    }
    for i := 0; i < num_cons; i++ {
        go consumidor(strconv.Itoa(i) + "-consumidor", fila, terminado)
    }

    for i := 0; i < num_prod; i++ {
        <-terminado
    }
    
}
