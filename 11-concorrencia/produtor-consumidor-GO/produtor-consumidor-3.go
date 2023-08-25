package main

import ("fmt"
        "time"
        "container/list")

const MAX = 5

type Fila struct {
    Lista *list.List
    filaCheia chan bool
    filaVazia chan bool
}


func NewFila() Fila {
    initLista := list.New()
    filaCheia := make(chan bool)
    filaVazia := make(chan bool)
    return Fila{initLista, filaCheia, filaVazia}
}

func (fila Fila) Deposita(item int) {
    if fila.Lista.Len() < MAX {
       fila.Lista.PushBack(item)
       if fila.Lista.Len() == 1 {
           fila.filaVazia <- false
       }
    } else {
        <-fila.filaCheia
        fila.Lista.PushBack(item)
    }
}

func (fila Fila) Retira() int {
    if fila.Lista.Len() > 0 {
        primeiro := fila.Lista.Front()
        fila.Lista.Remove(primeiro)
        if fila.Lista.Len() == MAX - 1 {
            fila.filaCheia <- false
        }
        return primeiro.Value.(int)
    } else {
        <-fila.filaVazia
        primeiro := fila.Lista.Front()
        fila.Lista.Remove(primeiro)
        return primeiro.Value.(int)
    }
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
    numero := 10
    for i := 0; i < numero; i++ {
        item := fila.Retira()
        fmt.Println("Consumindo (", item, ")")
        time.Sleep(1000)
    }
    terminado <- true
}


func main() {

    fila := NewFila()

    fmt.Println("-------------------------------------------")

    terminado := make(chan bool)

    go produtor(fila, terminado)
    go consumidor(fila, terminado)
    <-terminado
    <-terminado
    fmt.Println("-------------------------------------------")
    
}
