# 이 셀의 내용은 market_models.py 파일로 저장됩니다.

"""
시장 수요, 공급, 균형점 계산 관련 함수들을 모아놓은 모듈
"""

def quantity_demanded(price, a, b):
    """선형 수요 함수 Qd = a - bP 를 계산합니다."""
    if b <= 0:
        # print("오류: 수요 곡선 기울기(b)는 양수여야 합니다.") # 모듈에서는 print보다 오류 발생 권장
        raise ValueError("수요 곡선 기울기(b)는 양수여야 합니다.")
    q_d = a - b * price
    return max(0, q_d)

def quantity_supplied(price, c, d):
    """선형 공급 함수 Qs = c + dP 를 계산합니다."""
    if d <= 0:
        raise ValueError("공급 곡선 기울기(d)는 양수여야 합니다.")
    q_s = c + d * price
    return max(0, q_s)

def find_equilibrium(a, b, c, d):
    """선형 수요/공급 함수의 균형 가격(P*)과 균형 거래량(Q*)을 계산하여 튜플로 반환합니다."""
    if b <= 0 or d <= 0:
        raise ValueError("수요/공급 곡선 기울기(b, d)는 양수여야 합니다.")
    if (b + d) == 0:
        raise ValueError("수요와 공급 곡선 기울기 합이 0입니다. 평행선.")

    p_star = (a - c) / (b + d)

    if p_star < 0:
        # print("균형 가격이 음수입니다.") # 실제 균형 없음
        return (None, None) # 음수 가격 대신 None 반환 고려

    # 균형 거래량 계산
    q_star = quantity_demanded(p_star, a, b) # 같은 모듈 내 함수 호출
    # if q_star < 0: q_star = 0 # 필요시 음수 거래량 0 처리

    return p_star, q_star

# 모듈로 만들 때는 아래와 같은 직접 실행 코드는 보통 if __name__ == "__main__": 블록 안에 넣습니다.
# (이 부분은 모듈로 사용될 때는 실행되지 않음)
if __name__ == "__main__":
    print("market_models 모듈이 직접 실행되었습니다. (테스트용)")
    # 간단한 테스트 코드
    a_test, b_test = 100, 1
    c_test, d_test = 20, 2
    p_eq, q_eq = find_equilibrium(a_test, b_test, c_test, d_test)
    if p_eq is not None:
        print(f"테스트 균형점: P*={p_eq:.2f}, Q*={q_eq:.2f}")
