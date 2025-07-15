import threading
import time

def new():
    for x in range(3):
        print("single Thread")

thread1 = threading.Thread(target=new)

thread1.start()
thread1.join()
print('Função finalizada')

#Multi-thread

def calc_square(numbers):
    for i in numbers:
        time.sleep(2)
        print("square: {}".format(str(i * i)))

def calc_cube(numbers):
    for i in numbers:
        time.sleep(2)
        print("square: {}".format(str(i * i * i)))

if __name__ == "__main__":
    array = [4,6,7,9]
    thread1 = threading.Thread(target=calc_square, args=(array,))
    thread2 = threading.Thread(target=calc_cube, args=(array,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Função principal terminada")