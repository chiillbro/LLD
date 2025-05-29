import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    print("Creating new instance (Thread Safe)")
                    cls._instance = super().__new__(cls)

        
        return cls._instance
        