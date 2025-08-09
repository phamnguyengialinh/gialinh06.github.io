import csv

def count_users(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header if present
        return sum(1 for row in reader)

if __name__ == "__main__":
    user_count = count_users('abc.csv')
    print(f"Number of users đã phát hiện: {user_count}")