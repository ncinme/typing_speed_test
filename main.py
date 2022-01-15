from tkinter import *
from tkinter import messagebox
from random import choice

COUNT = 60      # Time available to complete the teat

str1 = "way came when miss water do girl later large came new below mother far well only the thing all put try its close page under without always stop mile mile my before you leave along until people two from I will this most any is take because oil close turn too city air change feet these come than place fall study such time carry how talk these come must food will great air hear life same study best answer her upon might seem side once tell black own another up"
str2 = "go she walk father next two open come feet without soon letter why above after but watch every each follow hand up why just same saw so back song get well have cut always light while begin later father thought face mean at almost plant state end high country where earth the start spell say war later began one call long soon page river sea need be tell other must walk too again find begin now than next get girl up side call look point she at your idea another"
str3 = "miss story car watch year its man home enough at are plant grow into even go here tree later keep spell my very place own need once those high leave tell an form do own man to go took often and that can would night be large mother line those us or war why said letter hand land other car went if could own time only red much sun them its also us then when those white on paper from than here white set air while a school and play"
str4 = "want group has there while above him above help have just have her list run example that keep mile place are tell study men up turn too cut head out out new idea night last country walk through how never until than say learn also another sometimes men had where find be by really white often find often those mile is seem saw write study began page without call line show write important other no ask often left might run did number took father come word like more night work"
str5 = "her important which is has need once made just are out without paper start show must is sometimes show best me me need soon come off story water first almost began after should spell as out each because away boy open it different example where word it below we by the add her group set know man mean never sound oil over feet animal without high will will find over as each tree give keep be number when been she most year who would are who those sometimes song may"
str6 = "might add name are close were below fall family car under as feet open once black river were country get once after in small sea up on he take above number oil as world like once my number sound right eat big above hand think big change has say know below so grow light turn often been walk plant we right children saw along cut study animal would mother life for over first country mother show while little important let story car above a not men another hand get part"

str_list = [str1, str2, str3, str4, str5, str6]
random_str = choice(str_list)


# ---------------------------- RESULT ------------------------------- #
def result():
    word_count = 0
    word_list = random_str.split(" ")
    input_str = input_box.get('1.0', 'end').strip()     # Text widget get method adds \n in the end, hence strip()
    input_list = input_str.split(" ")
    duplicate_words = []

    for word in input_list:
        if word in word_list and word not in duplicate_words:       # find out number of correct, non-duplicate words
            duplicate_words.append(word)
            word_count += 1

    incorrect_words = len(input_list) - word_count
    return word_count, incorrect_words


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    input_box['state'] = 'normal'
    start_button['state'] = 'disabled'

    timer_display_label.config(text=f"{count}")

    if count > 0:
        window.after(1000, count_down, count - 1)       # counter going down by 1 second
    else:
        word_count, incorrect_words = result()
        messagebox.showinfo(title="Time's up!!", message="Click 'OK' to know your score")
        res = messagebox.askquestion('Your Score!!', message=f"Your typing speed is: {word_count} words/minute."
                                                             f"\n You typed {incorrect_words} incorrect words."
                                                             f"\n\nDo you want to try again?")
        if res == 'yes':
            input_box.delete('1.0', 'end')
            input_box['state'] = 'disabled'
            timer_display_label.config(text=f"{COUNT}")
            start_button['state'] = 'normal'
        elif res == 'no':
            messagebox.showinfo('Thank you!!', message='Keep practicing to improve your typing speed.')
            window.destroy()
        else:
            messagebox.showwarning('error', 'Something went wrong!')


# ---------------------------- Tkinter UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

# Labels
head_label = Label(text="One-minute typing test!!\nPress the space bar after each word. Do not type duplicate words.")
head_label.grid(row=1, column=2, columnspan=3)
timer_label = Label(text="Timer: ", width=5, anchor=E)
timer_label.grid(row=2, column=1)
timer_display_label = Label(text=f"{COUNT}", width=3, anchor=W)
timer_display_label.grid(row=2, column=2)
text_box_label = Label(text="Word List: ", width=8)
text_box_label.grid(row=3, column=1)
input_box_label = Label(text="Type Here: ", width=8)
input_box_label.grid(row=4, column=1)

# Text widget
text_box = Text(window, height=8, width=75, wrap=WORD)
text_box.grid(row=3, column=3, sticky="EW")
input_box = Text(window, height=8, width=75, wrap=WORD)
input_box.grid(row=4, column=3, sticky="EW")  # sticky="EW" ensures the alignment of subsequent columns

# Buttons
start_button = Button(text="Start", command=lambda: count_down(COUNT))
start_button.grid(row=5, column=3, sticky="EW")

# Insert the text string
text_box.insert('1.0', random_str)
text_box['state'] = 'disabled'  # user will not be able to enter any text
input_box['state'] = 'disabled'
input_box.focus()
# The position has the following format: 'line.column'. In the above example, ‘1.0’ means line 1, character 0,
# which is the first character of the first line on the text area.

window.mainloop()
