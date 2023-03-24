"""LOTTO game. Provide 6 lucky numbers in range 1 to 49 and try your luck"""
from random import shuffle


def _check(id_: int) -> int:
    """
    function is checking if entered values are correct

    :param id_: holding what number you provide
    :return: providing number if correct
    """
    correct_value = 0
    while True:
        try:
            correct_value = int(input(f"Enter your {id_ + 1} lucky number: "))
        except ValueError:
            pass
        if 0 < correct_value < 50:
            return correct_value
        print("Enter number in range 1 to 49.")


def _enter_numbers() -> list[int, int, int, int, int, int]:
    """
    Add provided values to the list and checks if that values are not already on the list.
    Sorted them and print.

    :return: sorted list of six integers provided by player
    """
    lucky_numbers = []
    for i in range(6):
        while True:
            not_on_list = _check(i)
            if not_on_list not in lucky_numbers:
                break
            print("You already enter that number.")
        lucky_numbers.append(not_on_list)
    lucky_numbers.sort()

    print("Your lucky numbers: ")
    print(lucky_numbers)
    return lucky_numbers


def _lotto_numbers() -> list[int, int, int, int, int, int]:
    """
    Draw six unique LOTTO numbers in range 1 to 49
    :return: list of six unique numbers
    """
    lotek_list = list(range(1, 50))
    shuffle(lotek_list)
    print("LOTTO numbers: ")
    print(lotek_list[:6])
    return lotek_list[:6]


def _did_win(p_num: list[int, int, int, int, int, int],
             l_num: list[int, int, int, int, int, int]
             ) -> None:
    """
    Checking if player wins -> at less 3 guessed numbers and prints results.
    :param p_num: player numbers
    :param l_num: LOTTO numbers
    :return: None
    """
    strikes = []
    for values_ in p_num:
        if values_ in l_num:
            strikes.append(values_)
    if len(strikes) < 3:
        print(f"You got {len(strikes)} strikes. Better luck next time!")
    elif len(strikes) < 6:
        print(f"You win! You got {len(strikes)} strikes!")
    else:
        print("!!!!!! YOU WIN !!!!!!\nYou got all the numbers!!!!")


def main() -> None:
    """
    Main function.
    :return: None
    """
    player_numbers = _enter_numbers()
    lotto_numbers = _lotto_numbers()
    _did_win(player_numbers, lotto_numbers)


main()
