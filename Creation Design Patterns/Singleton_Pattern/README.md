# Singleton Pattern

**1. The "Why": What problem does this pattern solve? (ELI6 - Explain Like I'm 6)**

Imagine you have a special toy box, and this toy box is unique. There's only _one_ of this special toy box in the whole world (or in your whole house, for our example).

- **Why only one?** Maybe this toy box holds the "Master Rules" for all your games. If you had many "Master Rules" boxes, they might have different rules, and everyone would get confused!
- **Easy to find:** Everyone in the house knows _exactly_ where this one special toy box is. They don't need to search for it or ask, "Which master rules box should I use?"

The Singleton Pattern is like that special toy box. It makes sure that for a certain kind of thing (we call this a "class" in programming), there is **only one** instance (one object, one "thing") created for your entire application. And it gives everyone an easy, well-known way to get to that single instance.

**Common reasons you'd want only one of something:**

- **Managing a shared resource:** Like a connection to a database (you might want to manage a pool of connections, but the manager itself could be a singleton), or access to a printer.
- **A global point of access for configuration:** Your application might have settings that many parts need to read. A singleton can hold these settings.
- **A logging facility:** You typically want all log messages to go through one central logger.

**2. The "What": The core concept and structure of the pattern.**

The Singleton pattern ensures:

- **One Instance Only:** A class can have only one instance.
- **Global Access Point:** It provides a global point of access to that instance.

How does it achieve this? Typically by:

- Making the **constructor private** (or otherwise inaccessible from outside the class directly), so no one else can just create new instances willy-nilly.
- Providing a **static method** (a method belonging to the class, not an instance) that does the following:
  - Checks if an instance already exists.
  - If not, it creates the single instance (internally, because it _can_ access the private constructor).
  - Returns the (newly created or existing) instance.

**3. The "How": Implementation**

Let's look at implementations in Python, TypeScript, and how Go handles similar scenarios.

## Python Implementation Approaches

Python offers a several ways to implement Singletons, from classic approaches to more "Pythonic" ones.

### a. Classic Implementation (using class variable and `__new__`)

**_This is often shown as a direct translation from languages like Java/C++_**

Please refer to [Python/classic_singleton.py](Python/classic_singleton.py) for the implementation.

### b. Module-Level Singleton (Most Pythonic & Simplest)

In python, modules themselves are singletons. When a module is imported for the first time, its code is executed, and the resulting module object is cached in sys.modules. Subsequent imports of the same module simply return the cached object. This is often the preferred and simplest way in Python.

Please refer to [Python/module_singleton.py](Python/module_singleton.py) for the implementation.

### c. Metaclass implementation (More Advanced)

Metaclasses are "classes of classes." They control the creation of classes. This is a more advanced Python feature but provides a very robust way to implement singletons.

Please refer to [Python/metaclass_singleton.py](Python/metaclass_singleton.py) for the implementation.

## TypeScript Implementation

Typescript, being statically typed and class-based, implements Singletons in a way that's very similar to Java or C#.

Please refer to [TypeScript_JavaScript/singleton.ts](TypeScript_JavaScript/singleton.ts) for the implementation.

### JavaScript (ES6 Modules variant)

Modern JavaScript often achieves singleton-like behavior through its module system (ESM or CommonJS). When you export an object or class instance from a module, that module is cached by the runtime. Subsequent imports of that module will refer to the same cached instance.

Please refer to [TypeScript_JavaScript/main.mjs](TypeScript_JavaScript/main.mjs) for the implementation.

## Go Implementation (Idiomatic Approaches)

Go doesn't have classes or constructors in the same way as Python/TS. Singletons are often achieved using package-level variables and careful initialization, often with the sync.Once type for thread-safe lazy initialization.
