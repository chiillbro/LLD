class AppConfig {
  private static instance: AppConfig; // A static variable to hold the single instance
  public readonly appName: string;
  private readonly settings: Map<string, any>;

  private constructor() {
    // Prevents direct instantiation with new AppConfig()
    console.log(
      "AppConfig: Private constructor called - initializing instance."
    );

    this.appName = "MySuperApp";
    this.settings = new Map<string, any>();
    this.settings.set("version", "1.0.0");
    this.settings.set("api_url", "https://api.example.com");
    // Simulate loading config from a file or environment
  }

  public static getInstance(): AppConfig {
    // The global access point. It handles lazy initialization (create the instance only when first requested)
    if (!AppConfig.instance) {
      console.log("AppConfig: Instance not found, creating new one.");
      AppConfig.instance = new AppConfig();
    } else {
      console.log("AppConfig: Returning existing instance.");
    }

    return AppConfig.instance;
  }

  public getSetting(key: string): any {
    return this.settings.get(key);
  }

  public setSetting(key: string, value: any): void {
    this.settings.set(key, value);
    console.log(`AppConfig: Setting '${key}' updated to '${value}'.`);
  }
}

// --- Usage ---
// const configError = new AppConfig(); // Error: Constructor of class 'AppConfig' is private.

const config1 = AppConfig.getInstance();
console.log(`Config1 App Name: ${config1.appName}`);
console.log(`Config1 API URL: ${config1.getSetting("api_url")}`);

const config2 = AppConfig.getInstance();
console.log(`Config2 Version: ${config2.getSetting("version")}`);

console.log(`Are config1 and config2 the same object? ${config1 === config2}`); // Output: true

config1.setSetting("api_url", "https://new.api.example.com");
console.log(
  `Config2 API URL after config1 modification: ${config2.getSetting("api_url")}`
); // Shows the new URL
