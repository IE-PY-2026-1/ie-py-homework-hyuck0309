# 파일이름 : 4차과제 실행결과
# 작 성 자 : 이상혁

# 작업자 생산성 정밀 평가 및 분석 시스템 V3.0

workers = []

def add_worker():
    try:
        name = input("작업자 이름: ")
        amount = float(input("작업량: "))
        time = float(input("작업 시간: "))

        productivity = amount / time

        if productivity >= 20:
            grade = "S"
        elif productivity >= 15:
            grade = "A"
        elif productivity >= 10:
            grade = "B"
        elif productivity >= 5:
            grade = "C"
        else:
            grade = "D"
        if productivity >= 20 and amount >= 100:
            special = "우수 작업자"
        else:
            special = "-"

        workers.append([
            name,
            amount,
            time,
            round(productivity, 2),
            grade,
            special
        ])

        print("등록 완료")
    except ValueError:
        print("숫자를 올바르게 입력하세요.")

def show_workers():
    if len(workers) == 0:
        print("등록된 작업자가 없습니다.")
        return
    
    print("\n===== 작업자 목록 =====")

    for worker in workers:
        print(
            f"이름:{worker[0]} "
            f"작업량:{worker[1]} "
            f"시간:{worker[2]} "
            f"생산성:{worker[3]} "
            f"등급:{worker[4]} "
            f"특별평가:{worker[5]}"
        )

def save_file():
    try:
        with open("workers.txt", "w", encoding="utf-8") as file:
            for worker in workers:
                file.write(
                f"{worker[0]},"
                f"{worker[1]},"
                f"{worker[2]},"
                f"{worker[3]},"
                f"{worker[4]},"
                f"{worker[5]}\n"
                )
        print("파일 저장 완료")

    except FileNotFoundError:
        print("파일 오류 발생")

def load_file():
    try:
        with open("workers.txt", "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("저장된 파일이 없습니다.")

while True:
    print("\n===== 작업자 생산성 관리 시스템 =====")
    print("1. 작업자 등록")
    print("2. 작업자 조회")
    print("3. 파일 저장")
    print("4. 파일 읽기")
    print("0. 종료")
    menu = input("선택 : ")
    if menu == "1":
        add_worker()
    elif menu == "2":
        show_workers()
    elif menu == "3":
        save_file()
    elif menu == "4":
        load_file()
    elif menu == "0":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")