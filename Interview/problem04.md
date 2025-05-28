## Problem 4: Design Pattern Comparison

### ✅ Overview

You have two implementations for creating language localizer objects:

* **Implementation 1:** Direct instantiation
* **Implementation 2:** Factory pattern

---

## Implementations

### Implementation 1: Direct Instantiation

```python
f = FrenchLocalizer()
e = EnglishLocalizer()
s = SpanishLocalizer()
```

* **Approach:** TThis method create manual instance of each class.
* **Drawback:** if more languages are added then it will be harder to maintain.

---

### Implementation 2: Factory Pattern

```python
def Localizer(language="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()
```

* **Approach:** Uses a dictionary to map language names to their respective classes and returns an instance dynamically.

---

## Comparison Analysis

| **Aspect**          | **Implementation 1** (Direct)           | **Implementation 2** (Factory Pattern) |
| ------------------- | --------------------------------------- | -------------------------------------- |
| **Pattern**         | Direct instantiation                    | Factory pattern                        |
| **Readability**     | Clear and explicit                      | Clean and centralized                  |
| **Maintainability** | Poor – changes scattered                | Excellent – single place to update     |
| **Flexibility**     | Static – all objects created upfront    | Dynamic – created on demand            |
| **Memory Usage**    | Higher – creates all objects            | Lower – creates only when needed       |
| **Error Handling**  | No built-in error handling              | Easy to validate and raise exceptions  |
| **Scalability**     | Poor – manual updates for each language | Excellent – just update dictionary     |

---

## Recommendation: Use Implementation 2 (Factory Pattern)

### Why?

1. **Encapsulation of Creation Logic:**

   * The factory hides the logic of object instantiation, making the main code cleaner.

2. **Better Maintainability:**

   * Adding a new language only requires updating the dictionary in one place.

3. **Dynamic Creation:**

   * Objects are created only when needed, which improves memory usage.

4. **Centralized Validation:**

   * Easier to handle unsupported languages via error handling.

5. **Future-Proof Design:**

   * Easily extendable to support features like caching, logging, or configuration injection.

---

## ✅ Enhanced Version of Factory Function (Final Code)

```python
def Localizer(language="English"):

    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()
```

