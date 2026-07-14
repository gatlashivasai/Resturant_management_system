def feedback():
    msg = input("Enter feedback: ")

    file = open("feedback.txt", "a")
    file.write(msg + "\n")
    file.close()

    print("Thank you for your feedback")