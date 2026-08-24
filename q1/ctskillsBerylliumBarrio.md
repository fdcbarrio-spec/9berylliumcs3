# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Franxianna Dawn
**Section:** 9-Beryllium
**Last Name:** Barrio
**Date:** August 25, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The PSHS canteen has difficulty serving students quickly and efficiently during lunch breaks, because ordering, payment, and tracking the food stocks are all handled manually.
---
## Step 2: Identify the Sub-Problems
1. Students take too much time deciding what to order.
2. The cashier needs to manually calculate the students' total and change.
3. The canteen lacks an efficient method to track which food items are running low.
4. The long ordering and payment process causes the queue to become crowded.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Students take too much time deciding what to order. | Abstraction | Display only important information such as the item/food name, price, and availability so students can make decisions more quickly. |
| The cashier needs to manually calculate the students' total and change. | Algorithm Design | Create a sequence that adds the selected food prices, receives the payment, calculates the change, and displays the result. |
| The canteen lacks an efficient method to track which food items are running low. | Pattern Recognition | Track the number of items sold and identify when the quantity repeatedly reaches a low number or stock. |
| The long ordering and payment process causes the queue to become crowded. | Decomposition | Divide the ordering process into smaller steps such as selecting food, calculating payment, completing the transaction, and updating the stock. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
I selected the sub-problem: **The cashier needs to manually calculate the students' total and change.**
### Pseudocode
START

1. Display the available food choices and their prices
2. Ask the student to select a food item
3. Get the food price
4. Calculate the total cost
5. Ask the student for payment
6. IF payment is enough THEN
    Calculate the change
    Give the change to the student
    Complete the transaction
   ELSE
    Display "Payment is insufficient."
   END IF

END
---