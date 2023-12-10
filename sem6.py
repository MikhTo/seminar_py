import math
class Complex:

    def __init__(self, real:float, img: float) -> None:
        self.real = real
        self.img = img
    
    def abs(self) -> float:
        return (self.real**2+self.img**2)**0.5
    
    def phase(self) -> float:
        return math.atan(self.img/self.real)
    
    def conj(self) -> None:
        self.img *= -1
    
    def __eq__(self, other) -> bool:
        return self.real, self.img == other.real, other.img
    
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
    
    def __getitem__(self, key):
        if key in (0,1):
            return self.real if key==0 else self.img
        elif key in ("real", "img"):
            return self.real if key=="real" else self.img
        else:
            raise KeyError(f"key can be either integer equal 0 and 1 or str equal \"real\" and \"img\", not {key}")
        
    def __reversed__(self):
        return Complex(self.img, self.real)

    def __call__(self, *args, **kwargs):
        print(f"Are you idiot or smth? I'm Complex number what do you suppose to get calling me with all these {args} and {kwargs}?")

    def __contains__(self, item):
        return item in (self.real, self.img)
    
    def __repr__(self) -> str:
        return f"{self.real}+{self.img}*i"
    
class MySuperPuperList(list):
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
    
from typing import Any, Literal
def hinted_func(arg1: str, arg2:list, arg3:str|list, arg4:dict[Literal['name', 'second_name', 'username'], str], arg5: Any ) -> str:
    #играем с параметрами
    return f"arg1:{arg1}, arg2:{arg2}, arg3:{arg3}, arg4:{arg4}"

if __name__ == "__main__":

    c1 = Complex(1, 1)
    c2 = Complex(2, 2)
    c2.conj()
    print(f"abs: {c2.abs()}, phase: {c2.phase()}")
    is_eq = c1 == c2
    c3 = c2 + c1
    print(abs(c3))
    print(f"c3: re = {c3[0]}, img = {c3['img']}")
    c3 = c1 + c2
    print(c1)
    x = hinted_func(1,1,1,1,1)