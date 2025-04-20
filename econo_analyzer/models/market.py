# 이 셀의 내용은 econo_analyzer/models/market.py 파일로 저장됩니다.

"""
시장 수요, 공급, 균형점 계산 관련 함수들을 모아놓은 모듈
"""

def quantity_demanded(price, a, b):
    """선형 수요 함수 Qd = a - bP 를 계산합니다."""
    if b <= 0: raise ValueError("수요 곡선 기울기(b)는 양수여야 합니다.")
    q_d = a - b * price
    return max(0, q_d)

def quantity_supplied(price, c, d):
    """선형 공급 함수 Qs = c + dP 를 계산합니다."""
    if d <= 0: raise ValueError("공급 곡선 기울기(d)는 양수여야 합니다.")
    q_s = c + d * price
    return max(0, q_s)

def find_equilibrium(a, b, c, d):
    """선형 수요/공급 함수의 균형 가격(P*)과 균형 거래량(Q*)을 계산하여 튜플로 반환합니다."""
    if b <= 0 or d <= 0: raise ValueError("수요/공급 곡선 기울기(b, d)는 양수여야 합니다.")
    if (b + d) == 0: raise ValueError("수요와 공급 곡선 기울기 합이 0입니다. 평행선.")

    p_star = (a - c) / (b + d)
    if p_star < 0: return (None, None) # 음수 가격

    q_star = quantity_demanded(p_star, a, b)
    return p_star, q_star

print("econo_analyzer.models.market 모듈 로드됨") # 모듈 로드 확인용 (선택 사항)
