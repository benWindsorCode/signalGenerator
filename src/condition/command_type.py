from enum import Enum


class Command_Type(Enum):
    IF = 0
    AND = 1
    OR = 2
    EXPRESSION = 3 # Used to represent an atomic expression to eval like x > 50
