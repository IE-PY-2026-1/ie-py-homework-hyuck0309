# 파일이름 : 2차과제 실행결과
# 작 성 자 : 이상혁

print("---------------------------------------------------------------------------")
print("*작업자 생산성 평가 시스템*")
print("---------------------------------------------------------------------------")

worker_names = []
productivities = []

total_productivity = 0

for i in range(5):
    print(f"\n[{i+1}번째 작업자 입력]")

    name = input("이름: ")
    work_amount = int(input("작업량: "))
    work_time = float(input("작업시간: "))

    productivity = work_amount / work_time
    total_productivity += productivity 

    if productivity >= 20:
            grade = '우수'
    elif productivity >=10:
            grade = '보통'
    else:
            grade = '개선 필요'

    if productivity >= 20 and work_amount >= 50:
            special = "축하합니다! 성과금 지급 대상입니다."
    else:
            special = "교육 대상입니다."

    worker_names.append(name)
    productivities.append(productivity)

    print(f"{name}, 생산성: {productivity: .2f}")
    print(f"등급: {grade}")
    print(special)

print("\n전체결과")

for i in range(len(worker_names)):
   print(f"{worker_names[i]}: {productivities[i]:.2f}")

avg = total_productivity / len(productivities)
max_value = max(productivities)
max_index = productivities.index(max_value)

print(f"\n평균 생산성: {avg:.2f}")
print(f"우수 작업자: {worker_names[max_index]}")
