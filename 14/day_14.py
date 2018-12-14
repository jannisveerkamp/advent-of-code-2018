def day_14_task_1(iterations):
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1

    for i in range(iterations + 10):
        new_score = recipes[elf_1] + recipes[elf_2]
        if new_score > 9:
            recipes.append(1)
        recipes.append(new_score % 10)

        elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
        elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

    return "".join(str(x) for x in recipes[iterations:iterations + 10])


def day_14_task_2(score_sequence):
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1
    length = len(score_sequence)
    score_ints = list(map(int, score_sequence))

    while True:
        new_score = recipes[elf_1] + recipes[elf_2]
        if new_score > 9:
            recipes.append(1)
            if recipes[-length:] == score_ints:
                break
        recipes.append(new_score % 10)
        if recipes[-length:] == score_ints:
            break

        elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
        elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

    return len(recipes) - length
