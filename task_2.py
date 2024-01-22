from collections import deque


def check_palindrom(string):
    formatted_string = string.replace(" ", "").lower()
    deque_string = deque(formatted_string)

    while len(deque_string) >= 2:
        left_symbol = deque_string.popleft()
        right_symbol = deque_string.pop()

        if left_symbol != right_symbol:
            return False

    return True


if __name__ == "__main__":
    print(check_palindrom("s stRing G nir TSs"))
    print(check_palindrom("Ola Salo"))
    print(check_palindrom("Never odd or even"))
    print(check_palindrom("Not a palindrome"))
