import re

# ============================================================
# ДОПОМІЖНІ ФУНКЦІЇ БЕЗПЕЧНОГО ВВОДУ
# ============================================================
def safe_int(prompt, min_val=None, max_val=None):
    while True:
        raw = input(prompt).strip()
        if not re.fullmatch(r"-?\d+", raw):
            print("  ⚠ Введіть ціле число.")
            continue
        v = int(raw)
        if min_val is not None and v < min_val:
            print(f"  ⚠ Має бути >= {min_val}.")
            continue
        if max_val is not None and v > max_val:
            print(f"  ⚠ Має бути <= {max_val}.")
            continue
        return v


def safe_float(prompt, min_val=None, max_val=None, strict=False):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        if not re.fullmatch(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", raw):
            print("  ⚠ Введіть число.")
            continue
        v = float(raw)
        if min_val is not None:
            if (strict and v <= min_val) or (not strict and v < min_val):
                print(f"  ⚠ Має бути {'>' if strict else '>='} {min_val}.")
                continue
        if max_val is not None:
            if (strict and v >= max_val) or (not strict and v > max_val):
                print(f"  ⚠ Має бути {'<' if strict else '<='} {max_val}.")
                continue
        return v


def safe_int_list(prompt, elem_min, elem_max, max_len=100):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return []
        parts = [p for p in re.split(r"[,\s]+", raw) if p]
        ok = True
        values = []
        for p in parts:
            if not re.fullmatch(r"-?\d+", p):
                print(f"  ⚠ '{p}' — не ціле число.")
                ok = False
                break
            v = int(p)
            if not (elem_min <= v <= elem_max):
                print(f"  ⚠ {v} поза діапазоном [{elem_min}, {elem_max}].")
                ok = False
                break
            values.append(v)
        if not ok:
            continue
        if len(values) > max_len:
            print(f"  ⚠ Забагато елементів (макс {max_len}).")
            continue
        return values


# ============================================================
# РОЗВ'ЯЗКИ
# ============================================================
def reverse_string(s):
    return s[::-1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_array(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return dummy.next


def fibonacci(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def my_pow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x, n = 1.0 / x, -n
    result, base = 1.0, x
    while n:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return result


# ============================================================
# ВВІД ДАНИХ + ВИВІД РЕЗУЛЬТАТІВ
# ============================================================
def main():
    print("=" * 50)
    print("ВВЕДІТЬ ДАНІ ДЛЯ ВСІХ ЗАВДАНЬ")
    print("=" * 50)

    # ---- 1 ----
    s = input("1) Рядок для розвороту: ")
    while len(s) > 1000:
        print("  ⚠ Рядок задовгий (макс 1000).")
        s = input("1) Рядок для розвороту: ")

    # ---- 2 ----
    nums = safe_int_list(
        "2) Список чисел (0..100, через пробіл/кому, Enter = []): ",
        elem_min=0, elem_max=100, max_len=100
    )

    # ---- 3 ----
    n_fib = safe_int("3) n для Fibonacci (>= 0): ", min_val=0, max_val=100000)

    # ---- 4 ----
    n_stairs = safe_int("4) n для сходів (1..45): ", min_val=1, max_val=45)

    # ---- 5 ----
    while True:
        x = safe_float("5) x для pow (-100 < x < 100, x != 0): ",
                       min_val=-100, max_val=100, strict=True)
        if x == 0:
            print("  ⚠ x не може бути 0.")
            continue
        break
    n_pow = safe_int(f"5) n для pow ({-(2**31)}..{2**31-1}): ",
                     min_val=-(2**31), max_val=2**31 - 1)

    # ========================================================
    # ВИВІД УСІХ РЕЗУЛЬТАТІВ
    # ========================================================
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТИ")
    print("=" * 50)

    print(f"1) '{s}' -> '{reverse_string(s)}'")

    swapped = list_to_array(swap_pairs(build_list(nums)))
    print(f"2) {nums} -> {swapped}")

    print(f"3) F({n_fib}) = {fibonacci(n_fib)}")

    print(f"4) Способів піднятися на {n_stairs} сходів: {climb_stairs(n_stairs)}")

    try:
        res = my_pow(x, n_pow)
        print(f"5) {x} ^ {n_pow} = {res}")
    except OverflowError:
        print(f"5) {x} ^ {n_pow} = занадто велике число")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nПерервано.")