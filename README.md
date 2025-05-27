## Implemented Solution Explanation
# Task no 1
```
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
```
You can find this solution in [problem01.py](problem01.py). Just call letter_combinations with any input string of digits to get all possible letter combinations.

How it works
The goal is to take a string of digits (like "23") and return all possible letter combinations based on a phone keypad.

A dictionary phone_map links digits to their letters.

If any digit is outside 2-9, it raises an error.

The function uses backtracking (a recursive approach) to generate all combinations by adding letters one by one.

Once a full combination is created, it gets added to the results list.

## Task no 2

```
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);
```
Select the Customer ID from Customer and then Group them by their customer_id.
Then after Grouping we can apply aggregate functions.
Choose distict all products from Product.
In short 
```This query finds all customers who have purchased every product available in the Product table.```

## Task no 3
Print Line no 10 using bash script or linux command.
```
if [ -z "$1" ]; then
    echo "Usage: $0 <filename.txt>"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "$FILE not found!"
    exit 1
fi

if [ $(wc -l < "$FILE") -lt 10 ]; then
    echo "$FILE has less than 10 lines."
    exit 1
fi

sed -n '10p' "$FILE"
```
### What it does?
Checks if a filename was provided.

Verifies the file exists.

Checks if it has at least 10 lines.

Prints the 10th line of the file.
### How to Run?
In terminal in the same directory and change the Permisions with
```chmod +x print_line_10.sh```

and then with the command replace filename.txt with the actual file_path you want to print the line

```
./print_line_10.sh filename.txt
```
### Linux Commands
Command no 01: ```sed -n '10p' file.txt```

Command no 02: ```sed -n '10p' file.txt```

## Task no 04
Task no 4 is done in another Markdown as it was Explanatory Task.

Click this  to visit:  [Task no 04](problem04.md)

## Task no 05
Given a Kaggle Dataset for Road Sign Detection

[Dataset Link](https://www.kaggle.com/datasets/andrewmvd/road-sign-detection)

Two models were trained on this dataset:

YOLOv8 Small

YOLOv8 Nano

The small model was trained by tuning parameters, while the nano model was used as a starting baseline.

The Training result of yolov8 small:

YOLO_v8 Small: [CSV File](Task_05/yolov8_small.csv)

YOLO_v8 Nano: [CSV File](Task_05/yolov8_nano.csv)

Data was downloaded locally (due to internet limitations) and converted to YOLO format, which uses text files with bounding box coordinates and class names.

The training script is available here:
[Training Script](Task_05\Road_sign_detection.ipynb)

This notebook contains the full training code, evaluation metrics, and testing on sample images.



The detail Report of both the models is 
## 📊 Model Evaluation Report: YOLOv8 Nano vs YOLOv8 Small

### 🔍 Comparison Table (Best Epochs)

| Metric                  | YOLOv8 Nano        | YOLOv8 Small       |
|-------------------------|--------------------|---------------------|
| Precision               | 0.86052            | 0.81446             |
| Recall                  | 0.68307            | 0.68161             |
| mAP@0.5                 | **0.78968**        | 0.76341             |
| mAP@0.5:0.95            | **0.63310**        | 0.57919             |
| Validation Box Loss     | **0.72928**        | 0.74097             |
| Validation Class Loss   | **0.96346**        | 1.25851             |
| Validation DFL Loss     | **0.92772**        | 0.98646             |

> ✅ **Winner: YOLOv8 Nano**
- Higher accuracy (mAP, precision)
- Lower validation losses
- Lighter and faster for inference

---

### 📝 Model Selection Justification

**YOLOv8 Nano** is the preferred model for this task because:

- It achieves **better performance** across most metrics, including mAP and losses.
- It has **lower computational cost**, which makes it more suitable for real-time applications and deployment on edge devices.

---
⚙️ Note: The YOLOv8 Small model, with proper parameter tuning and longer training, can also achieve higher accuracy. However, for this experiment, YOLOv8 Nano performed better out-of-the-box.
---
## 💡 Future Work: Exploring EfficientNet for Detection

While YOLOv8 Nano performs well, future work may explore the use of **EfficientNet** or **EfficientDet**, especially for tasks requiring stronger feature extraction.

### Why EfficientNet?
- Highly **efficient CNN** backbone for feature extraction
- **Pretrained models** available (ImageNet)
- Scales from B0 to B7 for different hardware constraints

### Next Steps:
1. Use EfficientNet as a **backbone** for object detection (e.g., with YOLOv5, RetinaNet, or Faster R-CNN).
2. Alternatively, use **EfficientDet**, which combines EfficientNet + BiFPN + object detection heads.
3. Train on the same dataset and compare performance (mAP, inference time, etc.)

---

### 📦 References

- [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics)
- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [EfficientDet PyTorch Implementation](https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch)

