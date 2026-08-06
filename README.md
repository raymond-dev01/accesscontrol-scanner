# 🛂 Access Control Scanner

A simple command-line Python program that simulates a badge-based access control system. Visitors enter their name and badge number, and the program checks it against a list of revoked badges to grant or deny access.

## Features

- Continuously collects visitor names until "done" is entered
- Checks badge numbers against a set of revoked badges
- Grants or denies access based on badge status
- Displays a final, alphabetically sorted summary of approved and denied visitors
- Shows total counts for both approved and denied visitors

## How It Works

1. A set of revoked badge numbers is defined upfront.
2. The program loops, prompting for a visitor's name.
   - Typing `done` ends the loop.
3. For each visitor, their badge number is requested and checked:
   - If the badge is in the revoked set → **ACCESS DENIED**, name added to the denied list.
   - Otherwise → **ACCESS GRANTED**, name added to the approved list.
4. Once the loop ends, both lists are sorted alphabetically and printed as an **Access Summary**, along with the total number of approved and denied visitors.

## Requirements

- Python 3.x (no external libraries needed)

## Usage

Run the script from your terminal:

python access_control_scanner.py

Follow the prompts to enter visitor names and badge numbers. Type `done` when finished to see the summary.

### Example

Enter your name: Alice
What is your badge number? A1234
ACCESS GRANTED
Enter your name: Bob
What is your badge number? X1111
ACCESS DENIED
Enter your name: done
=====ACCESS SUMMARY=====
✅ Approved Visitors
 - Alice
⛔️ Denied Visitors
 - Bob
The total number of approved visitors are: 1
The total number of denied visitors are: 1

## Revoked Badge Numbers

The following badge numbers are treated as revoked by default:

- X1111
- C2222
- Z3333
- F4444

---

This project is being used just as a test to familiarize with GitHub Desktop.