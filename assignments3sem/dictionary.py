def compute_average(records): 
    total = sum(records.values()) 
    count = len(records) 
    return total / count if count > 0 else 0 

def find_max_min(records): 
    non_zero_values = [val for val in records.values() if val > 0] 
    if not non_zero_values:   
        return max(records.values())
    max_borrow = max(records.values()) 
    min_borrow = min(non_zero_values) 
    return max_borrow, min_borrow 

def count_zero_borrowers(records): 
    return list(records.values()).count(0) 

def find_mode(records): 
    from collections import Counter 
    non_zero_values = [val for val in records.values() if val > 0] 
    if not non_zero_values:   
        return None 
    freq = Counter(non_zero_values) 
    most_common = freq.most_common(1)[0] 
    return most_common 

# ---------------- Take borrow_records from user ----------------
borrow_records = {}
n = int(input("Enter number of people: "))

for i in range(n):
    name = input(f"Enter name of person {i+1}: ")
    books = int(input(f"Enter number of books borrowed by {name}: "))
    borrow_records[name] = books

# ---------------- Menu ----------------
while (True):
    print("\nChoose an option:") 
    print("1. Compute average books borrowed") 
    print("2. Find maximum and minimum (nonzero) books borrowed") 
    print("3. Count number of people who borrowed 0 books") 
    print("4. Find most common (mode, nonzero) books borrowed") 
    print("5. Exit") 

    choice = input("Enter your choice (1-5): ") 

    if choice == "1": 
        average = compute_average(borrow_records) 
        print(f"Average books borrowed: {average:.2f}") 

    elif choice == "2": 
        max_borrow, min_borrow = find_max_min(borrow_records) 
        print(f"Maximum books borrowed: {max_borrow}") 
        if min_borrow is not None: 
            print(f"Minimum (nonzero) books borrowed: {min_borrow}") 
        else: 
            print("No nonzero borrow records found.") 

    elif choice == "3": 
        zero_count = count_zero_borrowers(borrow_records) 
        print(f"Number of people who borrowed 0 books: {zero_count}") 

    elif choice == "4": 
        mode_borrow = find_mode(borrow_records) 
        if mode_borrow is not None: 
            print(f"Most common (mode, nonzero) books borrowed: {mode_borrow}") 
        else: 
            print("No mode found (all borrowed 0).") 

    elif choice == "5": 
        print("Exiting program.") 
        break

    else: 
        print("Invalid choice. Please enter a number from 1 to 5.") 

