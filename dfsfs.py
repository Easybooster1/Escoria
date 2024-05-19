import tkinter as tk
from tkinter import messagebox

morse_code = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
    'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
    'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def download_update(self):
    try:
        response = requests.get('dfsfs.py')
        with open('dfsfs.py', 'wb') as f:
            f.write(response.content)
        messagebox.showinfo("Обновление Escoria", "Обновление прошло успешно")

    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибочка: {e}")


def check_update(self):
    try:
        response = requests.get('version.txt')
        if self.version == response.text:
            messagebox.showinfo("Обновление ПО", "Программа не требует обновления")
            return
        else:
            user_input = messagebox.askquestion("Обновление ПО", "Обнаружено обновление. Хотите обновить программу?")
            if user_input == "yes":
                self.download_update()
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось проверить обновления: {e}")


def create_menu(self):
    self.menu_bar = tk.Menu(self.window)
    self.window.config(menu=self.menu_bar)
    self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.menu_bar.add_cascade(label="Обновление", menu=self.help_menu)
    self.help_menu.add_command(label="Обновление ПО", command=self.check_update)


def encrypt_text():
    text = input_text.get("1.0", tk.END).upper().strip()
    encrypted_text = ''
    for char in text:
        if char in morse_code:
            encrypted_text += morse_code[char] + ' '
    if encrypted_text:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, encrypted_text)
    else:
        messagebox.showinfo("Ошибка", "Некорректный ввод")

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    decrypted_text = ''
    morse_code_reverse = {value: key for key, value in morse_code.items()}
    words = text.split(' / ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in morse_code_reverse:
                decrypted_text += morse_code_reverse[char]
        decrypted_text += ' '
    if decrypted_text:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, decrypted_text)
    else:
        messagebox.showinfo("Ошибка", "Некорректный ввод")

def copy_to_clipboard():
    text = output_text.get(1.0, tk.END).strip()
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        messagebox.showinfo("Успешно", "Результат скопирован в буфер обмена!")
    else:
        messagebox.showinfo("Ошибка", "Нет текста для копирования.")

window = tk.Tk()
window.title("Escoria")

input_label = tk.Label(window, text="Введите текст:")
input_label.pack()

input_text = tk.Text(window, height=5, width=30)
input_text.pack()

encrypt_button = tk.Button(window, text="Зашифровать", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Расшифровать", command=decrypt_text)
decrypt_button.pack()

output_label = tk.Label(window, text="Результат:")
output_label.pack()

output_text = tk.Text(window, height=5, width=30)
output_text.pack()

copy_button = tk.Button(window, text="Скопировать", command=copy_to_clipboard)
copy_button.pack()

window.mainloop()