import operator
from typing import Callable, Dict


class Operation:
    """Represents a mathematical operation with its precedence and logic."""
    def __init__(self, symbol: str, precedence: int, evaluator: Callable[[int, int], int]):
        self.symbol = symbol
        self.precedence = precedence
        self.evaluator = evaluator

class OperatorRegistry:
   
    def __init__(self):
        self._operations: Dict[str, Operation] = {}

    def register(self, operation: Operation) -> None:
        self._operations[operation.symbol] = operation

    def get(self, symbol: str) -> Operation:
        return self._operations.get(symbol)

    def is_operator(self, symbol: str) -> bool:
        return symbol in self._operations

# ==========================================
# 2. Core Business Logic (SRP)
# ==========================================

class NotationConverter:
    """Handles parsing and converting infix expressions."""
    def __init__(self, registry: OperatorRegistry):
        self.registry = registry

    def infix_to_postfix(self, infix: str) -> str:
        stack = []
        output = []
        
        for char in infix:
            if char.isdigit():
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the '('
            elif self.registry.is_operator(char):
                current_op = self.registry.get(char)
                while (stack and stack[-1] != '(' and 
                       self.registry.get(stack[-1]).precedence >= current_op.precedence):
                    output.append(stack.pop())
                stack.append(char)
                
        while stack:
            output.append(stack.pop())
            
        return "".join(output)

    def infix_to_prefix(self, infix: str) -> str:
        reversed_infix = infix[::-1]
        
        swapped = []
        for char in reversed_infix:
            if char == '(': swapped.append(')')
            elif char == ')': swapped.append('(')
            else: swapped.append(char)
            
        stack = []
        output = []
        
        
        for char in swapped:
            if char.isdigit():
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif self.registry.is_operator(char):
                current_op = self.registry.get(char)
                while (stack and stack[-1] != '(' and 
                       self.registry.get(stack[-1]).precedence > current_op.precedence):
                    output.append(stack.pop())
                stack.append(char)
                
        while stack:
            output.append(stack.pop())
            
        return "".join(output)[::-1]

class NotationEvaluator:
    """Handles the evaluation of postfix and prefix expressions."""
    def __init__(self, registry: OperatorRegistry):
        self.registry = registry

    def evaluate_postfix(self, postfix: str) -> int:
        stack = []
        for char in postfix:
            if char.isdigit():
                stack.append(int(char))
            elif self.registry.is_operator(char):
                right_operand = stack.pop()
                left_operand = stack.pop()
                op = self.registry.get(char)
                result = op.evaluator(left_operand, right_operand)
                stack.append(result)
        return stack[0]

    def evaluate_prefix(self, prefix: str) -> int:
        stack = []
        # Evaluate from right to left
        for char in reversed(prefix):
            if char.isdigit():
                stack.append(int(char))
            elif self.registry.is_operator(char):
                left_operand = stack.pop()
                right_operand = stack.pop()
                op = self.registry.get(char)
                result = op.evaluator(left_operand, right_operand)
                stack.append(result)
        return stack[0]


math_registry = OperatorRegistry()
math_registry.register(Operation('+', 1, operator.add))
math_registry.register(Operation('-', 1, operator.sub))
math_registry.register(Operation('*', 2, operator.mul))

converter = NotationConverter(math_registry)
evaluator = NotationEvaluator(math_registry)


def infix_to_postfix(infix: str) -> str:
    return converter.infix_to_postfix(infix.replace(" ", ""))

def infix_to_prefix(infix: str) -> str:
    return converter.infix_to_prefix(infix.replace(" ", ""))

def evaluate_postfix(postfix: str) -> int:
    return evaluator.evaluate_postfix(postfix.replace(" ", ""))

def evaluate_prefix(prefix: str) -> int:
    return evaluator.evaluate_prefix(prefix.replace(" ", ""))


if __name__ == "__main__":
    print("--- Mathematical Expression Notation Converter ---")
    print("Rules: Single digits only. Supported operators: +, -, *")
    
    # Ask the user to enter a mathematical expression
    user_input = input("\nEnter a mathematical expression in Infix notation (e.g., 3+5*(2-8)): ")
    
    # Strip spaces in case the user types "3 + 5" instead of "3+5"
    clean_input = user_input.replace(" ", "")
    
    print(f"\n[0] Original Infix: {clean_input}")
    
    # 1. Convert to Postfix
    postfix_result = infix_to_postfix(clean_input)
    print(f"[1] Postfix Notation: {postfix_result}")
    
    # 2. Convert to Prefix
    prefix_result = infix_to_prefix(clean_input)
    print(f"[2] Prefix Notation:  {prefix_result}")
    
    # 3. Evaluate Postfix
    eval_postfix = evaluate_postfix(postfix_result)
    print(f"[3] Postfix Evaluation Result: {eval_postfix}")
    
    # 4. Evaluate Prefix
    eval_prefix = evaluate_prefix(prefix_result)
    print(f"[4] Prefix Evaluation Result:  {eval_prefix}")