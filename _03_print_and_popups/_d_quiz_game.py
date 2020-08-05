from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    q1 = simpledialog.askstring(title="q1", prompt="What is the capital of the UK")
    #      // 3.  Use an if statement to check if their answer is correct
    if q1 == "london":

        score = score + 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    q2 = simpledialog.askstring(title="q1", prompt="What is the capital of the China")
    q3 = simpledialog.askstring(title="q1", prompt="What is the capital of the Sweden")
    q4 = simpledialog.askstring(title="q1", prompt="What is the capital of the France")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    if q2 == "Bejing":
        score = score + 1
    if q3 == "Stockholm":
        score = score + 1
    if q4 == "Paris":
        score = score + 1
    messagebox.showinfo(title="hello",message = "You got" + str(score))
    # Run the window's .mainloop() method
window.mainloop()