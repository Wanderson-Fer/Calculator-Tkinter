from tkinter import *


class Application:
    expression = ''

    def __init__(self, master=None):
        self.font_default = ('Verdana', '12')
        self.font_title = ('Verdana', '15', 'bold')

        print('Renderizando título...')
        self.c_title = Frame(master)
        self.c_title['padx'] = 25
        self.c_title['pady'] = 25
        self.c_title.pack()

        self.label_title = Label(self.c_title)
        self.label_title['text'] = 'Calculator'
        self.label_title['font'] = self.font_title
        self.label_title['width'] = 15
        self.label_title.pack()

        print('Renderizando resultados...')
        self.c_result = Frame(master)
        self.c_result['padx'] = 10
        self.c_result['pady'] = 20
        self.c_result.pack()

        self.equation = StringVar()

        self.entry_result = Entry(self.c_result)
        self.entry_result['font'] = self.font_default
        self.entry_result['textvariable'] = self.equation
        self.entry_result['width'] = 30
        self.entry_result.pack()

        print('Renderizando teclado...')
        self.c_keyboard = Frame(master)
        self.c_keyboard['padx'] = 10
        self.c_keyboard['pady'] = 20
        self.c_keyboard.pack()

        # Keyboard buttons settings
        self.BUTTON_HEIGHT = 2
        self.BUTTON_WIDTH = 7

        values = {
            '7': {'position': [1, 1], 'function': lambda: self.press('7')},
            '8': {'position': [1, 2], 'function': lambda: self.press('8')},
            '9': {'position': [1, 3], 'function': lambda: self.press('9')},
            '+': {'position': [1, 4], 'function': lambda: self.press('+')},
            '4': {'position': [2, 1], 'function': lambda: self.press('4')},
            '5': {'position': [2, 2], 'function': lambda: self.press('5')},
            '6': {'position': [2, 3], 'function': lambda: self.press('6')},
            '-': {'position': [2, 4], 'function': lambda: self.press('-')},
            '1': {'position': [3, 1], 'function': lambda: self.press('1')},
            '2': {'position': [3, 2], 'function': lambda: self.press('2')},
            '3': {'position': [3, 3], 'function': lambda: self.press('3')},
            'x': {'position': [3, 4], 'function': lambda: self.press('x')},
            '=': {'position': [4, 1], 'function': self.equal_expression},
            '0': {'position': [4, 2], 'function': lambda: self.press('0')},
            '.': {'position': [4, 3], 'function': lambda: self.press('.')},
            '/': {'position': [4, 4], 'function': lambda: self.press('/')}
        }

        for val in values:
            self.button = Button(self.c_keyboard)
            self.button['text'] = val
            self.button['font'] = self.font_default
            self.button['width'] = self.BUTTON_WIDTH
            self.button['height'] = self.BUTTON_HEIGHT
            self.button['command'] = values[val]['function']
            self.button.grid(
                row=values[val]['position'][0],
                column=values[val]['position'][1]
            )

    def press(self, number):
        self.expression += str(number)

        self.equation.set(self.expression)

    def equal_expression(self):
        try:
            self.equation.set(str(eval(self.expression)))
        except SyntaxError as e:
            self.equation.set('Deu Certo não')
            print(e)

        self.expression = ''


if __name__ == '__main__':
    print('Initializing...')

    print('Staging memory...')
    expression = ""

    print('Building interface...')
    root = Tk()
    Application(root)
    root.title('Calculator')

    print('Working...')
    root.mainloop()

    print('Goodbye')
