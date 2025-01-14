import streamlit as st

# 제목 설정
st.title('🔮 나의 MBTI 특성 & 잘 맞는 유형 찾기!')

# MBTI 입력 받기
mbti = st.text_input('당신의 MBTI를 입력하세요:', '').upper()

# MBTI 특성 및 추천 유형 매핑
mbti_info = {
    'INTJ': ('🧠 논리적이고 창의적인 전략가! 항상 큰 그림을 보며 계획하는 것을 좋아해요. 🌌', 'ENTP', 'ESFP'),
    'ENTP': ('💡 뛰어난 문제 해결 능력을 가진 토론가! 새로운 아이디어를 탐구하고 즐겨요. 🚀', 'INFJ', 'ISFJ'),
    'INFJ': ('🌱 따뜻하고 직관적인 옹호자! 깊은 이해력으로 사람들을 돕는 것을 좋아해요. 🌈', 'ENFP', 'ESTP'),
    'ENFP': ('✨ 열정적이고 창의적인 운동가! 자유로운 영혼으로 새로운 경험을 추구해요. 🌍', 'INFJ', 'ISTJ'),
    'ISTJ': ('📚 신중하고 책임감 있는 현실주의자! 체계적이고 논리적인 사고를 중요시해요. 🛠️', 'ESFP', 'ENFP'),
    'ESTJ': ('💼 실용적이고 결단력 있는 관리자! 조직화된 환경에서 효율성을 추구해요. 📊', 'ISTP', 'INFP'),
    'ISFJ': ('🛡️ 헌신적이고 책임감 있는 수호자! 주변 사람들을 돌보는 것을 즐깁니다. 🏡', 'ESFP', 'ENTP'),
    'ESFJ': ('🎉 사교적이고 따뜻한 관리인! 사람들과 함께 어울리며 조화를 이루는 것을 중요시해요. 🤝', 'ISFP', 'INTP'),
    'ISTP': ('🔧 실용적이고 냉철한 장인! 문제 해결을 위해 논리적이고 효율적인 접근을 선호해요. 🛠️', 'ESTP', 'ENFJ'),
    'ESTP': ('⚡ 에너지 넘치고 모험을 즐기는 사업가! 즉각적인 결정을 내리고 도전을 즐겨요. 🎲', 'ISTP', 'INFJ'),
    'ISFP': ('🎨 온화하고 예술적인 모험가! 개인의 감정을 중시하고 창의력을 발휘해요. 🌺', 'ESFP', 'ENTJ'),
    'ESFP': ('🎭 사교적이고 즐거움을 추구하는 연예인! 사람들과 함께하는 것을 즐기고 순간을 즐겨요. 🎉', 'ISFJ', 'INTJ'),
    'INTP': ('🔍 분석적이고 호기심 많은 사색가! 복잡한 개념을 탐구하고 이론을 즐겨요. 🧬', 'ENTJ', 'ESFJ'),
    'ENTJ': ('🚀 결단력 있고 목표 지향적인 통솔자! 효율성과 전략을 통해 목표를 달성해요. 🌍', 'INTP', 'ISFP'),
    'INFP': ('🌸 이상적이고 깊이 있는 중재자! 사람들의 내면을 이해하고 그들을 돕고자 해요. ✨', 'ENFJ', 'ESTJ'),
    'ENFJ': ('🌟 카리스마 있고 공감 능력이 뛰어난 주최자! 사람들의 잠재력을 끌어내는 데 탁월해요. 🎤', 'INFP', 'ISTP')
}

# 버튼을 눌렀을 때 결과 출력
if st.button('나의 MBTI 특성 보기 👀'):
    if mbti in mbti_info:
        description, best_match, worst_match = mbti_info[mbti]
        st.write(f"🌟 **{mbti}**: {description}")
        st.write(f"💖 당신과 가장 잘 맞는 유형: **{best_match}**")
        st.write(f"💔 당신과 잘 맞지 않는 유형: **{worst_match}**")
    else:
        st.write('⚠️ 알 수 없는 MBTI 유형입니다. 다시 입력해 주세요!')
