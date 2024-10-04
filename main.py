import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, other):
        #"""Атакует другого героя, уменьшая его здоровье на величину силы удара."""
        if isinstance(other, Hero):
            attack_power = random.randint(15, 20)
            other.health -= attack_power
            # Если здоровье становится отрицательным, устанавливаем его в 0
            if other.health < 0:
                other.health = 0
            print(f"{self.name} атакует {other.name}, нанося {attack_power} урона. У {other.name} осталось {other.health} здоровья.")
        else:
            print("Цель атаки должна быть экземпляром класса Hero.")

    def is_alive(self):
        #"""Возвращает True, если здоровье героя больше 0, иначе False."""
        return self.health > 0

    def __str__(self):
        return f"Hero(name={self.name}, health={self.health})"


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        #"""Начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет."""
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break


# Пример использования
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютер"

    game = Game(player_name, computer_name)
    game.start()