import time, random, socket, platform, os
def welcome():
    print("파이썬 cmd\n버전 0")
welcome()
hn = socket.gethostname()
ip = socket.gethostbyname(hn)
while True:
    msg = input(" > ")
    if msg[:4] == "echo":
        print(msg[5:])
    elif msg  == "cmd":
        welcome()
    elif msg == "exit":
        exit(0)
    elif msg == "date":
        d = str(time.localtime())
        print(d[25:29]+"년"+d[38:40]+"월"+d[49:51]+"일")
    elif msg == "time":
        t = time.ctime()
        print(t[11:20])
    elif msg == "random":
        a = int(input("a~b에서 a:"))
        b = int(input("a~b에서 b:"))
        print(int(random.randrange(a, b+1)))
    elif msg[:2] == "py":
        exec(msg[3:])
    elif msg == "ipconfig":
        print("호스트명: " + str(hn) + "\nIP: " + str(ip))
    elif msg == "sysinfo":
        print(f"시스템: {platform.system()} {platform.release()} {platform.version()}\n아키텍쳐: {platform.machine()}\n파이썬 버전: {platform.python_version()}\n호스트명: {hn}\nIP: {ip}\nCPU: {platform.processor()}\n파이썬 빌드: {platform.python_build()}\n파이썬 컴파일러: {platform.python_compiler()}\n현재 사용자: {os.getlogin()}")
    elif msg == "help":
        print("echo: 내용을 echo한다\nipconfig: 호스트명, IP 출력\npy: 파이썬 커맨드 실행\nsysinfo: OS 정보, 아키텍쳐, 파이썬 버전, 호스트명, IP, CPU, 파이썬 빌드, 파이썬 컴파일러, 현재 사용자 출력\nrandom: a와 b까지의 랜덤한 수 출력\ntime: 시간을 나타낸다(nn:nn:nn)\ndate: 날짜를 나타낸다(nnnn년 nn월 nn일)\nexit: 프로그램 종료\ncmd: 프로그램 정보 나타내기\nhelp: 도움말 열기")
    else:
        print("알맞은 명령어가 아니다")
                    
