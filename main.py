# 파일이름 : 3차과제 실행결과
# 작 성 자 : 이상혁

# 작업자 생산성 정밀 평가 및 분석 시스템 V2.0

worker_names = []
work_amounts = []
work_times = []
productivities = []
grades = []


def calculate_productivity(work_amount, work_time):
    productivity = work_amount / work_time
    return productivity


def get_grade(productivity):
    if productivity >= 20:
        grade = "우수"
    elif productivity >= 10:
        grade = "보통"
    else:
        grade = "개선 필요"
    return grade


def add_worker():
    global worker_names, work_amounts, work_times, productivities, grades

    print("\n[작업자 정보 입력]")

    name = input("작업자 이름을 입력하세요: ")
    work_amount = int(input("작업량을 입력하세요: "))
    work_time = float(input("작업 시간을 입력하세요: "))

    if work_amount <= 0 or work_time <= 0:
        print("작업량과 작업 시간은 0보다 커야 합니다.")
        return

    productivity = calculate_productivity(work_amount, work_time)
    grade = get_grade(productivity)

    worker_names.append(name)
    work_amounts.append(work_amount)
    work_times.append(work_time)
    productivities.append(productivity)
    grades.append(grade)

    print(f"\n{name} 작업자의 정보가 저장되었습니다.")
    print(f"생산성: {productivity:.2f}")
    print(f"등급: {grade}")

    if productivity >= 20 and work_amount >= 50:
        print("특별 평가: 성과금 지급 대상")
    elif productivity < 10 or work_amount < 20:
        print("특별 평가: 교육 및 관리 필요")
    else:
        print("특별 평가: 일반 작업자")


def show_workers():
    print("\n[전체 작업자 조회]")

    if len(worker_names) == 0:
        print("저장된 작업자 정보가 없습니다.")
        return

    for i in range(len(worker_names)):
        print("\n------------------------------")
        print(f"작업자 번호: {i + 1}")
        print(f"이름: {worker_names[i]}")
        print(f"작업량: {work_amounts[i]}")
        print(f"작업 시간: {work_times[i]:.2f}시간")
        print(f"생산성: {productivities[i]:.2f}")
        print(f"등급: {grades[i]}")


def analyze_productivity():
    print("\n[생산성 분석]")

    if len(productivities) == 0:
        print("분석할 작업자 정보가 없습니다.")
        return

    total = 0

    for productivity in productivities:
        total += productivity

    average = total / len(productivities)
    max_productivity = max(productivities)
    top_index = productivities.index(max_productivity)

    sorted_productivities = productivities[:]
    sorted_productivities.sort()

    print(f"전체 작업자 수: {len(worker_names)}명")
    print(f"평균 생산성: {average:.2f}")
    print(f"최고 생산성: {max_productivity:.2f}")
    print(f"최고 생산성 작업자: {worker_names[top_index]}")
    print(f"생산성 오름차순 정렬: {sorted_productivities}")


while True:
    print("\n====================================")
    print(" 작업자 생산성 정밀 평가 시스템 V2.0")
    print("====================================")
    print("1. 작업자 정보 입력")
    print("2. 전체 작업자 조회")
    print("3. 생산성 분석")
    print("4. 프로그램 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        add_worker()
    elif menu == "2":
        show_workers()
    elif menu == "3":
        analyze_productivity()
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")