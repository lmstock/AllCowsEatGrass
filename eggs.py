# the sea will outlive us all
# 
# petrichor

from dataclasses import dataclass, field


@dataclass 
class Char:
    frog: int
    dog: list
    cat: list = field(default_factory=lambda: ["wander", 3, 0, 7])



    def internal_function(self):
        print(self)

    def add_something(self):
        self.frog = self.cat[1] + self.dog[0]
        print("internal ", self.frog)


def external_function(x):
    x.fish = x.cat[2] + x.dog[2]
    print("exteranl ", x.frog)



egg = Char(4, [4,5,7])
egg.internal_function()
egg.add_something()
egg.internal_function()

external_function(egg)
print("final result  ", egg.frog)