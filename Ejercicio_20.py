import sys

sys.path.append(r"C:\Users\franc\Desktop\UADER\algoritmos_2026_todo")

from stack import Stack


OPPOSITE_DIRECTION = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste",
}


def register_move(movement_stack: Stack, steps: int, direction: str) -> None:
    direction = direction.lower().strip()

    if direction not in OPPOSITE_DIRECTION:
        print("direccion invalida")
        return

    if not isinstance(steps, int) or isinstance(steps, bool) or steps <= 0:
        print("la cantidad de pasos debe ser positiva")
        return

    movement_stack.push([direction, steps])


def generate_return_movements(movement_stack: Stack) -> Stack:
    return_stack = Stack()

    while movement_stack.size() > 0:
        direction, steps = movement_stack.pop()
        return_stack.push([OPPOSITE_DIRECTION[direction], steps])

    return return_stack


def show_movements(movement_stack: Stack) -> None:
    movement_stack.show()


if __name__ == "__main__":
    movements = Stack()

    register_move(movements, 5, "norte")
    register_move(movements, 3, "sureste")
    register_move(movements, 2, "oeste")

    print("movimientos originales:")
    show_movements(movements)

    movements_to_return = generate_return_movements(movements)

    print("movimientos para volver:")
    show_movements(movements_to_return)