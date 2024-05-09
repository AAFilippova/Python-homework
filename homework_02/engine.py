"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: int
    pistons: int()

# def main():
#     engine_1 = Engine(100,500)
#     print(engine_1)
#
#
#
# if __name__=="__main__":
#     main()