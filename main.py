import re
import tkinter as tk


def bmi_calculation(weight, height):
    global main_language

    if main_language == 0:
        if check_fields(weight, height):
            height = round((float(height) / 100) ** 2, 4)
            bmi = round(float(weight) / height, 2)

            if bmi <= 16:
                result = "Выраженный дефицит массы тела"
                color = "blue"
            elif 16 < bmi <= 18.5:
                result = "Недостаточная (дефицит) масса тела"
                color = "blue"
            elif 18.5 < bmi <= 25:
                result = "Норма"
                color = "green"
            elif 25 < bmi <= 30:
                result = "Избыточная масса тела (предожирение)"
                color = "green"
            elif 30 < bmi <= 35:
                result = "Ожирение 1 степени"
                color = "orange"
            elif 35 < bmi < 40:
                result = "Ожирение 2 степени"
                color = "red"
            else:
                result = "Ожирение 3 степени"
                color = "red"

            personal_bmi.configure(highlightbackground=color, highlightthickness=2,
                                   text="Ваш ИМТ: " + str(bmi) + " - " + result)
        else:
            personal_bmi.configure(highlightbackground="white", text="Поле с весом или поле с ростом заполнены не верно")
    else:
        if check_fields(weight, height):
            height = round((float(height) / 100) ** 2, 4)
            bmi = round(float(weight) / height, 2)

            if bmi <= 16:
                result = "Severe underweight"
                color = "blue"
            elif 16 < bmi <= 18.5:
                result = "Insufficient (deficit) body weight"
                color = "blue"
            elif 18.5 < bmi <= 25:
                result = "Norm"
                color = "green"
            elif 25 < bmi <= 30:
                result = "Overweight (preobesity)"
                color = "green"
            elif 30 < bmi <= 35:
                result = "Obesity 1 degree"
                color = "orange"
            elif 35 < bmi < 40:
                result = "Obesity 2 degree"
                color = "red"
            else:
                result = "Obesity 3 degree"
                color = "red"

            personal_bmi.configure(highlightbackground=color, highlightthickness=2,
                                   text="Your BMI: " + str(bmi) + " - " + result)
        else:
            personal_bmi.configure(highlightbackground="white", text="The field with weight or the field with height is filled incorrectly")


def check_fields(weight, height):
    if re.match(r'^\d+(\.\d)?$', weight) and re.match(r'^\d+(\.\d)?$', height):
        if 1 <= len(weight) <= 5 and 1 <= len(height) <= 5:
            try:
                float(weight)
                float(height)
                if float(height) > 0:
                    return True
            except:
                return False
        else:
            return False
    else:
        return False


def language(lang):
    global main_language
    if int(lang) == 0:
        root.title("ИМТ")
        main_label.configure(text="Программа расчета Индекса Массы Тела")
        weight_label.configure(text="Введите вес в килограммах: ")
        height_label.configure(text="Введите рост в сантиметрах: ")
        bmi_button.configure(text="Рассчитать ИМТ")
        main_language = 0
        if weight_entry.get() == "" or height_entry.get() == "":
            pass
        else:
            bmi_calculation(weight_entry.get(), height_entry.get())
    else:
        root.title("BMI")
        main_label.configure(text="Body Mass Index Program")
        weight_label.configure(text="Enter weight in kilograms: ")
        height_label.configure(text="Enter your height in centimeters: ")
        bmi_button.configure(text="Calculate BMI")
        main_language = 1
        if weight_entry.get() == "" or height_entry.get() == "":
            pass
        else:
            bmi_calculation(weight_entry.get(), height_entry.get())


main_language = 0

root = tk.Tk()

root.title("ИМТ")

root.geometry("800x600+350+50")

root.configure(bg="white")

main_label = tk.Label(root, bg="white", text="Программа расчета Индекса Массы Тела")
main_label.place(x=275, y=100)

weight_label = tk.Label(root, bg="white", text="Введите вес в килограммах: ")
weight_label.place(x=150, y=200)

weight_entry = tk.Entry(root, width=10)
weight_entry.place(x=325, y=200)

height_label = tk.Label(root, bg="white", text="Введите рост в сантиметрах: ")
height_label.place(x=150, y=250)

height_entry = tk.Entry(root, width=10)
height_entry.place(x=325, y=250)

bmi_button = tk.Button(root, width=15, text="Рассчитать ИМТ",
                       command=lambda: bmi_calculation(weight_entry.get(), height_entry.get()))
bmi_button.place(x=330, y=300)

personal_bmi = tk.Label(root, bg="white", text="")
personal_bmi.place(x=275, y=350)

lang_rus_button = tk.Button(root, width=10, text="Рус",
                            command=lambda: language("0"))
lang_rus_button.place(x=670, y=20)

lang_en_button = tk.Button(root, width=10, text="Eng",
                           command=lambda: language("1"))
lang_en_button.place(x=670, y=50)

img = tk.PhotoImage(file="resources/photo.png")
image_label = tk.Label(root, image=img)
image_label.place(x=250, y=400)

tk.mainloop()
