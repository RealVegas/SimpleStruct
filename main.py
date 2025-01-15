from typing import Any


class FILOStack:
    """
    Класс реализует простой стек первым вошел - последним вышел

    """

    def __init__(self) -> None:
        self.stack = []

    def push(self, item: Any) -> None:
        print(f'| {item} успешно добавлено в стек |')
        self.stack.append(item)

    def remove(self) -> Any:
        print(f'{self.stack[-1]} успешно удалено из стека')
        return self.stack.pop()

    @property
    def peek(self) -> Any:
        return self.stack[-1]

    @property
    def is_empty(self) -> bool:
        return len(self.stack) == 0

    @property
    def size(self) -> int:
        return len(self.stack)


class FIFOQueue:
    """
    Класс реализует простую очередь первым вошел - первым вышел

    """
    def __init__(self) -> None:
        self.queue = []

    def push(self, item: Any) -> None:
        print(f'| {item} успешно добавлен в очередь |')
        self.queue.append(item)

    def remove(self) -> Any:
        print(f'{self.queue[0]} успешно удален из очереди')
        return self.queue.pop(0)

    @property
    def peek(self) -> Any:
        return self.queue[0]

    @property
    def is_empty(self) -> bool:
        return len(self.queue) == 0

    @property
    def size(self) -> int:
        return len(self.queue)


if __name__ == '__main__':
    # Проверка стека
    stack = FILOStack()

    print('\n' + '-' * 40)
    print('Проверка стека\n')
    print('Проверка что стек пуст:', stack.is_empty)
    print('\n+-------------------------------------+')
    stack.push('Значение 1')
    stack.push('Значение 2')
    stack.push('Значение 3')
    print('|                                     |\n')
    print('Размер стека:', stack.size)
    print('Последний элемент в стеке:', stack.peek)
    stack.remove()
    print('Размер стека:', stack.size)
    print('Последний элемент в стеке:', stack.peek)
    print('Проверка что стек пуст:', stack.is_empty)

    # Проверка очереди
    queue = FIFOQueue()

    print('\n' + '-' * 40)
    print('Проверка очереди\n')
    print('Проверка что очередь пуста:', queue.is_empty)
    print('\n|                                      |')
    queue.push('Элемент 1')
    queue.push('Элемент 2')
    queue.push('Элемент 3')
    print('|                                      |\n')
    print('Размер очереди:', queue.size)
    print('Первый элемент в очереди:', queue.peek)
    queue.remove()
    print('Размер очереди:', queue.size)
    print('Первый элемент в очереди:', queue.peek)
    print('Проверка что очередь пуста:', queue.is_empty)
    print('\n' + '-' * 40)