import threading

class Worker(threading.Thread):
    # 생성자 함수
    # Thread 클래스의 생성자를 호출
    def __init__(self, args, name=""):
        threading.Thread.__init__(self)
        self.args = args

    # 실제 실행할 함수(run)를 오버라이딩 하여 구현
    def run(self):
        # thread의 이름과 클래스의 속성을 출력
        print("name: %s, argument: %s" %(self.name, self.args[0]))
        
def main():
    for i in range(5):
        t = Worker(name="thread %i" %(i), args=(i, ))
        # 클래스 내부의 오버라이딩한 run을 실행
        t.start()

if __name__ == '__main__':
    main()
    