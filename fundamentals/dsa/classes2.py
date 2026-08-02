from typing import Any




class House:
    def __new__(cls) -> self:
        pass
        
        
    def __init__(self) -> None:
        pass
    


class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name: str = name
        self.age: int = age
        
p: Person = Person("Bob", 30)
print(p.name, p.age)


class DebugClass:
    def __new__(cls,*args: Any, **kwargs: Any) -> 'DebugClass':
        print(f"__new__ called with args: {args}, kwargs: {kwargs}")
        instance = super().__new__(cls)
        print(f"__new__ returning instance: {instance}")
        return instance
        
    def __init__(self, value:Any) -> None:
        print(f"value is {value}")
        self.value: Any = value
        
        
obj: DebugClass = DebugClass("test")#debug called before initialiser




class Singleton:
    _instance: 'Singleton | None' = None
    
    def __new__(cls,*args: Any, **kwargs: Any) -> 'Singleton':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self, name:str) -> None:
        self.name: str = name
        
a: Singleton = Singleton("First")
b: Singleton = Singleton("Second")
#both the exact same object

