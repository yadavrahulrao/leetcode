#901. Online Stock Span


class StockSpanner:

    def __init__(self):
        # Stack to store (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # Pop from stack while current price >= top of stack price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        # Push current price and its span onto the stack
        self.stack.append((price, span))
        return span


# Example usage:
# obj = StockSpanner()
# print(obj.next(100))  # Output: 1
# print(obj.next(80))   # Output: 1
# print(obj.next(60))   # Output: 1
# print(obj.next(70))   # Output: 2
# print(obj.next(60))   # Output: 1
# print(obj.next(75))   # Output: 4
# print(obj.next(85))   # Output: 6
