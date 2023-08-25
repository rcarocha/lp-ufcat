package main

import ("fmt"
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

func produtor(fila Fila, terminado chan bool) {
    fmt.Println("** P **")    
    numero := 10
    for i := 0; i < numero; i++ {
       fmt.Println("Produzindo (", i, ")")
       fila.Deposita(i)
    }
    terminado <- true
}

func consumidor(fila Fila, terminado chan bool) {
    fmt.Println("-- C --")

    for {
        item := fila.Retira()
        fmt.Println("Consumindo (", item, ") ")
        time.Sleep(2 * time.Second)
    }
}


func main() {

    fila := NewFila()

    fmt.Println("-------------------------------------------")

    terminado := make(chan bool)

    go produtor(fila, terminado)
    go consumidor(fila, terminado)
    <-terminado
    fmt.Println("-------------------------------------------")
    


}
