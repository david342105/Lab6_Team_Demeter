import sqlite3

def chatbot():
    conn = sqlite3.connect("vaccine_chatbot.db")  # Make sure this file exists
    cursor = conn.cursor()

    print("COVID-19 Chatbot is running. Please select a query: (0~5)")
    print("1. Look up someone's email and phone")
    print("2. Check if someone received the second dose")
    print("3. Look up someone's name using a phone number")
    print("4. List people who received only the first dose")
    print("5. List people who received both doses")
    print("0. Exit")

    while True:
        choice = input("\n Enter your choice (0-5): ").strip()

        if choice == "0":
            print("👋 Goodbye!")
            break

        elif choice == "1":
            fname = input("Enter First Name: ").strip()
            lname = input("Enter Last Name: ").strip()
            cursor.execute("""
                SELECT email, phone FROM vaccination
                WHERE LOWER(first_name)=LOWER(?) AND LOWER(last_name)=LOWER(?)
            """, (fname, lname))
            result = cursor.fetchone()
            if result:
                print("📧 Email:", result[0])
                print("📱 Phone:", result[1])
            else:
                print("No record found.")

        elif choice == "2":
            fname = input("Enter First Name: ").strip()
            lname = input("Enter Last Name: ").strip()
            cursor.execute("""
                SELECT date2 FROM vaccination
                WHERE LOWER(first_name)=LOWER(?) AND LOWER(last_name)=LOWER(?)
            """, (fname, lname))
            result = cursor.fetchone()
            if result:
                if result[0] and result[0].lower() != "nan":
                    print("✅ This person received the second dose on:", result[0])
                else:
                    print("❌ This person has not received the second dose yet.")
            else:
                print("No record found.")

        elif choice == "3":
            phone = input("Enter phone number: ").strip()
            cursor.execute("""
                SELECT first_name, last_name FROM vaccination
                WHERE phone = ?
            """, (phone,))
            result = cursor.fetchone()
            if result:
                print("👤 Name:", result[0], result[1])
            else:
                print("No record found for that phone number.")

        elif choice == "4":
            cursor.execute("""
                SELECT first_name, last_name FROM vaccination
                WHERE date2 IS NULL OR date2 = '' OR date2 = 'nan'
            """)
            results = cursor.fetchall()
            print("🟡 People who received only the first dose:")
            for r in results:
                print("-", r[0], r[1])
            print("👥 Total:", len(results))

        elif choice == "5":
            cursor.execute("""
                SELECT first_name, last_name FROM vaccination
                WHERE date2 IS NOT NULL AND date2 != '' AND date2 != 'nan'
            """)
            results = cursor.fetchall()
            print("🟢 People who received both doses:")
            for r in results:
                print("-", r[0], r[1])
            print("👥 Total:", len(results))

        else:
            print("⚠️ Please enter a number from 0 to 5.")

    conn.close()

# Start the chatbot
chatbot()
