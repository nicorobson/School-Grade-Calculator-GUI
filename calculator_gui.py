import tkinter as tk
from tkinter import ttk

MAIN_WIDTH = 650
MAIN_HEIGHT = 250
RESULTS_WIDTH = 650
RESULTS_HEIGHT = 300
GRID_PAD = 5

main_window = tk.Tk()
main_window.title('Grade Calculator')

main_window.geometry(f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

welcome_menu_string = """
~Please select one of the options below~\n
Use the Course Grade Calculator if you have received all your assignment grades, and would like to see your final mark.
Use the Exam Grade Calculator to see what you need on your final exam to achieve your desired course mark.
"""
exam_mode_string = """
This mode tells you the mark you need on your final exam, in order to achieve a certain course grade.
"""
course_mode_string = """
This mode computes your final course mark based on the weightage of the course's assignments. 
(This includes the course's tests, labs, assignments, etc.)\n
Please enter the following information:
"""

def course_calculator():
    results_window = tk.Tk()
    results_window.title('Course Grade Mode')
    results_window.geometry(
        f'{RESULTS_WIDTH}x{RESULTS_HEIGHT}+{int(results_window.winfo_screenwidth() / 2 - RESULTS_WIDTH / 2)}+{int(results_window.winfo_screenheight() / 2 - RESULTS_HEIGHT / 2)}')
    results_window.columnconfigure(0, weight=1)
    results_window.columnconfigure(1, weight=1)
    results_window.columnconfigure(2, weight=1)
    ttk.Label(results_window, text=course_mode_string).pack(padx=GRID_PAD, pady=GRID_PAD)

    ttk.Label(results_window, text="Course Name").pack(padx=GRID_PAD, pady=GRID_PAD)  
    input_txt = tk.Text(results_window, height = 1, width = 20)
    input_txt.pack()

    ttk.Label(results_window, text="Number of Assignments").pack(padx=GRID_PAD, pady=GRID_PAD)  
    input_txt2 = tk.Text(results_window, height = 1, width = 20)
    input_txt2.pack()

    def get_input():
        inp = input_txt.get(1.0, "end-1c")
        lbl.config(text = "Input: " + inp)
        inp2 = input_txt2.get(1.0, "end-1c")
        lbl2.config(text = "Input: " + inp2)

    lbl = tk.Label(results_window, text = "")
    lbl.pack()
    lbl2 = tk.Label(results_window, text = "")
    lbl2.pack()

    submit_button = tk.Button(results_window, text = "Submit", command = get_input)
    submit_button.pack()

def exam_calculator():
    results_window = tk.Tk()
    results_window.title('Exam Grade Mode')
    results_window.geometry(f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(results_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(results_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')
    results_window.columnconfigure(0, weight=1)
    results_window.columnconfigure(1, weight=1)
    results_window.columnconfigure(2, weight=1)
    ttk.Label(results_window, text=exam_mode_string).pack(padx=GRID_PAD, pady=GRID_PAD) 

ttk.Label(main_window, text=welcome_menu_string).grid(
    row=0, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Label(main_window, text="Options").grid(
    row=1, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Course Grade Calculator', command=course_calculator).grid(
    row=2, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Exam Grade Calculator', command=exam_calculator).grid(
    row=3, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Quit', command=main_window.destroy).grid(
    row=4, column=0, padx=GRID_PAD, pady=GRID_PAD)       

if __name__ == '__main__':
    main_window.mainloop()