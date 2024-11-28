import cProfile
from weakref_slots import AnimalField, Tiger, Lion, Bear


def profile_default(n: int) -> None:
    animal_lst = []

    for _ in range(n):
        beast = Tiger(
            AnimalField("name"),
            AnimalField(1024)
            )
        animal_lst.append(beast)

    for j in range(n):
        animal_lst[j].name = AnimalField(str(j))
        animal_lst[j].age = AnimalField(j)


def profile_slots(n: int) -> None:
    animal_lst = []

    for _ in range(n):
        beast = Lion(
            AnimalField("name"),
            AnimalField(1024)
            )
        animal_lst.append(beast)

    for j in range(n):
        animal_lst[j].name = AnimalField(str(j))
        animal_lst[j].age = AnimalField(j)


def profile_weakref(n: int) -> None:
    animal_lst = []

    for _ in range(n):
        beast = Bear(
            AnimalField("name"),
            AnimalField(1024)
            )
        animal_lst.append(beast)

    for j in range(n):
        animal_lst[j].name = AnimalField(str(j))
        animal_lst[j].age = AnimalField(j)


if __name__ == "__main__":

    BATCH_SIZE = 100_000

    # to run from the terminal
    # profile_default(BATCH_SIZE)
    # profile_slots(BATCH_SIZE)
    # profile_weakref(BATCH_SIZE)

    # to run from the code
    print("DEFAULT CLASS")
    cProfile.run("profile_default(BATCH_SIZE)")

    print("CLASS WITH SLOTS")
    cProfile.run("profile_slots(BATCH_SIZE)")

    print("CLASS WITH WEAKREF")
    cProfile.run("profile_weakref(BATCH_SIZE)")
