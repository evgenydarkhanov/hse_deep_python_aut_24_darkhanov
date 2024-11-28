from memory_profiler import profile
from weakref_slots import AnimalField, Tiger, Lion, Bear


@profile
def memory_func(animal, n: int) -> None:
    animal_lst = []

    for _ in range(n):
        beast = animal(
            AnimalField("name"),
            AnimalField(1024)
            )
        animal_lst.append(beast)

    for j in range(n):
        animal_lst[j].name = AnimalField(str(j))
        animal_lst[j].age = AnimalField(j)


if __name__ == "__main__":

    BATCH_SIZE = 10_000

    for animal, descr in zip(
                    [Tiger, Lion, Bear],
                    ["default class", "slots class", "weakref class"]
                    ):

        print(descr)
        memory_func(animal, BATCH_SIZE)
