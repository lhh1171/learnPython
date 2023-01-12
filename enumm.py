from enum import unique,IntEnum


@unique
class Sex(IntEnum):
    MALE=1
    FEMALE=2
    XXX=3

print(Sex["MALE"].value)