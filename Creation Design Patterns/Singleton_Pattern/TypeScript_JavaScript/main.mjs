import { displayLanguage } from "./anotherModule.mjs";
import configStore from "./configStore.mjs";
import anotherConfigStore from "./configStore.mjs";

console.log("main.js: Accessing config store...");

console.log(`Initial theme: ${configStore.getSetting("theme")}`);
configStore.setSetting("language", "fr");

displayLanguage();

console.log(
  `Is configStore === anotherConfigStore? ${configStore === anotherConfigStore}`
);

console.log(
  `configStore.getAllSettings(): ${JSON.stringify(
    configStore.getAllSettings()
  )}`
);
