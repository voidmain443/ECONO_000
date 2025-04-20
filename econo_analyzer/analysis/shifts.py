# 이 셀의 내용은 econo_analyzer/analysis/shifts.py 파일로 저장됩니다.

"""
수요 또는 공급 변화 분석 함수 모듈
"""
# 다른 모듈의 함수를 사용하기 위해 import
from econo_analyzer.models import market # 같은 패키지 내 models 폴더의 market 모듈 import

def compare_equilibria(params_old, params_new):
    """
    변화 전후의 파라미터 딕셔너리를 받아 두 균형점을 계산하고 비교 결과를 반환합니다.
    파라미터 딕셔너리 예시: {'a': 150, 'b': 3, 'c': 30, 'd': 2}
    """
    # 원래 균형점 계산
    p_old, q_old = market.find_equilibrium(params_old['a'], params_old['b'], params_old['c'], params_old['d'])

    # 새로운 균형점 계산
    p_new, q_new = market.find_equilibrium(params_new['a'], params_new['b'], params_new['c'], params_new['d'])

    results = {
        "old_equilibrium": (p_old, q_old),
        "new_equilibrium": (p_new, q_new),
    }

    # 변화 설명 추가 (선택 사항)
    if p_old is not None and p_new is not None:
        if p_new > p_old: results["price_change"] = "상승"
        elif p_new < p_old: results["price_change"] = "하락"
        else: results["price_change"] = "변동 없음"
    else: results["price_change"] = "비교 불가"

    if q_old is not None and q_new is not None:
        if q_new > q_old: results["quantity_change"] = "증가"
        elif q_new < q_old: results["quantity_change"] = "감소"
        else: results["quantity_change"] = "변동 없음"
    else: results["quantity_change"] = "비교 불가"

    return results

print("econo_analyzer.analysis.shifts 모듈 로드됨") # 모듈 로드 확인용 (선택 사항)
