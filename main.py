from imports import *

class ScreenButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
    

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        horisontal_layout = BoxLayout()
        vertical_layout = BoxLayout(orientation='vertical', spacing=8, padding=15)
        text_label = Label(text='Обери лінію метро!')
        vertical_layout.add_widget(ScreenButton(self, direction='down', goal='first', text='Червона лінія.'))
        vertical_layout.add_widget(ScreenButton(self, direction='left', goal='third', text='Синя лінія.'))
        vertical_layout.add_widget(ScreenButton(self, direction='up', goal='second', text='Зелена лінія.'))
        horisontal_layout.add_widget(text_label)
        horisontal_layout.add_widget(vertical_layout)
        self.add_widget(horisontal_layout)
        
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vertical_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.8),
            pos_hint = {
                'center_x':0.5,
                'center_y':0.5
            }
        )
        self.vertical_layout2 = BoxLayout(
            orientation='horizontal',
            size_hint=(.7, .7),
            pos_hint = {
                'center_x':0.5,
                'center_y':1
            }
        )
        self.label1 = Label(text='Станція 1', pos_hint={'center_x':0, 'center_y':0.3})
        self.label2 = Label(text='?', pos_hint={'center_x':0.5, 'center_y':0.3})
        self.label3 = Label(text='Станція 2', pos_hint={'center_x':1, 'center_y':0.3})
        self.label4 = Label(text='___________________________________________________________________________________________', color='red')
        self.label5 = Label(text='Обери станцію "?"')
        self.button_1 = Button(text='Вибір 1')
        self.button_2 = Button(text='Вибір 2')  
        self.button_3 = Button(text='Вибір 3')
        self.button_4 = Button(text='Старт')  
        self.button_back = ScreenButton(self, direction='up', goal='main', text='Назад')
        self.vertical_layout.add_widget(self.label4)
        self.vertical_layout.add_widget(self.label5)
        self.vertical_layout.add_widget(self.button_1)
        self.vertical_layout.add_widget(self.button_2)
        self.vertical_layout.add_widget(self.button_3)
        self.vertical_layout.add_widget(self.button_4)
        self.vertical_layout.add_widget(self.button_back)
        self.vertical_layout2.add_widget(self.label1)
        self.vertical_layout2.add_widget(self.label2)
        self.vertical_layout2.add_widget(self.label3)
        self.add_widget(self.vertical_layout)
        self.add_widget(self.vertical_layout2)
        self.button_4.on_press= self.start
        
    def start(self):
        self.button_1.on_press= self.answer1
        self.button_2.on_press= self.answer2
        self.button_3.on_press= self.answer3
        global station_list, random_1
        self.button_4.text = 'Рестарт'
        station_list = ["Академ", "Житомирська", "Святошин", "Нивки", "Берестейська",
            "Шулявська", "Політех","Вокзальна", "Коледж зв'язку", "Театральна", "Хрещатик",
            "Общага", "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"]
        random_1 = random.randint(0, len(station_list)-3)
        random_list = random.sample(station_list, 2)
        random_list.append(station_list[random_1+1])
        self.label1.text = (station_list[random_1])
        self.label2.text = ('?')
        self.label3.text = (station_list[random_1+2])
        random_list2 = random.sample(random_list, 3)
        self.button_1.text = (random_list2[0])
        self.button_2.text = (random_list2[1])
        self.button_3.text = (random_list2[2])

    def answer1(self):
        if self.button_1.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer2(self):
        if self.button_2.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer3(self):
        if self.button_3.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vertical_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.8),
            pos_hint = {
                'center_x':0.5,
                'center_y':0.5
            }
        )
        self.vertical_layout2 = BoxLayout(
            orientation='horizontal',
            size_hint=(.7, .7),
            pos_hint = {
                'center_x':0.5,
                'center_y':1
            }
        )
        self.label1 = Label(text='Станція 1', pos_hint={'center_x':0, 'center_y':0.3})
        self.label2 = Label(text='?', pos_hint={'center_x':0.5, 'center_y':0.3})
        self.label3 = Label(text='Станція 2', pos_hint={'center_x':1, 'center_y':0.3})
        self.label4 = Label(text='___________________________________________________________________________________________', color='green')
        self.label5 = Label(text='Обери станцію "?"')
        self.button_1 = Button(text='Вибір 1')
        self.button_2 = Button(text='Вибір 2')  
        self.button_3 = Button(text='Вибір 3')
        self.button_4 = Button(text='Старт')  
        self.button_back = ScreenButton(self, direction='down', goal='main', text='Назад')
        self.vertical_layout.add_widget(self.label4)
        self.vertical_layout.add_widget(self.label5)
        self.vertical_layout.add_widget(self.button_1)
        self.vertical_layout.add_widget(self.button_2)
        self.vertical_layout.add_widget(self.button_3)
        self.vertical_layout.add_widget(self.button_4)
        self.vertical_layout.add_widget(self.button_back)
        self.vertical_layout2.add_widget(self.label1)
        self.vertical_layout2.add_widget(self.label2)
        self.vertical_layout2.add_widget(self.label3)
        self.add_widget(self.vertical_layout)
        self.add_widget(self.vertical_layout2)
        self.button_4.on_press= self.start
        
    def start(self):
        self.button_1.on_press= self.answer1
        self.button_2.on_press= self.answer2
        self.button_3.on_press= self.answer3
        global station_list, random_1
        self.button_4.text = 'Рестарт'
        station_list = ["Сирець", "Борн", "Лук'янівська", "Золоті Ворота", "Палац спорту",
            "Кловська", "Общага 2", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки",
            "Харківська", "Вирлиця", "Бориспільська", "Червоний Хутір"]
        random_1 = random.randint(0, len(station_list)-3)
        random_list = random.sample(station_list, 2)
        random_list.append(station_list[random_1+1])
        self.label1.text = (station_list[random_1])
        self.label2.text = ('?')
        self.label3.text = (station_list[random_1+2])
        random_list2 = random.sample(random_list, 3)
        self.button_1.text = (random_list2[0])
        self.button_2.text = (random_list2[1])
        self.button_3.text = (random_list2[2])

    def answer1(self):
        if self.button_1.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer2(self):
        if self.button_2.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer3(self):
        if self.button_3.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vertical_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.8),
            pos_hint = {
                'center_x':0.5,
                'center_y':0.5
            }
        )
        self.vertical_layout2 = BoxLayout(
            orientation='horizontal',
            size_hint=(.7, .7),
            pos_hint = {
                'center_x':0.5,
                'center_y':1
            }
        )
        self.label1 = Label(text='Станція 1', pos_hint={'center_x':0, 'center_y':0.3})
        self.label2 = Label(text='?', pos_hint={'center_x':0.5, 'center_y':0.3})
        self.label3 = Label(text='Станція 2', pos_hint={'center_x':1, 'center_y':0.3})
        self.label4 = Label(text='___________________________________________________________________________________________', color='blue')
        self.label5 = Label(text='Обери станцію "?"')
        self.button_1 = Button(text='Вибір 1')
        self.button_2 = Button(text='Вибір 2')  
        self.button_3 = Button(text='Вибір 3')
        self.button_4 = Button(text='Старт')  
        self.button_back = ScreenButton(self, direction='right', goal='main', text='Назад')
        self.vertical_layout.add_widget(self.label4)
        self.vertical_layout.add_widget(self.label5)
        self.vertical_layout.add_widget(self.button_1)
        self.vertical_layout.add_widget(self.button_2)
        self.vertical_layout.add_widget(self.button_3)
        self.vertical_layout.add_widget(self.button_4)
        self.vertical_layout.add_widget(self.button_back)
        self.vertical_layout2.add_widget(self.label1)
        self.vertical_layout2.add_widget(self.label2)
        self.vertical_layout2.add_widget(self.label3)
        self.add_widget(self.vertical_layout)
        self.add_widget(self.vertical_layout2)
        self.button_4.on_press= self.start
        
    def start(self):
        self.button_1.on_press= self.answer1
        self.button_2.on_press= self.answer2
        self.button_3.on_press= self.answer3
        global station_list, random_1
        self.button_4.text = 'Рестарт'
        station_list = ["Теремки", "Іподром", "Плаза", "Васильківська", "Голосіївська",
            "Деміївська", "Либідська", "Палац Україна", "Олімпійська", "Площа Льва Толстого",
            "Майдан", "Поштова площа", "Контрактова площа", "Тараса Шевченка", "Петрівка", "Оболонь",
            "Мінська", "Героїв Дніпра"]
        random_1 = random.randint(0, len(station_list)-3)
        random_list = random.sample(station_list, 2)
        random_list.append(station_list[random_1+1])
        self.label1.text = (station_list[random_1])
        self.label2.text = ('?')
        self.label3.text = (station_list[random_1+2])
        random_list2 = random.sample(random_list, 3)
        self.button_1.text = (random_list2[0])
        self.button_2.text = (random_list2[1])
        self.button_3.text = (random_list2[2])

    def answer1(self):
        if self.button_1.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer2(self):
        if self.button_2.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()

    def answer3(self):
        if self.button_3.text == station_list[random_1+1]:
            self.label5.text = (f'Правильно, це - {station_list[random_1+1]}')
            self.start()
        else:
            self.label5.text = (f'Ні, це - {station_list[random_1+1]}')
            self.start()


class Application(App):
    def build(self):
        self.icon = 'C:\Python\KiVy rofls\Metropolitenus dwa\icon.png'
        self.title = 'Metropolitenus'
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(FirstScreen(name='first'))
        screen_manager.add_widget(SecondScreen(name='second'))
        screen_manager.add_widget(ThirdScreen(name='third'))
        return screen_manager

if __name__ == '__main__':  
    app = Application()
    app.run()
