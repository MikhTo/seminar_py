import math
from typing import Any, Literal
class Complex:
    """Тут можно писать всякое, чтобы пользователь при создании объекта класса.
    Например для этого класса:
    Это класс для работы с комплексными числами
    """
    def __init__(self, real:float, img: float) -> None:
        self.real = real
        self.img = img
    
    def abs(self) -> float:
        """Docstring также можно создать и для функций. Обычно это выглядит так:
        """
        return (self.real**2+self.img**2)**0.5
    
    def phase(self) -> float:
        return math.atan(self.img/self.real)
    
    def conj(self) -> None:
        self.img *= -1
    
    def __eq__(self, other) -> bool:
        return (self.real, self.img) == (other.real, other.img)
    
    def __add__(self, other):
        if isinstance(other, (int,float)):
            return Complex(self.real+other, self.img)
        elif isinstance(other, Complex):
            return Complex(self.real+other.real, self.img+other.img)
        else:
            raise ValueError(f"other can be Complex, int or float and can not be {type(other)}")
    
    def __abs__(self) -> float:
        return (self.real**2+self.img**2)**0.5
    
    def __radd__(self, other):
        return self+other
    
    def __getitem__(self, key: Literal[1,2,"real","img"]):
        """
        Предоставляет доступ к реальной и мнимой части комплексного числа.
        
        Параметры:
        key (int or "str"): индекс (1 или 0) или ключ-строка (real или img)
        """
        if key in (0,1):
            return self.real if key==0 else self.img
        elif key in ("real", "img"):
            return self.real if key=="real" else self.img
        else:
            raise KeyError(f"key can be either integer equal 0 and 1 or str equal \"real\" and \"img\", not {key}")
        
    def __reversed__(self):
        return Complex(self.img, self.real)

    def __call__(self, *args, **kwargs):
        print(f"Are you stupid or smth?"
              f" I'm Complex number what do you suppose to get calling me with all these {args} and {kwargs}?")

    def __contains__(self, item):
        return item in (self.real, self.img)
    
    def __repr__(self) -> str:
        return f"{self.real}{self.img:+}*i"
    
class MySuperPuperList(list):
    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs) -- вызовет конструктор родительского класса
    #    А тут можно еще что-то дописать


    def __add__(self, other):
        if isinstance(other, MySuperPuperList) and len(other) == len(self):
            return MySuperPuperList([x+y for x,y in zip(other, self)])
        elif isinstance(other, (int, float)):
            return MySuperPuperList([x+other for x in self])
        else:
            raise ValueError(f"other can be {type(self)} or parent classes, int or float and can not be {type(other)}")
        
    def __mult__(self, other):
        if isinstance(other, MySuperPuperList) and len(other) == len(self):
            return MySuperPuperList([x*y for x,y in zip(other, self)])
        elif isinstance(other, (int, float)):
            return MySuperPuperList([x*other for x in self])
        else:
            raise ValueError(f"other can be {type(self)} or parent classes, int or float and can not be {type(other)}")
    
    def __radd__(self, other):
        return self+other
    
    def __rmul__(self, other):
        return self*other
    
    def __iadd__(self, other):
        if isinstance(other, (MySuperPuperList, int, float)):
            self = self+other
        else:
            raise ValueError(f"other can be {type(self)} or parent classes, int or float and can not be {type(other)}")
        return self
    
def hinted_func(arg1: str, arg2:list, arg3:str|list, arg4:dict[Literal['name', 'second_name', 'username'], str], arg5: Any ) -> str:
    #играем с параметрами
    return f"arg1:{arg1}, arg2:{arg2}, arg3:{arg3}, arg4:{arg4}"

if __name__ == "__main__":
    #Метод, который вызывается при создании объекта класса, называется инициализатором
    c1 = Complex(1, 1)
    c2 = Complex(2, 2)

    #Можно создавать обычные методы
    c2.conj()
    print(f"abs: {c2.abs()}, phase: {c2.phase()}")
    
    #А можно "магические"
    #"Магические" методы определяют работу операторов/встроенных функций и т.п.
    is_eq = c1 == c2
    c3 = c2 + c1

    print(f"Is 1 real or imaginary part of c3? It is the {1 in c3} statement")
    print(abs(c3))
    #Можно сделать объект индексируемым
    print(f"c3: re = {c3[0]}, img = {c3['img']}")
    c3 = c1 + c2

    print(c3)
    print(reversed(c3))
    
    #Можно сделать объект вызываемым
    c3()


    #В питоне очень удобно реализовано наследование
    #На практике бывает очень удобно отнаследоваться от какого-то встроенного класса и добавить в него нужный вам функционал 
    lst = MySuperPuperList([1,2,3,4,5])
    neg_lst = MySuperPuperList([-1,-2,-3,-4,-5])

    #Теперь все складывается, как нам нужно!
    zeros_lst = lst + neg_lst
    zeros_lst += 100500
    #А какие могут быть проблемы с нашей реализацией?

    #Раз мы поняли, как все сломать, до давайте ломать!

    
    
    
    
    try:
        zeros_lst += "some_str"
    except Exception as ex:
        print(ex)
    x = hinted_func(1,1,1,1,1)