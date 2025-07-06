from typing import List

def letter_combinations(digits: str) -> List[str]:
    
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    for ch in digits:
        if ch not in phone_map:
            raise ValueError(f"Invalid digit '{ch}' in input. Allowed digits are 2-9.")

    def backtrack(index: int, current_combination: str):
        if index == len(digits):
            result.append(current_combination)
            return
        
        current_digit = digits[index]
        letters = phone_map[current_digit]
        
        for letter in letters:
            backtrack(index + 1, current_combination + letter)

    result = []
    backtrack(0, "")
    return result

if __name__ == "__main__":
    try:
        print(letter_combinations("2")) 
        print(letter_combinations("23"))     
        print(letter_combinations(""))       
        print(letter_combinations("a"))  
        print(letter_combinations("1")) 
    except ValueError as ve:
        print("Error:", ve)

    print("Goodbye!")
