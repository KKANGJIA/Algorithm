def solution(w,h):
    square = w * h # 96개
    if w == h : # 정사각형인 경우
        not_use_square = w # 사용할 수 없는 사각형의 개수
    elif w == 1 and h == 1:
        not_use_square = 1
    elif w == 1 and h != 1: # 한변이라도 1이라면 모든 사각형 제외
        not_use_square = h 
    elif w != 1 and h == 1:
        not_use_square = w
    elif h >= 3 and w >= 2: #직사각형인 경우
        if h // 3 == w // 2:
            not_use_square = 4 * (h // 3)
    
    # 다른 경우를 고려하지 못함... 어떻게 더 효율적인 코드를 짤 수 있을까?
            
    return square - not_use_square
  
# 정확성: 38.9 9 (20분)


        
        
        
    