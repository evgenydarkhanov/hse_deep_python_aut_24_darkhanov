import time
from weakref_slots import AnimalField, Tiger, Lion, Bear


if __name__ == "__main__":

    BATCH_SIZE = 1_000_000

    print(f"СОЗДАНИЕ {BATCH_SIZE} ЭКЗЕМПЛЯРОВ")
    for animal, descr in zip(
                    [Tiger, Lion, Bear],
                    ["default class", "slots class", "weakref class"]
                    ):

        time_lst = []
        for i in range(10):
            start_time = time.time()
            for j in range(BATCH_SIZE):

                beast = animal(
                    AnimalField("name"),
                    AnimalField(1024)
                )

            total_time = time.time() - start_time
            time_lst.append(total_time)

            print(f"Loop {i + 1}\t\t{descr}\t\t{total_time:.5f} sec")
        print(f"average time:\t{(sum(time_lst)/len(time_lst)):.5f} sec\n")

    print()
    print(f"ИЗМЕНЕНИЕ АТРИБУТОВ {BATCH_SIZE} ЭКЗЕМПЛЯРОВ")
    for animal, descr in zip(
                    [Tiger, Lion, Bear],
                    ["default class", "slots class", "weakref class"]
                ):

        time_lst = []
        beast = animal(
            AnimalField(str(-1)),
            AnimalField(-1)
        )

        for i in range(10):
            start_time = time.time()
            for j in range(BATCH_SIZE):

                beast.name = AnimalField(str(j))
                beast.age = AnimalField(j)

            total_time = time.time() - start_time
            time_lst.append(total_time)

            print(f"Loop {i + 1}\t\t{descr}\t\t{total_time:.5f} sec")
        print(f"average time:\t{(sum(time_lst)/len(time_lst)):.5f} sec\n")
