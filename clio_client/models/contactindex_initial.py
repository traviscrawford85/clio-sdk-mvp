from enum import Enum


class ContactindexInitial(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    IDX_I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    IDX_O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
