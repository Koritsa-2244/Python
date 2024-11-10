import enum
from enum import Enum
class discipline(Enum):
    class_rock = 1
    class_ice = 2
    skyrunning = 3
    class_height_techn = 4
    speed = 5
    lead = 6
    bouldering = 7

class Athletes:
    """Базовый класс спортсмены"""
    def __init__(self, region, category, name):
        """Регион, разряд, имя спортсмена"""
        self.__region = region
        self.__category = category
        self.__name = name

    @property
    def region(self):
        """Возвращает регион за который спортсмен выступает"""
        return self.__region
    
    @property
    def category(self):
        """Возвращает разряд спортсмена"""
        return self.__category
    
    @property
    def name(self):
        """Возвращает имя спортсмена"""
        return self.__name
    
    def display(self):
        """Метод вывода информации на экран"""
        print('Имя: ', self.name)
        print('Разряд: ', self.category)
        print('Регион: ', self.region)
    
    def skills(self):
        """Абстрактный метод для вывода вероятных навыков."""
        raise NotImplementedError("Метод skills() должен быть переопределен в подклассе.")
    
    def achievement(self):
        """Абстрактный метод для определения лучшего достижения."""
        raise NotImplementedError("Метод achievement() должен быть переопределен в подклассе.")
    
    def __le__(self, other):
        """Перегрузка оператора <= для сравнения разряда."""
        s_category = self.category
        o_category = other.category
        if s_category[1] == o_category[1]:
            if s_category[0] <= o_category[0]:
                return True
            else: return False
        elif s_category[1] < o_category[1]:
            return True
        else: return False

    def __eq__(self, other):
        """Перегрузка оператора == для сравнения разряда"""
        if self.__category == other.__category:
            return True
        else: return False

class Climber(Athletes):
    """Класс скалолазов"""
    def __init__(self, name, region_athlets, category, discipline, shoes, height_wall):
        """Инициализирует данные о спортсмене."""
        super().__init__(region_athlets, category, name)
        self.__descipline = discipline
        self.__shoes = shoes
        self.__height_wall = height_wall


    @property #это декоратор 
    def discipline(self):
        """Возвращает специализацию, дисциплину спортсмена"""
        return self.__descipline
    
    @property
    def shoes(self):
        """Возвращает модель скальников спортсмена"""
        return self.__shoes
    
    @property
    def height_wall(self):
        """Возвращает высоту зала в котором спортсмен занимается"""
        return self.__height_wall
    
    def display(self):
       Athletes.display(self)
       print('специализация: ',self.discipline)
       print('Модель скальников: ',self.shoes)
       print('Высота домашнего скалодрома: ',self.height_wall)
    
    def skills(self):
        if self.discipline == discipline.lead:
            print('Хорошие трудники очень выносливы')
        if self.discipline == discipline.speed:
            print('Хорошие скоростники достаточно сильны и у них быстрая реакция')
        if self.discipline == discipline.bouldering:
            print('Хорошие боулдерингисты очень сильны и обладают хорошим критическим мышлением')
    
    def achievement(self):
        print(self.category, 'спортсмен должен быть достаточно крут для сильных трасс')


class Mountaineer(Athletes):
    """Класс альпинистов"""

    def __init__(self, name, region_athlets, category, climb_class, greatest_hight, club):
        """Инициализирует данные о спортсмене."""
        super().__init__(region_athlets, category, name)
        self.__climb_class = climb_class
        self.__greatest_hight = greatest_hight
        self.__club = club
        if self.__greatest_hight < 0:
            raise InvalidHeightError
        
    @property
    def climb_class(self):
        """Возвращает специализацию (класс альпинизма) спортсмена"""
        return self.__climb_class
    
    @property
    def greatest_hight(self):
        """Возвращает наибольшую высоту спортсмена"""
        return self.__greatest_hight
    
    @property
    def club(self):
        """Возвращает название клуба в котором спортсмен занимается"""
        return self.__club
    
    def display(self):
       Athletes.display(self)
       print('специализация: ',self.climb_class)
       print('Наибольшая высота: ',self.greatest_hight)
       print('Название родного альпклуба: ',self.club)

    def skills(self):
        try :
            if self.climb_class == discipline.class_height_techn:
                print('такие спортсмены ваще отбитые типы')
            if self.climb_class == discipline.class_ice:
                print('Такие спортсмены не боятся холода')
            if self.climb_class == discipline.class_rock:
                print('Такие спортсмены лучше остальных альпинистов лазают')
        except (Exception):
            print ("Вы ввели непонятную дисциплину, попробуйте что-то из знакомых нам например: discipline.class_height_techn")

    def achievement(self):
        print(self.category, 'спортсмен должен быть достаточно крут для высоких гор')
   
class InvalidHeightError (Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def str(self):
        print("sdfsfswf")
        if self.message:
            return 'InvalidAnimalWeightError, {0}'.format(self.message)
        else:
            return 'InvalidAnimalWeightError has been raised'

climber1 = Climber("polina","Volo","1ю",discipline.speed,"Stenolaz", 17)
climber2 = Climber("ivan","Volo","3р",discipline.lead,"Stenolaz", 17)
mountaineer1 = Mountaineer("Pavel", "Arch", "2р", 'class_height_techn', 5200, "Archangelsk")
mountaineer2 = Mountaineer("Aleksandr", "Rkr", "1р", discipline.class_ice, -3750, "kollab")
climber1.display()
climber2.display()
mountaineer1.display()
mountaineer2.display()

assert mountaineer1.greatest_hight > 0, "Не может лучшая вершина быть - морем"

try: 
    mountaineer2.greatest_hight < 0 
except InvalidHeightError as e:
    print("Ошибка: {e}")
finally:
    print ("Завершение")


if climber1<=climber2:
    if climber1 == climber2:
        print('Оба крутые')
    else:
        print(climber1.name,'круче')
else: 
    print(climber2.name,'круче')

climber1.skills()
mountaineer1.skills()
climber1.achievement()



#classmethod(может влиять на класс, но не на экземпляр, для его использования не обязательно создавать экземпляр класса), staticmethod(статические методы могут использоваться без создания экземпляра класса), property(собственно обеспечивает доступ к полям класса), contextlib: contextmanager(создан для использовать для определения фабричной функции для оператора контекстных менеджеров with без необходимости создавать класс или отдельные методы __enter__() и __exit__()), dataclassess: dataclass(Они вводят значения по умолчанию и требуют аннотации типов. Быстро генерируемые методы, такие как __eq__, __lt__, и др., упрощают сравнение объектов в Python. представляют собой быстро создаваемые постройки, основанные на автоматизации, освобождающей вас от рутинного кодирования. Обычные классы, в свою очередь, больше напоминают индивидуальную архитектуру, требующую уникального подхода и ручного труда.)
#Декораторы используются для  для логирования, кеширования, добавления нового функционала, используются в тестовых и веб-фреймворках
# Пример композиции - дисплей в классах-потомках, состоит из дисплея класса родителей и собственных функций получения и вывода данных полей (это процесс создания сложных функций или объектов путем комбинирования и объединения более простых функций или объектов. То есть, вместо того чтобы создавать новую функцию или объект с нуля, мы можем использовать уже существующие функции или объекты и комбинировать их в более сложные структуры.)