from random import randint

N = 1000


def simulate(N):
    K = 0
    car_choice = randint(1, 3)

    for i in range(N):
        my_choice = randint(1, 3)

        if my_choice == car_choice:
            monte_choice = randint(1, 3)

            while monte_choice == car_choice:
                monte_choice = randint(1, 3)

        else:
            monte_choice = 6 - car_choice - my_choice
            second_choice = 6 - my_choice - monte_choice

            if second_choice == car_choice:
                K += 1

    return float(K) / float(N)

print(simulate(N))
