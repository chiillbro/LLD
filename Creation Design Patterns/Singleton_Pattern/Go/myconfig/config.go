package myconfig

import "fmt"


type AppConfig struct {
	AppName string
	Version string
	Settings map[string]any
}

// GO111MODULE on


// Eagerly initialized package-level variable.
// This init() function is run once when the package is first imported.

var globalConfig *AppConfig

func init() {
	fmt.Println("myconfig: init() called - Initializing global AppConfig.")

	globalConfig = &AppConfig{
		AppName: "GoApp",
		Version: "0.1.0",
		Settings: make(map[string]any),
	}
	globalConfig.Settings["db_host"] = "localhost"
	// In a real app. load from file, env vars, etc.
}


func GetInstance() *AppConfig {
	fmt.Println("myconfig: GetInstance() called.")
	return globalConfig
}


func (c *AppConfig) GetSetting(key string) any {
	return c.Settings[key]
}

func (c *AppConfig) SetSetting(key string, value any) {
	// Note: For concurrent use, this map access needs a mutex.
	// The Singleton pattern itself doesn't solve concurrent access to its *data*.
	c.Settings[key] = value
	fmt.Printf("myconfig: Setting '%s' updated to '%v' .\n", key, value)

}