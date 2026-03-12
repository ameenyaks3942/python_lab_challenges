from collections import deque

def process_pipeline():
    # 1. Initialize
    application_inbox = deque()
    processed_history = [] # This acts as our Stack

    # 2. Ingest Data
    raw_data = [" TechCorp ", "bio-gen", "  Cloud_Nine  ", "Data_Flow "]
    for name in raw_data:
        clean_name = name.strip().lower()
        application_inbox.append(clean_name)

    # 3. Process (FIFO - First In, First Out)
    print("--- Processing Applications ---")
    while application_inbox:
        item = application_inbox.popleft()
        print(f"Approving: {item}")
        processed_history.append(item)

    # 4. Undo (LIFO - Last In, First Out)
    print("\n--- Simulating a Mistake (Undo) ---")
    if processed_history:
        last_item = processed_history.pop()
        print(f"Reverting approval for: {last_item}")

if __name__ == "__main__":
    process_pipeline()
