# 파일명: sd_analyzer.py (실제 파일로 저장해야 함)

import argparse

# --- S&D 관련 함수 정의 (또는 다른 파일에서 import) ---
# (이 부분은 설명을 위해 간단히 다시 정의합니다. 실제로는 import 사용 권장)
def quantity_demanded(price, a, b):
    if b <= 0: return None
    q_d = a - b * price
    return max(0, q_d)

def quantity_supplied(price, c, d):
    if d <= 0: return None
    q_s = c + d * price
    return max(0, q_s)

def find_equilibrium(a, b, c, d):
    if b <= 0 or d <= 0 or (b + d) == 0: return None
    p_star = (a - c) / (b + d)
    if p_star < 0: return None
    q_star = quantity_demanded(p_star, a, b)
    # if q_star < 0: return None # 필요시 추가
    return p_star, q_star
# --- 함수 정의 끝 ---

# 1. ArgumentParser 객체 생성
parser = argparse.ArgumentParser(description='선형 수요/공급 모델의 균형점을 계산합니다.')

# 2. 명령줄 인자 정의 (--a, --b, --c, --d 라는 이름으로 인자를 받음)
#    type=float : 입력값을 실수로 처리
#    required=True : 필수 인자임을 명시
#    help='...' : 도움말 메시지
parser.add_argument('--a', type=float, required=True, help='수요 함수 절편 (Qd = a - bP)')
parser.add_argument('--b', type=float, required=True, help='수요 함수 기울기 절대값 (Qd = a - bP)')
parser.add_argument('--c', type=float, required=True, help='공급 함수 절편 (Qs = c + dP)')
parser.add_argument('--d', type=float, required=True, help='공급 함수 기울기 (Qs = c + dP)')

# 3. 명령줄 인자 파싱(분석)
args = parser.parse_args()

# 4. 파싱된 인자를 사용하여 균형점 계산 함수 호출
#    args.a, args.b 등으로 접근 가능
equilibrium_point = find_equilibrium(args.a, args.b, args.c, args.d)

# 5. 결과 출력
if equilibrium_point:
    p_eq, q_eq = equilibrium_point
    print(f"--- 계산 결과 ---")
    print(f"수요 함수: Qd = {args.a} - {args.b}P")
    print(f"공급 함수: Qs = {args.c} + {args.d}P")
    print(f"균형 가격(P*): {p_eq:.2f}")
    print(f"균형 거래량(Q*): {q_eq:.2f}")
else:
    print("오류: 균형점을 계산할 수 없습니다. 파라미터를 확인하세요.")