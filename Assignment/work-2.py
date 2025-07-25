from collections import Counter, defaultdict


messages = []
n = int(input("Enter the number of messages: "))
for _ in range(n):
    msg = input()
    messages.append(msg)


data = []
for msg in messages:
    if ':' in msg:
        user, text = msg.split(':', 1)
        data.append((user.strip(), text.strip()))


while True:
    print("\nMenu:")
    print("1. Count total number of messages")
    print("2. Identify unique users")
    print("3. Count total words")
    print("4. Average words per message")
    print("5. Find the longest message")
    print("6. Most active user")
    print("7. Message count for a specific user")
    print("8. Most frequent word by a user")
    print("9. First and last message by a user")
    print("10. Check if a user is in the chat")
    print("11. Commonly repeated words")
    print("12. Display message timeline")
    print("13. User with longest average message")
    print("14. Messages mentioning a user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract questions")
    print("18. Reply ratio between users")
    print("19. Check for deleted messages")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Total messages: {len(data)}")

    elif choice == '2':
        users = {user for user, _ in data}
        print(f"Unique users in the chat: {users}")

    elif choice == '3':
        count = sum(len(text.split()) for _, text in data)
        print(f"Total words in the chat: {count}")

    elif choice == '4':
        total = sum(len(text.split()) for _, text in data)
        avg = total / len(data)
        print(f"Average words per message: {round(avg, 2)}")

    elif choice == '5':
        longest = max(data, key=lambda x: len(x[1]))
        print(f"Longest message: \"{longest[0]}: {longest[1]}\"")

    elif choice == '6':
        counts = Counter(user for user, _ in data)
        top_user, top_count = counts.most_common(1)[0]
        print(f"Most active user: {top_user} ({top_count} messages)")

    elif choice == '7':
        name = input("Enter user name: ")
        count = sum(1 for user, _ in data if user == name)
        print(f"Messages sent by {name}: {count}")

    elif choice == '8':
        name = input("Enter user name: ")
        words = []
        for user, msg in data:
            if user == name:
                words.extend(msg.lower().split())
        if words:
            top_word = Counter(words).most_common(1)[0][0]
            print(f"Most frequent word used by {name}: \"{top_word}\"")
        else:
            print("No messages found for that user.")

    elif choice == '9':
        name = input("Enter user name: ")
        user_msgs = [f"{u}: {t}" for u, t in data if u == name]
        if user_msgs:
            print(f"First message by {name}: \"{user_msgs[0]}\"")
            print(f"Last message by {name}: \"{user_msgs[-1]}\"")
        else:
            print(f"No messages found for {name}.")

    elif choice == '10':
        name = input("Enter user name: ")
        users = {user for user, _ in data}
        if name in users:
            print(f"User '{name}' is present in the chat.")
        else:
            print(f"User '{name}' not found in the chat.")

    elif choice == '11':
        words = [word.lower() for _, msg in data for word in msg.split()]
        repeated = {w for w, c in Counter(words).items() if c > 1}
        print(f"Common repeated words: {repeated}")

    elif choice == '12':
        print("Message Timeline:")
        for user, msg in data:
            print(f"{user}: {msg}")

    elif choice == '13':
        user_words = defaultdict(list)
        for user, msg in data:
            user_words[user].append(len(msg.split()))
        avg_lengths = {u: sum(v)/len(v) for u, v in user_words.items()}
        top_user = max(avg_lengths, key=avg_lengths.get)
        print(f"User with longest average message: {top_user} (avg {round(avg_lengths[top_user], 2)} words)")

    elif choice == '14':
        name = input("Enter name to search in messages: ").lower()
        count = sum(1 for _, msg in data if name in msg.lower())
        print(f"Messages mentioning '{name}': {count}")

    elif choice == '15':
        unique = list(dict.fromkeys(messages))
        print(f"Unique messages count: {len(unique)}")

    elif choice == '16':
        for msg in sorted(messages, key=lambda x: x.lower()):
            print(msg)

    elif choice == '17':
        for user, msg in data:
            if '?' in msg:
                print(f"{user}: {msg}")

    elif choice == '18':
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        reply_count = 0
        for i in range(1, len(data)):
            if data[i-1][0] == u1 and data[i][0] == u2:
                reply_count += 1
        print(f"Reply ratio from {u2} to {u1}: {reply_count} replies")

    elif choice == '19':
        deleted = sum(1 for _, msg in data if msg.lower() == "this message was deleted")
        print(f"Deleted messages found: {deleted}")

    elif choice == '0':
        break

    else:
        print("Invalid option. Please try again.")
