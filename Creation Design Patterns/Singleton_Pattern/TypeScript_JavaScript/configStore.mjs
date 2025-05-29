console.log(
  "configStore.js module execution: Initializing configuration store."
);

const settings = new Map();
settings.set("theme", "dark");
settings.set("language", "en");

const configStore = {
  getSetting: (key) => {
    console.log(`configStore.js: Getting setting '${key}'`);
    return settings.get(key);
  },

  setSetting: (key, value) => {
    console.log(`configStore.js: Setting '${key}' to '${value}'`);
    settings.set(key, value);
  },

  getAllSettings: () => {
    return Object.fromEntries(settings); // Return a copy for inspection
  },
};

Object.freeze(configStore); // Optional: makes the exported object immutable (its properties cannot be changed)

export default configStore;

/// This is very similar to the Python module-level singleton. The configStore.js module is executed once, its configStore object is created, and then cached. All other modules importing it get the same object.
