import argparse
import logging

class LotteryGame:
    def __init__(self, list1, list2):
        # Проверка, что list1 и list2 действительно являются списками
        if not isinstance(list1, list) or not isinstance(list2, list):
            logging.error("Неверно: list1 и list2 должны иметь тип list")
            raise ValueError("list1 и list2 должны иметь тип list")

        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        # Проверка, что list1 и list2 содержат только числа
        if not all(isinstance(num, (int, float)) for num in self.list1 + self.list2):
            logging.error("Неверно: cписки должны содержать только числа")
            raise ValueError("Списки должны содержать только числа")

        matching_numbers = [num for num in self.list1 if num in self.list2]

        if not matching_numbers:
            print("Совпадающих чисел нет.")
        else:
            print(f"Совпадающие числа: {matching_numbers}")
            print(f"Количество совпадающих чисел: {len(matching_numbers)}")
        
        return matching_numbers

def main():
    parser = argparse.ArgumentParser(description="Lottery Game")
    parser.add_argument('list1', type=float, nargs='+', help='Список чисел list1')
    parser.add_argument('list2', type=float, nargs='+', help='Список чисел list2')

    args = parser.parse_args()

    # Настройка логгирования в файл
    logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    format='[{levelname:<8}] {asctime}: {msg}',
                    style='{')
    LOGGER = logging.getLogger(__name__)

    try:
        game = LotteryGame(args.list1, args.list2)
        game.compare_lists()
    except Exception as e:
        LOGGER.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
