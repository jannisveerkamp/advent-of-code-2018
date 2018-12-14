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
