# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General Topics

- Summation and Product notation
- What is a series?
- Common series
- What is a derivative?
- What is the product rule?
- What is the chain rule?
- Common derivative rules
- What is a partial derivative?
- What is an indefinite integral?
- What is a definite integral?
- What is a double integral?

## Tasks

### 0. Sigma is for Sum
**Task:**
Find the sum represented by the following summation:

$$
\sum_{i=2}^{5} i
$$

**Options:**

- 3 + 4 + 5
- 3 + 4
- 2 + 3 + 4 + 5
- 2 + 3 + 4

### 1. The Greeks pronounce it sEEgma (mandatory)

**Task:**
Find the sum represented by the following summation:

$$
\sum_{k=1}^{4} 9i - 2k
$$

**Options:**

- 90 - 20
- 36i - 20
- 90 - 8k
- 36i - 8k

### 2. Pi is for Product (mandatory)

**Task:**
Find the product represented by the following summation:

$$
\prod_{i = 1}^{m} i
$$

**Options:**

- (m - 1)!
- 0
- (m + 1)!
- m!

### 3. The Greeks pronounce it pEE

**Task:**
Find the product represented by the following summation:

$$
\prod_{i = 0}^{10} i
$$

**Options:**

- 10!
- 9!
- 100
- 0

### 4. Hello, derivatives!

**Task:**
Find the derivative of the function:

$$
\frac{dy}{dx} \quad \text{where} \quad y = x^4 + 3x^3 - 5x + 1
$$

**Options:**

- 3x^3 + 6x^2 -4
- 4x^3 + 6x^2 - 5
- 4x^3 + 9x^2 - 5
- 4x^3 + 9x^2 - 4

### 5. A log on the fire

**Task:**
Find the derivative of the following function:

$$
\frac{d(x\ln(x))}{dx}
$$

**Options:**

- ln(x)
- \(\frac{1}{x} + 1\)
- ln(x) + 1
- \(\frac{1}{x}\)

### 6. It is difficult to free fools from the chains they revere

**Task:**
Find the derivative of the following function:

$$
\frac{d(\ln(x^2))}{dx}
$$

**Options:**

- \(\frac{2}{x}\)
- \(\frac{1}{x^2}\)
- \(\frac{2}{x^2}\)
- \(\frac{1}{x}\)

### 7. Partial truths are often more insidious than total falsehoods

**Task:**
Find the partial derivative with respect to \( y \) for the function:

$$
\frac{\partial f(x, y)}{\partial y} \quad \text{where} \quad f(x, y) = e^{xy}
$$

**Options:**

- \( e^{xy} \)
- \( ye^{xy} \)
- \( xe^{xy} \)
- \( e^{x} \)

### 8. Put it all together and what do you get?

**Task:**
Find the second partial derivative with respect to \( y \) and \( x \) for the function:

$$
\frac{\partial^2}{\partial y \partial x} (e^{x^2 y}) \quad \text{where} \quad \frac{\partial x}{\partial y} = \frac{\partial y}{\partial x} = 0
$$

**Options
### 9. Our life is the sum total of all the decisions we make every day, and those decisions are determined by our priorities

**Task:**
Write a function `def summation_i_squared(n):` that calculates:

$$
\sum_{i=1}^{n} i^2
$$

- \( n \) is the stopping condition
- Return the integer value of the sum
- If \( n \) is not a valid number, return `None`
- You are not allowed to use any loops

**Example Usage:**

```python
#!/usr/bin/env python3

summation_i_squared = __import__('9-sum_total').summation_i_squared

n = 5
print(summation_i_squared(n))

10. Derive happiness in oneself from a good day's work (mandatory)

Task: Write a function def poly_derivative(poly): that calculates the derivative of a polynomial:

    poly is a list of coefficients representing a polynomial.
        The index of the list represents the power of xx that the coefficient belongs to.
        Example: if f(x)=x3+3x+5f(x)=x3+3x+5, then poly is equal to [5, 3, 0, 1]
    If poly is not valid, return None
    If the derivative is 0, return [0]
    Return a new list of coefficients representing the derivative of the polynomial
#!/usr/bin/env python3

poly_derivative = __import__('10-matisse').poly_derivative

poly = [5, 3, 0, 1]
print(poly_derivative(poly))

11. Good grooming is integral and impeccable style is a must (mandatory)

Task: Solve the following integral:
3x2+C
3x2+C

Options:

    x4/4+Cx4/4+C
    x4+Cx4+C
    x4/3+Cx4/3+C

12. We are all an integral part of the web of life

Task: Solve the following integral:
e2y+C
e2y+C

Options:

    ey+Cey+C
    e2y/2+Ce2y/2+C
    ey/2+Cey/2+C

13. Create a definite plan for carrying out your desire and begin at once (mandatory)

Task: Solve the definite integral of:
3
3

Options:

    6
    9
    27

14. My talents fall within definite limitations (mandatory)

Task: Solve the following definite integral:
−1
−1

Options:

    0
    1
    undefined

### Instructions:

1. Add your code for each task in the appropriate files.
2. To run each Python function, make sure to use the appropriate testing script or command as indicated.
3. Ensure that all functions handle edge cases as described in the task descriptions.

---

This README provides clear organization with Markdown syntax for formatting math expressions and tasks. Let me know if you'd like any adjustments or additional information!
