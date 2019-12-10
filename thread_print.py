import threading

def worker(count):
    # thread의 이름과 인자를 출력
    print("name: %s, argument: %s" %(threading.currentThread().getName(), count))


def main():
    for i in range(5):
        # target: thread로 실행할 함수의 이름, 
        t = threading.Thread(target=worker, name="thread %i" %i, args=(i,))
        t.start()


if __name__ == '__main__':
    main()
    