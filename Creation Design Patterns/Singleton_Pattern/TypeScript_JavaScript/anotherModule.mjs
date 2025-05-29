import configStore from "./configStore.mjs";

export function displayLanguage() {
  console.log("anotherModule.js: Accessing config store...");
  console.log(
    `Current language from another module: ${configStore.getSetting(
      "language"
    )}`
  );
}
