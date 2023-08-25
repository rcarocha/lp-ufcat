package main


import ("fmt"
        "time"
        "container/list")

const MAX = 10

type Fila struct {
    Lista *list.List
}

func NewFila() Fila {
    initLista := list.New()
    return Fila{initLista}
}

func (fila Fila) Deposita(item int) {
    fila.Lista.PushBack(item)
}

func (fila Fila) Retira() int {
    primeiro := fila.Lista.Front()
    fila.Lista.Remove(primeiro)
    return primeiro.Value.(int)
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

    fmt.Println("------------------------------------------")

    terminado := make(chan bool)

    go produtor(fila, terminado)
    go consumidor(fila, terminado)
    <-terminado
    <-terminado
    fmt.Println("-------------------------------------------")
    
}
