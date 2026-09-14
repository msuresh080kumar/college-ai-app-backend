# B.Sc AI Project 2 - College Enquiry AI Chatbot
import random

print("🤖 College Bot: Vanakkam da! Naan un College AI Bot. Kelvi Kelu!")

responses = {
    "fees": ["B.Sc AI fees per year 25k da", "Fees 25,000 - scholarship irukku"],
    "timing": ["College timing 9.30 AM to 3.30 PM da", "Morning 9.30 ku start"],
    "python": ["Python is heart of AI da!", "Python la thaan ellam AI pannuvom"],
    "ai": ["AI na Artificial Intelligence da, machine ah yosikka vekkardhu", "AI future da thambi!"],
    "hod": ["HOD name Dr. Kumar, romba strict illa friendly dhan"],
    "exam": ["Exam December la da, ippo irunthe padikalam"],
    "hello": ["Hello da! Epdi irukka?", "Hi da thambi!"],
    "bye": ["Bye da, nalaiku paaklam!", "Ok da, poitu va"]
}

while True:
    q = input("\nNee: ").lower()

    if q == "bye" or q == "exit":
        print("🤖 Bot: Bye da! All the best!")
        break

    answered = False
    for key in responses:
        if key in q:
            print(f"🤖 Bot: {random.choice(responses[key])}")
            answered = True
            break

    if not answered:
        print("🤖 Bot: Purila da, 'fees', 'timing', 'python', 'ai', 'exam' maadhiri kelu da")