package mylazylogger

import (
	"fmt"
	"sync"
	"time"
)


type Logger struct {
	initTime time.Time
	logs []string
	// For thread-safe access to logs slice (if methods modify it)
	// mu sync.Mutex
}


var (
	instance *Logger
	once sync.Once // Guarantees the Do func is called only once
)


func newLogger() *Logger {
	fmt.Println("mylazylogger: newLogger() called - Heavy initialization logic here...")

	time.Sleep(1 * time.Second)

	return &Logger{
		initTime: time.Now(),
		logs: make([]string, 0),
	}
}



// GetInstance returns the singleton Logger instance.
// It's thread-safe for initialization

func GetInstance() *Logger {
	fmt.Println("mylazylogger: GetInstance() called.")
	once.Do(func() {
		fmt.Println("mylazylogger: once.Do() executing - actual creation happening now.")

		instance = newLogger()
	})

	return instance
}



func (l *Logger) Log(message string) {
	// l.mu.Lock() // If logs slice needs concurrent protection
	// defer l.mu.Unlock()
	l.logs = append(l.logs, message)
	fmt.Printf("[%s] LOG: %s\n", l.initTime.Format("15:04:05"), message)
}


func (l *Logger) GetInitTime() time.Time {
	return l.initTime
}



// func main() {
// 	var wg sync.WaitGroup
// 	wg.Add(2)

// 	go helloworld(&wg)
// 	go goodbye(&wg)
// 	wg.Wait()
// }

// func helloworld(wg *sync.WaitGroup) {
// 	defer wg.Done()
// 	fmt.Println("Hello world!")
// }

// func goodbye(wg *sync.WaitGroup) {
// 	defer wg.Done()
// 	fmt.Println("Good Bye!")
// }

// func main(){
// 	msg := make(chan string)
// 	go greet(msg)
// 	time.Sleep(2 * time.Second) 

// 	greeting := <- msg

// 	time.Sleep(2 * time.Second)

// 	fmt.Println("Greeting received: " + greeting)

// 	_, ok :=  <- msg
// 	if ok {
// 		fmt.Println("Channel is open!")
// 	} else {
// 		fmt.Println("Channel is closed!")
// 	}

// }

// func greet(ch chan string) {
// 	fmt.Println("Greeter waiting to send greeting!")

// 	ch <- "Hello Siva!"
// 	close(ch)

// 	fmt.Println("Greeter completed")
// }