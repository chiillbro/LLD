package main

import (
	"fmt"
	"sync"

	// "singleton/myconfig"

	"singleton/mylazylogger"
)


func main() {
	var wg sync.WaitGroup
	numGoroutines := 5

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()
			fmt.Printf("Goroutine %d trying to get logger instance...\n", id)
			logger := mylazylogger.GetInstance()
			logger.Log(fmt.Sprintf("Message from goroutine %d, logger init time: %s", id, logger.GetInitTime()))
		}(i)
	}


	wg.Wait()

	fmt.Println("All goroutines finished.")

	logger1 := mylazylogger.GetInstance()
	logger2 := mylazylogger.GetInstance()
	fmt.Printf("Are logger1 and logger2 the same? %t\n", logger1 == logger2)
	fmt.Printf("Logger 1 init time: %s\n", logger1.GetInitTime())
	fmt.Printf("Logger 2 init time: %s\n", logger2.GetInitTime())
 }

// func main() {
// 	cfg1 := myconfig.GetInstance()
// 	fmt.Printf("App Name from cfg1: %s\n", cfg1.AppName)
// 	fmt.Printf("DB Host from cfg1: %s\n", cfg1.GetSetting("db_host"))

// 	cfg2 := myconfig.GetInstance()
// 	cfg2.SetSetting("db_host", "remote-db.example.com")

// 	fmt.Printf("DB Host from cfg1 after cfg2 modification: %s\n", cfg1.GetSetting("db_host"))
// 	fmt.Printf("Are cfg1 and cfg2 the same? %t\n", cfg1 == cfg2)
// }