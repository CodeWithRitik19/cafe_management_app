# 🍽️ Hotel Menu Ordering System  
*A minimal, interactive command-line food ordering app built in Python.*

---

## 📌 Overview

The **Hotel Menu Ordering System** is a simple yet extensible Python-based CLI program that simulates a restaurant ordering workflow.  
It allows the user to browse the menu, select items, validate availability, and receive a total bill.

This project demonstrates:
- Python dictionaries & data structures  
- Input handling & validation  
- Conditional logic  
- Real-world menu ordering flow  

---

## 🚀 Features

### ✅ Predefined Menu  
A Python dictionary stores menu items and prices for instant lookup.

### ✅ User-Friendly CLI  
Displays the full hotel menu and guides the user step-by-step.

### ✅ Input Validation  
Validates ordered items against the menu to avoid invalid selections.

### ✅ Billing System  
Automatically calculates the total cost of all items.

### ✅ Optional Additional Orders  
User can choose to add more items.

---

## 🧠 Program Flow (Diagram)

```mermaid
flowchart TD
    A[Start Program] --> B[Display Menu]
    B --> C[Ask user for first item]
    C --> D{Item in menu?}
    D -->|Yes| E[Add price to total]
    D -->|No| F[Show item not available]
    E --> G[Ask if user wants another item]
    F --> G
    G -->|Yes| H[Input second item]
    G -->|No| I[Display total]
    H --> J{Item exists?}
    J -->|Yes| K[Add price to total]
    J -->|No| L[Show not available]
    K --> I
    L --> I
    I --> M[End]
git clone https://github.com/yourusername/hotelmenu.git
cd hotelmenu
