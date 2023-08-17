# KoBertSum V2 학습결과 정리

## 1. 데이터

- Data 출처 - [AIHub 문서 요약 텍스트](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=97) (데이콘 데이터)  [](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=97)
- train(210,516) / valid(90,221) / test(34,844)
    - train - *사설 56,760개 , 신문기사 243,977개 → 총  **300,737**개의 문서 데이터*
    - test - *사설 7008개 , 신문기사 30,121개 → 총  37,129개의 문서 데이터*
- EDA
    - 사설_train
        - 문장 개수 분포
            
            ![문장갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%25AF%25EC%2588%2598.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5.png)
            
        
        - 단어 개수 분포
            
            ![단어갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%25AF%25EC%2588%2598.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4.png)
            
        - 추출된 위치 분포
            
            ![주로 어디에서 추출되었는가.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25A3%25BC%25EB%25A1%259C_%25EC%2596%25B4%25EB%2594%2594%25EC%2597%2590%25EC%2584%259C_%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%2598%25EC%2597%2588%25EB%258A%2594%25EA%25B0%2580.png)
            
            주로 몇 번째 문장에서 추출이 되었는가를 표현
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 문장 단어 갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EB%25AC%25B8%25EC%259E%25A5_%25EB%258B%25A8%25EC%2596%25B4_%25EA%25B0%25AF%25EC%2588%2598.png)
            
    - 뉴스_train
        - 문장 개수 분포
            
            ![문장갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%25AF%25EC%2588%2598%201.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%201.png)
            
        - 단어 개수 분포
            
            ![단어개수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%259C%25EC%2588%2598.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%201.png)
            
        - 추출된 위치 분포
            
            ![주로 어디에서 문장이 추출되는가.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25A3%25BC%25EB%25A1%259C_%25EC%2596%25B4%25EB%2594%2594%25EC%2597%2590%25EC%2584%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%25B4_%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%2598%25EB%258A%2594%25EA%25B0%2580.png)
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 문장의 단어갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%2598_%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%25AF%25EC%2588%2598.png)
            
    - 전체_train
        - 문장 개수 분포
            
            ![문장갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%25AF%25EC%2588%2598%202.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%202.png)
            
        - 단어 개수 분포
            
            ![단어갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%25AF%25EC%2588%2598%201.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%202.png)
            
        - 추출되는 위치 분포
            
            ![주로 어디에서 추출되는가.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25A3%25BC%25EB%25A1%259C_%25EC%2596%25B4%25EB%2594%2594%25EC%2597%2590%25EC%2584%259C_%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%2598%25EB%258A%2594%25EA%25B0%2580.png)
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 3개 문장의 단어 개수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_3%25EA%25B0%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%2598_%25EB%258B%25A8%25EC%2596%25B4_%25EA%25B0%259C%25EC%2588%2598.png)
            
    - 사설_test
        - 문장 개수 분포
            
            ![문장갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%25AF%25EC%2588%2598%203.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%203.png)
            
        - 단어 개수 분포
            
            ![단어갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%25AF%25EC%2588%2598%202.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%203.png)
            
        - 추출된 위치 분포
            
            ![추출된 위치 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EC%259C%2584%25EC%25B9%2598_%25EB%25B6%2584%25ED%258F%25AC.png)
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 3개 문장의 단어 개수 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_3%25EA%25B0%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%2598_%25EB%258B%25A8%25EC%2596%25B4_%25EA%25B0%259C%25EC%2588%2598_%25EB%25B6%2584%25ED%258F%25AC.png)
            
    - 뉴스_test
        - 문장 개수 분포
            
            ![문장개수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%259C%25EC%2588%2598.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%204.png)
            
        - 단어 개수 분포
            
            ![단어갯수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%25AF%25EC%2588%2598%203.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%204.png)
            
        - 추출된 위치 분포
            
            ![추출된 위치 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EC%259C%2584%25EC%25B9%2598_%25EB%25B6%2584%25ED%258F%25AC%201.png)
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 문장의 단어 개수 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%2598_%25EB%258B%25A8%25EC%2596%25B4_%25EA%25B0%259C%25EC%2588%2598_%25EB%25B6%2584%25ED%258F%25AC.png)
            
    - 전체_test
        - 문장 개수 분포
            
            ![문장개수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%25EA%25B0%259C%25EC%2588%2598%201.png)
            
            ![문장.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%25AC%25B8%25EC%259E%25A5%205.png)
            
        - 단어 개수 분포
            
            ![단어개수.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%25EA%25B0%259C%25EC%2588%2598%201.png)
            
            ![단어.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EB%258B%25A8%25EC%2596%25B4%205.png)
            
        - 추출된 위치 분포
            
            ![추출된 위치 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EC%259C%2584%25EC%25B9%2598_%25EB%25B6%2584%25ED%258F%25AC%202.png)
            
        - 추출된 문장의 단어 개수 분포
            
            ![추출된 문장의 단어 개수 분포.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/%25EC%25B6%2594%25EC%25B6%259C%25EB%2590%259C_%25EB%25AC%25B8%25EC%259E%25A5%25EC%259D%2598_%25EB%258B%25A8%25EC%2596%25B4_%25EA%25B0%259C%25EC%2588%2598_%25EB%25B6%2584%25ED%258F%25AC%201.png)
            

## 2. 모델

- **KoBertSum** ([https://github.com/uoneway/KoBertSum](https://github.com/uoneway/KoBertSum))
- 모델 설명
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled.png)
    
    - BertSum(우)은 원래의 Bert(좌) 와 다른 형태로 데이터 입력을 받음.
    - **각 문장의 앞에 [CLS] 토큰을 추가하여 각 문장들의 특징을 해당 토큰에 담을 수 있도록 수정**
    - **Interval segment Embedding을 통해 두 개 이상의 문장에 대해서도 세그먼트 임베딩을 진행.** 예를 들어 문장 1, 문장 2, 문장 3, 문장 4가 주어졌다면, 세그먼트 임베딩은 A, B, A, B 식으로 번갈아가며 문장을 구분
    - BERTSUM 출력값 상단에 **summarization-specific layer를 추가하여 문서 요약에 필요한 특징을 추출.** 이를 통해 각 문장별로 요약 정보에 포함할지 여부를 결정.
        
        → 해당 요약 레이어를 구성하는 방법에는 3가지가 있다.
        
        1. 단일 분류 레이어 (FFN + Sigmoid)
        2. ***문장간 트랜스포머 (Inter-sentence Transformer)***
        3. LSTM
        
        우리가 학습 시킨 모델은 Inter-sentence Transformer 이용. BERT에서도 Transformer 구조가 존재하지만, 이때 Attention은 문장 간이 아니라 토큰 간에 작용한다. 따라서 문장 간의 관계를 파악하기 위해 Inter-sentence Transformer를 도입하여 Summarization Layer로 사용하는 것. 이러한 Transformer layer은 Summarization을 위해 문서 수준의 특징을 뽑아내고 오직 문장들 간에 Transformer를 적용. 그 후 Sigmoid를 취한 단순 분류 Linear layer를 통과하여 정답 label과 비교함. (논문에서 가장 좋은 성능을 보임을 Ablation Study를 통해 확인)
        
        아래 그림은 Inter-sentence Transformer
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%201.png)
        
    - 또한 기존 BERT 모델의 positional embedding의 최대 길이는 512인데, BERTSUM에서는 무작위로 초기화되고, encoder에서 다른 매개변수로 finetuned 되는 더 많은 positional embedding을 추가하여 이 한계를 극복했다고 주장함.
        
        코드로 보면, 아래의 부분인 것 같음.
        
        ```python
        if(args.max_pos>512):
                my_pos_embeddings = nn.Embedding(args.max_pos, self.bert.model.config.hidden_size)
                my_pos_embeddings.weight.data[:512] = self.bert.model.embeddings.position_embeddings.weight.data
                my_pos_embeddings.weight.data[512:] = self.bert.model.embeddings.position_embeddings.weight.data[-1][None,:].repeat(args.max_pos-512,1)
                self.bert.model.embeddings.position_embeddings = my_pos_embeddings
        ```
        
        → max_pos 를 1024로 수정해서 짧게 학습시킨 후 inference를 돌려봤는데, 아래의 오류가 발생
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%202.png)
        
        ⇒ 좀 더 탐구가 필요함.
        
    - Extractive Summarization은 document의 각 i번째 문장(*senti*)을 요약문에 포함시킬지에 대한 여부를 *yi*∈ {0,1}로 라벨링하는 것. BERTSUM에서 i번째 [CLS] 토큰의 출력이 *sent_i*를 표현하는 벡터. (→ *ti*).
        
        BERT의 결과(BERT에서 얻은 문장 표현 : T)를 transformer의 encoder layer에 공급.
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%203.png)
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%204.png)
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%205.png)
        
    
    마지막 output layer는 sigmoid classifier → 각 문장을 요약에 포함시킬지 여부의 확률을 얻음
    
    - *h_i^L* : transformer의 top layer (L번째 layer)의 *sent_i*(i번째 문장)에 대한 벡터 → L = 2인 transformer가 가장 성능이 우수
    - loss는 y와 y_pred 간의 binary classification entropy를 이용. 또한 Adam 옵티마이저(*b*1=0.9, *b*2=0.999)를 사용하고 learning rate는 warmup 이용
        
        (*warmup: Training이 시작될 때, 모든 parameters들은 보통 random values(initialized)이므로, 최종 solution에서 멀리 떨어져 있음. 이 때, 너무 큰 learning rate를 사용하면 numerical instability가 발생할 수 있기에, 초기에 작은 learning rate를 사용하고, training과정이 안정되면 초기 learning rate로 전환하는 방법이다.)
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%206.png)
        
        warmup으로 인해 학습을 돌리다 보면 lr 이 치솟다가 서서히 우하향함.
        
    - 정리하면 Bert 단을 통과해서 나온 문장 표현인 t_i[CLS] 를 입력받아서 위치 인코딩을 해준 후, 트랜스포머 인코더에 입력으로 넣어주고, 인코더를 거쳐 최상위 인코더의 은닉상태인 h_i^L 을 얻음. 그 이후 h_i^L 값을 시그모이드를 통과시켜 요약에 문장의 포함 여부를 반환하는 프로세스를 거치게 됨.
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%207.png)
    

## 3. 학습 결과

- **학습 Detail**
    - dropout : 0.1
    - Learning Rate : 2e-3
    - batch size : 2000
    - train steps : 28000
        - **epoch : 20**
            - 2,000(batch size) * 28,000(step) = 300,737(data) * 13(sent avg) * ***epoch***
    - accum count : 2
    - use interval : True
    - warmup steps : 3000
    - *max pos : 512*
        
        ⇒ 위 EDA 를 보면 한 글의 길이가 512를 넘어가는 것이 없어서 문제가 없음.
        
    - 학습 시 인자(args). 중요 부분은 형광펜 처리
        
        ```python
        parser = argparse.ArgumentParser()
            parser.add_argument("-task", default='ext', type=str, choices=['ext', 'abs'])
            parser.add_argument("-encoder", default='bert', type=str, choices=['bert', 'baseline'])
            parser.add_argument("-mode", default='train', type=str, choices=['train', 'validate', 'test'])
            parser.add_argument("-bert_data_path", default='../bert_data_new/cnndm')
            parser.add_argument("-model_path", default='../models/')
            parser.add_argument("-result_path", default='../results/cnndm')
            parser.add_argument("-temp_dir", default='../temp')
        
            parser.add_argument("-batch_size", default=140, type=int)
            parser.add_argument("-test_batch_size", default=200, type=int)
        
            parser.add_argument("-max_pos", default=512, type=int)
            parser.add_argument("-use_interval", type=str2bool, nargs='?',const=True,default=True)
            parser.add_argument("-large", type=str2bool, nargs='?',const=True,default=False)
            parser.add_argument("-load_from_extractive", default='', type=str)
        
            parser.add_argument("-sep_optim", type=str2bool, nargs='?',const=True,default=False)
            parser.add_argument("-lr_bert", default=2e-3, type=float)
            parser.add_argument("-lr_dec", default=2e-3, type=float)
            parser.add_argument("-use_bert_emb", type=str2bool, nargs='?',const=True,default=False)
        
            parser.add_argument("-share_emb", type=str2bool, nargs='?', const=True, default=False)
            parser.add_argument("-finetune_bert", type=str2bool, nargs='?', const=True, default=True)
            parser.add_argument("-dec_dropout", default=0.2, type=float)
            parser.add_argument("-dec_layers", default=6, type=int)
            parser.add_argument("-dec_hidden_size", default=768, type=int)
            parser.add_argument("-dec_heads", default=8, type=int)
            parser.add_argument("-dec_ff_size", default=2048, type=int)
            parser.add_argument("-enc_hidden_size", default=512, type=int)
            parser.add_argument("-enc_ff_size", default=512, type=int)
            parser.add_argument("-enc_dropout", default=0.2, type=float)
            parser.add_argument("-enc_layers", default=6, type=int)
        
            # params for EXT
            parser.add_argument("-ext_dropout", default=0.2, type=float)
            parser.add_argument("-ext_layers", default=2, type=int)
            parser.add_argument("-ext_hidden_size", default=768, type=int)
            parser.add_argument("-ext_heads", default=8, type=int)
            parser.add_argument("-ext_ff_size", default=2048, type=int)
        
            parser.add_argument("-label_smoothing", default=0.1, type=float)
            parser.add_argument("-generator_shard_size", default=32, type=int)
            parser.add_argument("-alpha",  default=0.6, type=float)
            parser.add_argument("-beam_size", default=5, type=int)
            parser.add_argument("-min_length", default=15, type=int)
            parser.add_argument("-max_length", default=150, type=int)
            parser.add_argument("-max_tgt_len", default=140, type=int)
        
            parser.add_argument("-param_init", default=0, type=float)
            parser.add_argument("-param_init_glorot", type=str2bool, nargs='?',const=True,default=True)
            parser.add_argument("-optim", default='adam', type=str)
            parser.add_argument("-lr", default=1, type=float)
            parser.add_argument("-beta1", default= 0.9, type=float)
            parser.add_argument("-beta2", default=0.999, type=float)
            parser.add_argument("-warmup_steps", default=8000, type=int)
            parser.add_argument("-warmup_steps_bert", default=8000, type=int)
            parser.add_argument("-warmup_steps_dec", default=8000, type=int)
            parser.add_argument("-max_grad_norm", default=0, type=float)
        
            parser.add_argument("-save_checkpoint_steps", default=5, type=int)
            parser.add_argument("-accum_count", default=1, type=int)
            parser.add_argument("-report_every", default=1, type=int)
            parser.add_argument("-train_steps", default=1000, type=int)
            parser.add_argument("-recall_eval", type=str2bool, nargs='?',const=True,default=False)
        
            parser.add_argument('-visible_gpus', default='-1', type=str)
            parser.add_argument('-gpu_ranks', default='0', type=str)
            parser.add_argument('-log_file', default='../logs/cnndm.log')
            parser.add_argument('-seed', default=666, type=int)
        
            parser.add_argument("-test_all", type=str2bool, nargs='?',const=True,default=False)
            parser.add_argument("-test_from", default='')
            parser.add_argument("-test_start_from", default=-1, type=int)
        
            parser.add_argument("-train_from", default='')
            parser.add_argument("-report_rouge", type=str2bool, nargs='?',const=True,default=True)
            parser.add_argument("-block_trigram", type=str2bool, nargs='?', const=True, default=True)
        ```
        
    

**학습 시간** : 약 1시간 30분(train) + 6시간(validation) 

             → 서버 리소스 상태에 따라 변동 가능

- **Loss**
    
    v1. train
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%208.png)
    
    v2. train
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%209.png)
    
    v2. valid
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2010.png)
    
    <aside>
    💡 v1(사설 10,000개, 기사 10,000개로 학습 : 균일한 데이터)과 다르게 v2 그래프의 양상을 보아, **데이터 불균형의 문제**가 발생한  것 같음.
    
    </aside>
    
- **Rouge(Metric)**
    - <중간에 끊긴 test 결과>
        
        [rouge_scores.csv](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/rouge_scores.csv)
        
        ![0b1240b8-5e03-4374-a23f-c359b08d39bc.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/0b1240b8-5e03-4374-a23f-c359b08d39bc.png)
        
        —> 점수별 데이터 히스토그램
        
        ![64b268ba-9d29-47da-9d3c-8207fcf7d09f.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/64b268ba-9d29-47da-9d3c-8207fcf7d09f.png)
        
        ![3261adbe-98d7-42b3-96b4-fd5065b0d4e4.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/3261adbe-98d7-42b3-96b4-fd5065b0d4e4.png)
        
        —> 인덱스 1000개 묶음 평균
        
        - metric
            
            ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2011.png)
            
            - **metric :**  Rouge-1 (31.08), Rouge-2 (29.14), Rouge-L (30.97)
        
        중간에 끊켜서 사설의 결과값이 더 많음
        
    
    **최종 test 결과**
    
    [rouge_scores.csv](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/rouge_scores%201.csv)
    
    ![f914b252-0664-48b3-886a-e63242661e89.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/f914b252-0664-48b3-886a-e63242661e89.png)
    
    ![dab1d0c7-97af-41a8-9fe0-738baad59652.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/dab1d0c7-97af-41a8-9fe0-738baad59652.png)
    
    <aside>
    💡 1. 추출 요약 task의 경우, 문장을 그대로 뽑아오기 때문에, 정답 문장과 요약 문장이 일치할 경우 모든 단어가 일치하여 1, 틀리면 0이 됨. → 이러한 이유로 0 또는 1의 점수가 많이 분포함.
    2. 위 그래프를 보면, R1, R2, RL 모두 중간에 심하게 꺾이는 경우가 있는데 이에 대한 원인을 파악해야 함.
    → Bert 특성상, token의 개수가 512로 한정되어서 각 문장당 생성되어야 하는 [CLS]토큰 문장 개수만큼 생성되지 않아서, Ext Transformer 단으로 넘어가는 [CLS]개수가 전체 문장보다 현저히 적어지는 현상 발생. 그렇게 되면 정답을 맞출 확률이 현저히 떨어짐.
    **3.** 위 꺾은선 그래프에서 아래로 젖혀지는 구간의 추출 개수를 보면, 개수가 많이 없기는 함. 좀 더 확인 요망.
    
    </aside>
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2012.png)
    
    - **metric 결과 :**  **Rouge-1 (39.81), Rouge-2 (37.43), Rouge-L (39.62)**
    
    ⇒ *Recall*: Gold Summary(정답 라벨링 값)을 구성하는 단어 중 몇 개의 단어가 Model Summary(모델 예측값)을 구성하는 단어들과 겹치는지를 보는 점수
    
    ⇒ *Precision*: Model Summary(모델 예측값)을 구성하는 단어들 중 Gold Summary(정답 라벨링 값)을 구성하는 단어들과 얼마나 겹치는지를 보는 점수
    
    ⇒ *Rouge 1*: Unigram (개별 단어)
    
    ⇒ *Rouge 2*: Bigram (단어 2개씩)
    
    → 모델 ****요약본과 정답 ****요약본이 길어질수록 **겹치는 bigram**의 수가 적어질 것이라는 사실을 짚고 넘어갈 필요가 있음
    
    ⇒ *ROUGE-L*: [LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) 기법을 이용해 **최장 길이**로 매칭되는 문자열을 측정. LCS의 장점은 **ROUGE-2**와 같이 단어들의 **연속적 매칭**을 요구하지 않고, 어떻게든 **문자열** 내에서 발생하는 매칭을 측정하기 때문에 보다 유연한 성능 비교가 가능하다는 것.
    

## 4. 실제 추론

[inference.ipynb](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/inference.ipynb)

1. BertSum 모델에 들어갈 수 있도록 input data 수정
    
    → 각 문장 시작과 끝에 [CLS], [SEP] 토큰 붙히기
    
    → interval segment 사용(홀수번째 1, 짝수번째 0)
    
2. 학습된 모델 가중치 불러오기
    
    → 임베딩 가중치 및 transformer extractive layer 가중치
    
    → 학습 완료된 pt 파일 구성도 (768 은 bert-base 의 d_model(각 단어들의 임베딩 벡터))
    
    [model_step_26000.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/model_step_26000.png)
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2013.png)
    
3. 원하는 문장 수 만큼 추출
- BertData(), ExtSummarizer model 코드
    
    ```python
    class BertData():
        def __init__(self):
            self.tokenizer = KoBertTokenizer.from_pretrained("monologg/kobert", do_lower_case=True)
    
            self.sep_token = '[SEP]'
            self.cls_token = '[CLS]'
            self.pad_token = '[PAD]'
            self.sep_vid = self.tokenizer.token2idx[self.sep_token]
            self.cls_vid = self.tokenizer.token2idx[self.cls_token]
            self.pad_vid = self.tokenizer.token2idx[self.pad_token]
    
        def preprocess(self, src):
    
            if (len(src) == 0):
                return None
    
            original_src_txt = [' '.join(s) for s in src]
            idxs = [i for i, s in enumerate(src) if (len(s) > 1)]
    
            src = [src[i][:2000] for i in idxs]
            src = src[:1000]
    
            if (len(src) < 3):
                return None
    
            src_txt = [' '.join(sent) for sent in src]
            text = ' [SEP] [CLS] '.join(src_txt)
            src_subtokens = self.tokenizer.tokenize(text)
            src_subtokens = src_subtokens[:510]  ## 512가 최대인데 [SEP], [CLS] 2개 때문에 510
            src_subtokens = ['[CLS]'] + src_subtokens + ['[SEP]']
    
            src_subtoken_idxs = self.tokenizer.convert_tokens_to_ids(src_subtokens)
            _segs = [-1] + [i for i, t in enumerate(src_subtoken_idxs) if t == self.sep_vid]
            segs = [_segs[i] - _segs[i - 1] for i in range(1, len(_segs))]
            segments_ids = []
            for i, s in enumerate(segs):
                if (i % 2 == 0):
                    segments_ids += s * [0]
                else:
                    segments_ids += s * [1]
            cls_ids = [i for i, t in enumerate(src_subtoken_idxs) if t == self.cls_vid]
            labels = None
            src_txt = [original_src_txt[i] for i in idxs]
            tgt_txt = None
            
            return src_subtoken_idxs, labels, segments_ids, cls_ids, src_txt, tgt_txt
    ```
    
    - 논문에서 positional embedding 의 최대 길이 512 제한을 극복했다고 하지만, Encoder의 Bert에서 여전히 512 이상의 차원을 받아들이지 못함.
    
    ```python
    class ExtSummarizer(nn.Module):
        def __init__(self, args, device, checkpoint):
            super(ExtSummarizer, self).__init__()
            self.args = args
            self.device = device
            self.bert = Bert(args.large, args.temp_dir, args.finetune_bert)
    
            self.ext_layer = ExtTransformerEncoder(self.bert.model.config.hidden_size, args.ext_ff_size, args.ext_heads,
                                                   args.ext_dropout, args.ext_layers)
            if (args.encoder == 'baseline'):
                bert_config = BertConfig(self.bert.model.config.vocab_size, hidden_size=args.ext_hidden_size,
                                         num_hidden_layers=args.ext_layers, num_attention_heads=args.ext_heads, intermediate_size=args.ext_ff_size)
                self.bert.model = BertModel(bert_config)
                self.ext_layer = Classifier(self.bert.model.config.hidden_size)
    
            if(args.max_pos>512):
                my_pos_embeddings = nn.Embedding(args.max_pos, self.bert.model.config.hidden_size)
                my_pos_embeddings.weight.data[:512] = self.bert.model.embeddings.position_embeddings.weight.data
                my_pos_embeddings.weight.data[512:] = self.bert.model.embeddings.position_embeddings.weight.data[-1][None,:].repeat(args.max_pos-512,1)
                self.bert.model.embeddings.position_embeddings = my_pos_embeddings
    
            if checkpoint is not None:
                self.load_state_dict(checkpoint['model'], strict=True)
            else:
                if args.param_init != 0.0:
                    for p in self.ext_layer.parameters():
                        p.data.uniform_(-args.param_init, args.param_init)
                if args.param_init_glorot:
                    for p in self.ext_layer.parameters():
                        if p.dim() > 1:
                            xavier_uniform_(p)
    
            self.to(device)
    
        def forward(self, src, segs, clss, mask_src, mask_cls):
            top_vec = self.bert(src, segs, mask_src)
            #print(top_vec)
            #top_vec = top_vec.last_hidden_state
            sents_vec = top_vec[torch.arange(top_vec.size(0)).unsqueeze(1), clss]
            sents_vec = sents_vec * mask_cls[:, :, None].float()
            sent_scores = self.ext_layer(sents_vec, mask_cls).squeeze(-1)
            return sent_scores, mask_cls
    ```
    
- inference 코드
    
    ```python
    def summarize(text):
        
        def txt2input(text):
            #data = list(filter(None, text.split('\n')))
            #data = split_sentences(text)
            bertdata = BertData()
            txt_data = bertdata.preprocess(text)
            data_dict = {"src":txt_data[0],
                        "labels":[0,1,2],
                        "segs":txt_data[2],
                        "clss":txt_data[3],
                        "src_txt":txt_data[4],
                        "tgt_txt":None}
            input_data = []
            input_data.append(data_dict)
            return input_data
        
        input_data = txt2input(text)
        device = torch.device("cuda")
        
        def _pad(data, pad_id, width=-1):
            if (width == -1):
                width = max(len(d) for d in data)
            rtn_data = [d + [pad_id] * (width - len(d)) for d in data]
            return rtn_data
        
        pre_src = [x['src'] for x in input_data]
        pre_segs = [x['segs'] for x in input_data]
        pre_clss = [x['clss'] for x in input_data]
    
        src = torch.tensor(_pad(pre_src, 0)).cuda()
        segs = torch.tensor(_pad(pre_segs, 0)).cuda()
        mask_src = ~(src == 0)
    
        clss = torch.tensor(_pad(pre_clss, -1)).cuda()
        mask_cls = ~(clss == -1)
        clss[clss == -1] = 0
    
        clss.to(device).long()
        mask_cls.to(device).long()
        segs.to(device).long()
        mask_src.to(device).long()
        
        checkpoint = torch.load("D:/KoBertSum/ext/models/model_step_26000.pt", device)
        model = ExtSummarizer(args, device, checkpoint)
        model.eval()
    
        with torch.no_grad():
            sent_scores, mask = model(src, segs, clss, mask_src, mask_cls)
            sent_scores = sent_scores + mask.float()
            sent_scores = sent_scores.cpu().data.numpy()
            print(sent_scores)
            selected_ids = np.argsort(-sent_scores, 1)
            print(selected_ids)
        
        return selected_ids
    ```
    
- **결과**
    
    원문을 문장 단위로 쪼개기 위하여 `kss`의 `split_setences` 사용
    
    ```python
    from kss import split_sentences
    text = split_sentences(text)
    result = summarize(text)
    ```
    
    이후 원하는 만큼 뽑을 수 있음.
    
    ```python
    [text[i] for i in result[0][:len(text)//3]]
    #[text[i] for i in result[0][:3]]
    ```
    
    아래 예시들은 위처럼 **전체 문장 길이를 3으로 나눈 만큼** 추출하도록 함.
    
    - 사설 예시 1 [https://www.hani.co.kr/arti/opinion/editorial/1103219.html](https://www.hani.co.kr/arti/opinion/editorial/1103219.html)
        1. **문장 쪼갠 결과(원문)**
        
        ['서울 서초구 초등학교 교사 사망에 대한 교육당국 합동조사 결과가 지난 4일 나왔지만 새롭게 규명된 것이 없다는 교사들의 반발이 거세다.',
        '교육부와 서울시교육청이 사건 직후 사실관계 확인에 나서겠다며 합동조사에 착수했지만, 대부분 의혹을 경찰 수사로 미뤄두면서 ‘용두사미 조사’가 되고 말았다는 것이다.',
        '전국초등교사노조는 “‘새내기 교사의 죽음에 무거운 책임감을 느낀다’며 내놓은 결과라고 납득할 수 없을 정도로 허술하다. 합동조사단이 해야 할 일은 해당 학교가 낸 가정통신문 내용의 사실 확인이 아닌 고인의 업무상 고충을 면면히 공개하는 것이어야 했다”며 재조사를 촉구했다.',
        '전국 교사 4만명은 지난 주말에도 철저한 진상규명을 촉구하는 집회를 이어갔다.',
        '실제로 합동조사 결과의 대부분은 학교 쪽이 고인의 사망 직후 냈던 입장문과 언론보도에서 제기된 내용이 맞는지 확인하는 수준에 그쳤다.',
        '올해 3월 이후 고인의 학급 담임 교체 사실이 없었다거나, 해당 학급에서 올해 학교폭력 신고가 없었으며, 학급 내 이른바 ‘연필사건’ 이후 고인이 학부모로부터 전화를 받았다는 등의 단순 사실 확인에 불과하다.',
        '연필사건 학생의 학부모가 고인의 휴대전화 번호를 알게 된 경위나 담임 자격 시비와 같은 폭언이 있었는지 여부, 학교 쪽이 연필사건을 원만히 중재했다고 한 7월13일 이후에도 추가적인 학부모 민원이 있었는지 등 정작 규명이 필요한 의혹에 대해서는 새롭게 밝혀낸 것이 하나도 없다.',
        '무엇보다 합동조사 결과에는 고인이 사망에 이르기까지 학교나 학교장의 책임은 없었는지에 대한 내용이 쏙 빠져 있다.',
        '고인은 연필사건 학생뿐 아니라 다른 2명의 부적응 학생으로 인한 고충이 적지 않았고, 모두 10차례나 학교 쪽에 학생 지도의 어려움을 이유로 상담 요청을 한 바 있다.',
        '그러나 학교 쪽은 고인에게 얼른 전화번호를 바꾸라거나 학부모에게 심리검사 또는 상담을 받을 것을 권유하라고 조언하는 정도에 그쳤다.',
        '학교가 함께 문제를 해결하려는 의지를 보이는 대신 개별 교사에게 책임을 지운 정황이 아닐 수 없다.',
        '심지어 학교 쪽은 지난달 최초 작성한 입장문에서 연필사건이 원만히 해결된 것처럼 언급했다가 해당 내용을 삭제했는데, 애초 어떤 의도로 작성한 것인지 규명될 필요가 있다.',
        '교육당국은 재발 방지 대책을 촘촘하게 마련하는 일도 중요하지만 제대로 된 진상규명이 우선이라는 점을 명심해야 한다.']
        
        1. **추출 결과**
        
        <aside>
        📎 **# v1 KoBertSum 모델 요약**
        
        전국초등교사노조는 “‘새내기 교사의 죽음에 무거운 책임감을 느낀다’며 내놓은 결과라고 납득할 수 없을 정도로 허술하다. 합동조사단이 해야 할 일은 해당 학교가 낸 가정통신문 내용의 사실 확인이 아닌 고인의 업무상 고충을 면면히 공개하는 것이어야 했다”며 재조사를 촉구했다.
        전국 교사 4만명은 지난 주말에도 철저한 진상규명을 촉구하는 집회를 이어갔다.
        서울 서초구 초등학교 교사 사망에 대한 교육당국 합동조사 결과가 지난 4일 나왔지만 새롭게 규명된 것이 없다는 교사들의 반발이 거세다.
        실제로 합동조사 결과의 대부분은 학교 쪽이 고인의 사망 직후 냈던 입장문과 언론보도에서 제기된 내용이 맞는지 확인하는 수준에 그쳤다.
        
        </aside>
        
        <aside>
        📎 **# v2 KoBertSum 모델 요약**
        
        서울 서초구 초등학교 교사 사망에 대한 교육당국 합동조사 결과가 지난 4일 나왔지만 새롭게 규명된 것이 없다는 교사들의 반발이 거세다.
        교육부와 서울시교육청이 사건 직후 사실관계 확인에 나서겠다며 합동조사에 착수했지만, 대부분 의혹을 경찰 수사로 미뤄두면서 ‘용두사미 조사’가 되고 말았다는 것이다.
        전국초등교사노조는 “‘새내기 교사의 죽음에 무거운 책임감을 느낀다’며 내놓은 결과라고 납득할 수 없을 정도로 허술하다. 합동조사단이 해야 할 일은 해당 학교가 낸 가정통신문 내용의 사실 확인이 아닌 고인의 업무상 고충을 면면히 공개하는 것이어야 했다”며 재조사를 촉구했다.
        전국 교사 4만명은 지난 주말에도 철저한 진상규명을 촉구하는 집회를 이어갔다.
        
        </aside>
        
        <aside>
        📎 **# pororo 모델 요약**
        
        서울 서초구 초등학교 교사 사망에 대한 교육당국 합동조사 결과가 지난 4일 나왔지만 새롭게 규명된 것이 없다는 교사들의 반발이 거세다. 
        교육부와 서울시교육청이 사건 직후 사실관계 확인에 나서겠다며 합동조사에 착수했지만, 대부분 의혹을 경찰 수사로 미뤄두면서 ‘용두사미 조사’가 되고 말았다는 것이다. 
        전국 교사 4만명은 지난 주말에도 철저한 진상규명을 촉구하는 집회를 이어갔다. 
        무엇보다 합동조사 결과에는 고인이 사망에 이르기까지 학교나 학교장의 책임은 없었는지에 대한 내용이 쏙 빠져 있다.
        
        </aside>
        
        ⇒ 뉴스 기사라 그런지 앞의 문장들로만 이루어져 있음.
        
    - 사설 예시 2 [http://news.heraldcorp.com/view.php?ud=20230810000399](http://news.heraldcorp.com/view.php?ud=20230810000399)
        1. **문장 쪼갠 결과(원문)**
        
        ['BNK경남은행 간부의 562억원 횡령 사건이 채 잊히기도 전인데 또 다른 금융사고가 연발하고 있다.',
        '수법도 거래 기업의 미공개 정보로 주식을 거래해 부당이득을 취하고, 고객 몰래 계좌를 개설하는 등 눈앞의 이익을 위해 온갖 불법·편법 행위가 동원되고 있다.',
        'KB국민은행의 직원들이 고객사의 미공개정보를 이용해 주식을 사고팔아 127억원의 부당이득을 챙긴 사실이 최근 금융당국에 적발됐다.',
        '이들은 2021년 1월부터 올해 4월까지 61개 상장사의 증권 업무를 대행하며 알게 된 무상증자 규모와 일정을 주식 매수에 이용했다.',
        '정보 공개 전 미리 주식을 사뒀다가 공시 뒤 주가가 오르면 팔았다.',
        '무상증자를 하게 되면 기업재무구조가 건전한 것으로 풀이돼 주가에는 호재로 작용한다.',
        '이런 방식으로 66억원 정도를 챙겼고, 일부는 다른 부서의 동료나 가족 등에게도 정보를 전달했다.',
        '이 과정에서도 61억원 상당의 부당 이득이 발생했다.',
        '대구은행 일부 지점 직원 수십명은 평가 실적을 올리기 위해 지난해 1000여건이 넘는 고객 문서를 위조해 증권 계좌를 개설한 것으로 파악됐다.',
        '이 직원들은 내점한 고객을 상대로 증권사 연계 계좌를 만들어 달라고 요청한 뒤 해당 계좌 신청서를 복사해 고객의 동의 없이 같은 증권사의 계좌를 하나 더 만들었다.',
        'A증권사 위탁 계좌 개설 신청서를 받고, 같은 신청서를 복사해 A증권사 해외선물계좌까지 개설하는 방식이다.',
        '최근 한 고객이 동의하지 않은 계좌가 개설됐다는 사실을 알게 돼 대구은행에 민원을 제기하면서 직원들의 비리가 드러났다.',
        '대구은행은 문제를 인지하고도 금감원에 이 사실을 보고하지 않았고, 영업점들에 공문을 보내 불건전 영업행위를 예방하라고 안내하는 데 그쳤다.',
        '금융실명제법 위반, 사문서 위조 등에 해당할 수 있는 범죄행위를 대수롭지 않게 넘기는 안일함이 혀를 차게 한다.',
        '국내 은행은 땅 짚고 헤엄치기식 이자장사로 평균 1억원대 고연봉을 누리는 직종이다.',
        '시중은행은 미국발 고금리에 편승해 거둬들인 막대한 예대마진으로 최근 수년간 성과급 잔치를 벌여 국민의 눈총을 받았다.',
        '국민의 재산으로 손쉽게 수익을 올리는 직종이라면 누구보다 엄격한 도덕적 기준을 세워도 모자랄 판에 ‘내 몫을 더 챙기겠다’며 이기적 탐욕을 부리고 있으니 말문이 막힌다.',
        '자체 내부통제가 안 된다면 현행 솜방망이 처벌 수위를 높이는 수밖에 없다.',
        '주요 동기가 경제적 이익인 만큼 벌금이나 과징금, 양형 부과 수준을 크게 높여 법 무서운 줄 알도록 해야 한다.',
        '주요 선진국에서 이미 도입한 불공정거래 범죄자에 대한 자본시장 거래제한제도도 적극 검토할 필요가 있다.']
        
        1. **추출 결과**
        
        <aside>
        📎 **# v1 KoBertSum 모델 요약**
        
        이들은 2021년 1월부터 올해 4월까지 61개 상장사의 증권 업무를 대행하며 알게 된 무상증자 규모와 일정을 주식 매수에 이용했다.
        BNK경남은행 간부의 562억원 횡령 사건이 채 잊히기도 전인데 또 다른 금융사고가 연발하고 있다.
        KB국민은행의 직원들이 고객사의 미공개정보를 이용해 주식을 사고팔아 127억원의 부당이득을 챙긴 사실이 최근 금융당국에 적발됐다.
        무상증자를 하게 되면 기업재무구조가 건전한 것으로 풀이돼 주가에는 호재로 작용한다.
        정보 공개 전 미리 주식을 사뒀다가 공시 뒤 주가가 오르면 팔았다.
        이 과정에서도 61억원 상당의 부당 이득이 발생했다.
        
        </aside>
        
        <aside>
        📎 **# v2 KoBertSum 모델 요약**
        
        수법도 거래 기업의 미공개 정보로 주식을 거래해 부당이득을 취하고, 고객 몰래 계좌를 개설하는 등 눈앞의 이익을 위해 온갖 불법·편법 행위가 동원되고 있다.
        BNK경남은행 간부의 562억원 횡령 사건이 채 잊히기도 전인데 또 다른 금융사고가 연발하고 있다.
        KB국민은행의 직원들이 고객사의 미공개정보를 이용해 주식을 사고팔아 127억원의 부당이득을 챙긴 사실이 최근 금융당국에 적발됐다.
        이들은 2021년 1월부터 올해 4월까지 61개 상장사의 증권 업무를 대행하며 알게 된 무상증자 규모와 일정을 주식 매수에 이용했다.
        정보 공개 전 미리 주식을 사뒀다가 공시 뒤 주가가 오르면 팔았다.
        무상증자를 하게 되면 기업재무구조가 건전한 것으로 풀이돼 주가에는 호재로 작용한다.
        
        </aside>
        
        <aside>
        📎 **# pororo 모델 요약**
        BNK경남은행 간부의 562억원 횡령 사건이 채 잊히기도 전인데 또 다른 금융사고가 연발하고 있다. 
        수법도 거래 기업의 미공개 정보로 주식을 거래해 부당이득을 취하고, 고객 몰래 계좌를 개설하는 등 눈앞의 이익을 위해 온갖 불법·편법 행위가 동원되고 있다. 
        KB국민은행의 직원들이 고객사의 미공개정보를 이용해 주식을 사고팔아 127억원의 부당이득을 챙긴 사실이 최근 금융당국에 적발됐다. 
        이 과정에서도 61억원 상당의 부당 이득이 발생했다. 
        시중은행은 미국발 고금리에 편승해 거둬들인 막대한 예대마진으로 최근 수년간 성과급 잔치를 벌여 국민의 눈총을 받았다. 
        자체 내부통제가 안 된다면 현행 솜방망이 처벌 수위를 높이는 수밖에 없다.’
        
        </aside>
        
    - 뉴스 예시 1 [https://n.news.naver.com/article/029/0002818639?sid=110](https://n.news.naver.com/article/029/0002818639?sid=110)
        1. **문장 쪼갠 결과(원문)**
        
        ['"뭔가 있긴 있는 거 같은데, 아직은 완벽하지 않은 것 같다."',
        "국내 연구진이 개발한 상온 초전도체 'LK-99'의 정체에 대해 국내 과학자들은 말끝을 흐리며 이같이 애매모호하게 답했다.",
        '국내외에서 재현 실험 등의 검증이 이뤄지고 있는 상황에서 확실하게 말할 수 없음을 이해해 달라고도 했다.',
        '그럼에도 이전까지 볼 수 없었던 물질임에는 틀림 없다는 여운을 남겼다.',
        '취재 과정에서 인터뷰한 대다수 과학자들은 LK-99가 초전도 특성을 가진 물질인 거 같긴 한데, 그렇다고 100% 초전도체라고 현재로선 단정적으로 말하기 어렵다는 얘기를 공통적으로 꺼냈다.',
        '초전도체 검증 결과 여부를 떠나 21세기 들어 이처럼 새로운 과학적 발명에 이토록 전 세계가 떠들석하고, 가히 센세이셔',
        '널한 반응을 몰고 온 적이 있었던가.',
        '아마도 현대과학의 혁명기로, 과학적 발명과 발견이 많았던 19세기 말과 20세기 초를 제외하곤 이번이 처음인 듯 싶다.',
        '그만큼 인류가 얼마나 세기적 발명의 탄생을 목말라 했는지를 가늠케 한 사건이었다.',
        "지난달 22일 퀀텀에너지연구소가 상온·상압 초전도체 'LK-99' 개발에 대한 논문을 사전 공개 사이트(아카이브)에 올린 이후 지금까지 전 세계가 우리나라를 주목하고 있다.",
        '112년 전인 1911년 네덜란드 라이덴 대학의 카멜린 온네스 교수가 초전도 현상을 발견한 이후, 상온 초전도체 개발에 수많은 과학자들이 밤낮을 잊고 실험실을 지켜 왔지만 모두 허사로 끝났다.',
        "이렇듯 '꿈의 물질'로 불리는 상온 초전도체 개발은 노벨상 '0순위'이자, 기존 기술패권 질서의 판을 한 순간에 뒤집어 놓을 파괴적 혁신기술로 추앙 받아왔다.",
        '그토록 갈망하던 현대 과학계의 난제 중의 하나인 상온 초전도체 개발 소식이 한국에서 전해진 것이다.',
        '그것도 세계 유수의 대학과 연구소, 글로벌 대기업이 아닌 2008년 창업한 대학 실험실 기반 벤처기업이 깜짝 주인공으로 등장했다.',
        '이 기업은 국내 상온·상압 초전도체 연구의 토대를 놓은 초전도 이론의 대가로 불리는 고(故) 최동식 고려대 교수의 제자들이 주축이 돼 설립됐다.',
        "이들의 논문에 '고 최동식 교수를 기립니다'는 문장이 기재돼 있을 정도로, 대학 시절부터 20년 넘게 스승의 유훈을 받들어 상온 초전도체 개발을 이어 왔다.",
        "LK-99는 이석배(L) 대표와 김지훈(K) 연구소장의 영문 이니셜을 따서 정했고, LK-99를 발견해 본격적인 연구를 시작한 1999년을 기념해 '99'라고 붙여졌다.",
        '이들은 지난 20년 동안 1000회 이상의 실험을 반복한 끝에 LK-99 개발에 성공했다고 했다.',
        'LK-99 진위 여부를 확인하기 위해 전 세계 주류 연구그룹들이 일을 제쳐놓고 재현 실험 등을 통한 검증에 힘을 쏟고 있다.',
        '글로벌 빅테크 기업도 이에 합류했다는 소식도 들린다.',
        '지금까지의 결과를 보면 LK-99는 상온 초전도체가 아닐 가능성이 커 보인다.',
        "더 많은 검증 결과가 나올수록 한국발 '상온 초전도체 탄생'은 물거품이 될 가능성이 높아 보인다.",
        '미 프린스턴대는 LK-99가 자석일 가능성이 크다고 밝혔다.',
        "상온 초전도체에 대한 회의적 시각이 늘면서 LK-99 검증 논란을 '제2의 황우석 사태'에 빗대어 깎아 내릴 듯 하다.",
        '분명한 것은 논문을 고의로 조작한 황우석 사태와 LK-99는 본질적으로 다르다.',
        ...
        '결코 황우석 사태와 비교해 비난해선 안 될 것이다.',
        '과학은 무수한 실패 과정을 거쳐 진보해 왔다.',
        '그렇기에 과학은 솔직해야 하고, 거짓이 없어야 한다.',
        'LK-99가 신기루에 불과하더라도 우리의 작은 벤처가 촉발시킨 상온 초전도체 이슈는 전 세계 과학자들의 개발 경쟁을 가속화해 우리를 더 나은 세상으로 이끌어 주는 트리거가 될 것이라는 점만으로도 의미있는 일이 아닐까.',
        '우리나라가 초전도체 개발을 계속 이어가야 하는 이유이기도 하다.']
        
        1. **추출 결과**
        
        <aside>
        📎 **# v1 KoBertSum 모델 요약**
        
        그럼에도 이전까지 볼 수 없었던 물질임에는 틀림 없다는 여운을 남겼다.
        "뭔가 있긴 있는 거 같은데, 아직은 완벽하지 않은 것 같다."
        초전도체 검증 결과 여부를 떠나 21세기 들어 이처럼 새로운 과학적 발명에 이토록 전 세계가 떠들석하고, 가히 센세이셔
        취재 과정에서 인터뷰한 대다수 과학자들은 LK-99가 초전도 특성을 가진 물질인 거 같긴 한데, 그렇다고 100% 초전도체라고 현재로선 단정적으로 말하기 어렵다는 얘기를 공통적으로 꺼냈다.
        국내외에서 재현 실험 등의 검증이 이뤄지고 있는 상황에서 확실하게 말할 수 없음을 이해해 달라고도 했다.
        아마도 현대과학의 혁명기로, 과학적 발명과 발견이 많았던 19세기 말과 20세기 초를 제외하곤 이번이 처음인 듯 싶다.
        널한 반응을 몰고 온 적이 있었던가.
        국내 연구진이 개발한 상온 초전도체 'LK-99'의 정체에 대해 국내 과학자들은 말끝을 흐리며 이같이 애매모호하게 답했다.
        그만큼 인류가 얼마나 세기적 발명의 탄생을 목말라 했는지를 가늠케 한 사건이었다.
        
        </aside>
        
        <aside>
        📎 **# v2 KoBertSum 모델 요약**
        
        국내 연구진이 개발한 상온 초전도체 'LK-99'의 정체에 대해 국내 과학자들은 말끝을 흐리며 이같이 애매모호하게 답했다.
        국내외에서 재현 실험 등의 검증이 이뤄지고 있는 상황에서 확실하게 말할 수 없음을 이해해 달라고도 했다.
        그럼에도 이전까지 볼 수 없었던 물질임에는 틀림 없다는 여운을 남겼다.
        초전도체 검증 결과 여부를 떠나 21세기 들어 이처럼 새로운 과학적 발명에 이토록 전 세계가 떠들석하고, 가히 센세이셔
        취재 과정에서 인터뷰한 대다수 과학자들은 LK-99가 초전도 특성을 가진 물질인 거 같긴 한데, 그렇다고 100% 초전도체라고 현재로선 단정적으로 말하기 어렵다는 얘기를 공통적으로 꺼냈다.
        아마도 현대과학의 혁명기로, 과학적 발명과 발견이 많았던 19세기 말과 20세기 초를 제외하곤 이번이 처음인 듯 싶다.
        그만큼 인류가 얼마나 세기적 발명의 탄생을 목말라 했는지를 가늠케 한 사건이었다.
        널한 반응을 몰고 온 적이 있었던가.
        ”뭔가 있긴 있는 거 같은데, 아직은 완벽하지 않은 것 같다."
        
        </aside>
        
        <aside>
        📎 **# pororo 모델 요약**
        
        "뭔가 있긴 있는 거 같은데, 아직은 완벽하지 않은 것 같다." 
        국내 연구진이 개발한 상온 초전도체 \'LK-99\'의 정체에 대해 국내 과학자들은 말끝을 흐리며 이같이 애매모호하게 답했다. 
        국내외에서 재현 실험 등의 검증이 이뤄지고 있는 상황에서 확실하게 말할 수 없음을 이해해 달라고도 했다. 
        그럼에도 이전까지 볼 수 없었던 물질임에는 틀림 없다는 여운을 남겼다. 
        취재 과정에서 인터뷰한 대다수 과학자들은 LK-99가 초전도 특성을 가진 물질인 거 같긴 한데, 그렇다고 100% 초전도체라고 현재로선 단정적으로 말하기 어렵다는 얘기를 공통적으로 꺼냈다. 
        지난달 22일 퀀텀에너지연구소가 상온·상압 초전도체 \'LK-99\' 개발에 대한 논문을 사전 공개 사이트(아카이브)에 올린 이후 지금까지 전 세계가 우리나라를 주목하고 있다. 
        이렇듯 \'꿈의 물질\'로 불리는 상온 초전도체 개발은 노벨상 \'0순위\'이자, 기존 기술패권 질서의 판을 한 순간에 뒤집어 놓을 파괴적 혁신기술로 추앙 받아왔다. 
        그토록 갈망하던 현대 과학계의 난제 중의 하나인 상온 초전도체 개발 소식이 한국에서 전해진 것이다. 
        그것도 세계 유수의 대학과 연구소, 글로벌 대기업이 아닌 2008년 창업한 대학 실험실 기반 벤처기업이 깜짝 주인공으로 등장했다. 
        이 기업은 국내 상온·상압 초전도체 연구의 토대를 놓은 초전도 이론의 대가로 불리는 고(故) 최동식 고려대 교수의 제자들이 주축이 돼 설립됐다. 
        LK-99는 이석배(L) 대표와 김지훈(K) 연구소장의 영문 이니셜을 따서 정했고, LK-99를 발견해 본격적인 연구를 시작한 1999년을 기념해 \'99\'라고 붙여졌다.'
        
        </aside>
        
    - 뉴스 예시 2 [https://n.news.naver.com/mnews/article/001/0014123951?sid=102](https://n.news.naver.com/mnews/article/001/0014123951?sid=102)
        1. **문장 쪼갠 결과(원문)**
        
        ['(서울=연합뉴스) 이주영 기자 = 빠른 진화 속도로 혹독한 환경에 적응하며 4억년을 살아온 히말라야 티베트고원의 이끼도 현재 진행되고 있는 지구온난화에는 살아남지 못할 것이라는 연구 결과가 나왔다.',
        "독일 프라이부르크대 랄프 레스키 교수와 중국 서우두사범대 허이쿤 교수팀은 10일 과학저널 '셀'(Cell)에서 티베트고원 등에 사는 화석 식물인 타카키아 이끼의 DNA 분석 결과 유전적으로 매우 빠른 진화 특성을 가졌지만 현 기후변화에서 살아남을 만큼 빠르게 진화하지는 못할 가능성이 큰 것으로 나타났다고 밝혔다.",
        '티베트고원 얼음 절벽에서 3억9천만년이나 살아온 타카키아는 작고 느리게 자라는 이끼로 히말라야 4천ｍ 고지대와 일본, 미국 등 일부 지역에서만 볼 수 있다.',
        '연구팀은 티베트고원의 타카키아 서식지를 10년간 18차례 방문해 샘플을 수집하고 서식지를 조사했다.',
        '타카키아의 DNA 염기서열을 분석하고 기후변화가 타카키아에 어떤 영향을 미치는지 연구했다.',
        '레스키 교수는 지각변동으로 히말라야산맥이 솟아올랐을 때는 타카키아가 등장한 지 1억년이 지난 시점이었고, 이런 급격한 환경 변화 속에서 살아남았다며 이 연구를 통해 그 비밀을 밝히고자 했다고 말했다.',
        '연구팀은 DNA 분석 결과 타카키아의 게놈(유전체)이 여러 세대에 걸쳐 자연선택에 의해 진화하면서 손상된 DNA를 고치고 자외선 손상으로부터 회복하는 데 탁월한 유전자들을 많이 갖게 된 것으로 나타났다고 밝혔다.',
        '레스키 교스는 "타카키아가 현재 빠르게 진화하는 유전자가 가장 많은 게놈을 가지고 있다는 사실을 발견했다"고 말했다.',
        '허이쿤 교수는 "타카키아는 매년 8개월간 눈에 덮여 있고 4개월은 고강도 자외선을 받는다"며 "타카키아는 이에 대응해 유연한 가지 뻗기로 다양한 위치에서 살 수 있게 적응했고 이를 통해 폭설과 자외선을 견딜 수 있는 견고한 개체군 구조를 만들었다"고 설명했다.',
        '연구팀은 또 타카키아 분류에 대해서도 이끼인지, 조류인지 등에 대한 논란이 있었으나 이번 게놈 분석으로 이끼라는 게 확인됐다며 시간 흐름에 따라 게놈이 크게 변했음에도 식물체 형태가 거의 변하지 않은 점은 새 연구 과제라고 밝혔다.',
        '연구팀은 그러나 타카키아가 과거 환경변화에 빠르게 적응해 살아남았지만 현재의 온난화와 서식지 감소 속도를 고려하면 앞으로 100년 이상 살아남기는 어려울 것으로 보인다고 우려했다.',
        '연구가 진행되는 동안 티베트고원의 타카키아 개체수는 매년 1.6%씩 감소했으며 서식지도 빠르게 줄어 금세기 말에는 타카키아에 적합한 서식지가 세계적으로 1천~1천500㎢밖에 남지 않을 것으로 예상됐다.',
        '연구팀은 타카키아의 멸종을 막기 위해 실험실에서 타카키아를 증식한 다음 티베트고원에 이식하는 시도를 하고 있으며 5년간 관찰 결과 이식된 식물 일부가 생존하고 번성하는 것으로 나타났다고 밝혔다.',
        '레스키 교수는 "인간이 진화 정점에 있다고 생각하지만 공룡도 왔다가 사라진 것처럼 인간도 사라질 수 있다"며 "공룡의 등장과 멸종, 인간의 등장을 지켜본 타카키아로부터 회복력과 멸종에 대해 무언가를 배울 수 있을 것"이라고 말했다.']
        
        1. **추출 결과**
        
        <aside>
        📎 **# v1 KoBertSum 모델 요약**
        
        연구팀은 티베트고원의 타카키아 서식지를 10년간 18차례 방문해 샘플을 수집하고 서식지를 조사했다.
        독일 프라이부르크대 랄프 레스키 교수와 중국 서우두사범대 허이쿤 교수팀은 10일 과학저널 '셀'(Cell)에서 티베트고원 등에 사는 화석 식물인 타카키아 이끼의 DNA 분석 결과 유전적으로 매우 빠른 진화 특성을 가졌지만 현 기후변화에서 살아남을 만큼 빠르게 진화하지는 못할 가능성이 큰 것으로 나타났다고 밝혔다.
        티베트고원 얼음 절벽에서 3억9천만년이나 살아온 타카키아는 작고 느리게 자라는 이끼로 히말라야 4천ｍ 고지대와 일본, 미국 등 일부 지역에서만 볼 수 있다.
        타카키아의 DNA 염기서열을 분석하고 기후변화가 타카키아에 어떤 영향을 미치는지 연구했다.
        
        </aside>
        
        <aside>
        📎 **# v2 KoBertSum 모델 요약**
        
        (서울=연합뉴스) 이주영 기자 = 빠른 진화 속도로 혹독한 환경에 적응하며 4억년을 살아온 히말라야 티베트고원의 이끼도 현재 진행되고 있는 지구온난화에는 살아남지 못할 것이라는 연구 결과가 나왔다.
        독일 프라이부르크대 랄프 레스키 교수와 중국 서우두사범대 허이쿤 교수팀은 10일 과학저널 '셀'(Cell)에서 티베트고원 등에 사는 화석 식물인 타카키아 이끼의 DNA 분석 결과 유전적으로 매우 빠른 진화 특성을 가졌지만 현 기후변화에서 살아남을 만큼 빠르게 진화하지는 못할 가능성이 큰 것으로 나타났다고 밝혔다.
        티베트고원 얼음 절벽에서 3억9천만년이나 살아온 타카키아는 작고 느리게 자라는 이끼로 히말라야 4천ｍ 고지대와 일본, 미국 등 일부 지역에서만 볼 수 있다.
        연구팀은 티베트고원의 타카키아 서식지를 10년간 18차례 방문해 샘플을 수집하고 서식지를 조사했다.
        
        </aside>
        
        <aside>
        📎 **# pororo 모델 요약**
        
        (서울=연합뉴스) 이주영 기자 = 빠른 진화 속도로 혹독한 환경에 적응하며 4억년을 살아온 히말라야 티베트고원의 이끼도 현재 진행되고 있는 지구온난화에는 살아남지 못할 것이라는 연구 결과가 나왔다. 
        독일 프라이부르크대 랄프 레스키 교수와 중국 서우두사범대 허이쿤 교수팀은 10일 과학저널 '셀'(Cell)에서 티베트고원 등에 사는 화석 식물인 타카키아 이끼의 DNA 분석 결과 유전적으로 매우 빠른 진화 특성을 가졌지만 현 기후변화에서 살아남을 만큼 빠르게 진화하지는 못할 가능성이 큰 것으로 나타났다고 밝혔다. 
        연구팀은 DNA 분석 결과 타카키아의 게놈(유전체)이 여러 세대에 걸쳐 자연선택에 의해 진화하면서 손상된 DNA를 고치고 자외선 손상으로부터 회복하는 데 탁월한 유전자들을 많이 갖게 된 것으로 나타났다고 밝혔다. 
        연구팀은 그러나 타카키아가 과거 환경변화에 빠르게 적응해 살아남았지만 현재의 온난화와 서식지 감소 속도를 고려하면 앞으로 100년 이상 살아남기는 어려울 것으로 보인다고 우려했다.
        
        </aside>
        
    
    <aside>
    💡 **## 의견**
    
    1. v1의 경우 학습한 데이터가 적어서, metric 값은 높을지 몰라도 요약의 질이 떨어짐.
    2. v2의 경우 **불균형 데이터**를 균형하게 해서 학습한다면, 좋은 성능을 기대할 수 있을 것이라 예상.
    3. pororo의 경우 설치가 힘들고, API 등으로 공개된 것이 없음.
    
    </aside>
    
    - **발생한 문제**
        - **max_pos**를 512에서 1024로 수정해도, 기존 Bert의 문제점을 벗어날 수 없었음. 즉 추출 요약 프로세스를 위한 마지막 단 Inter-sentence Transformer에 입력하기 위한 임베딩을 Bert로 하는데, 이 때 최대 길이 512를 변경할 수 없었음.
            
            ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2014.png)
            
        - 최대 문장 길이가 512인 것이 문제인지는 모르겠으나, 몇몇 문서들에 대해서 추론을 돌려보았을 때, 실제 문서의 문장 개수보다 더 적게 점수를 매김을 확인함. 즉 13문장으로 이루어진 문서에서 6문장만 점수를 매기는 현상이 발생함.
            - 문제가 발생한 문서에 kobert tokenizer를 돌렸을 때 결과 → 불필요한 토큰의 개수가 너무 많아보임.
                
                ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2015.png)
                
            - 이후 배포된 코드대로 512개로 맞추고 [CLS]토큰의 개수를 세어 본 결과
                
                ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2016.png)
                
            
            ⇒ 즉 원문 문장에 비해 적은 수의 문장이 입력된다고 볼 수 있음(Bert를 통과하고 나면 [CLS]가 각문장을 대표하는 값을 가지고 있기 때문에). 이는 위에서 ROUGE 값의 불균형의 원인이 될 수도 있음. 
            

## 5. v1, pororo, v2 성능 비교(rouge)

- **v1, 2**
    
    **KobertSum(우리 모델)**
    
    - base-model: Bert-base ***(tokernizer - KoBert Tokenizer)***
- **pororo**
    
    모델에 대한 설명
    
    - **base-model :** *brainbert.base.ko.summary **(tokenizer - BertSumTokenizer)***
        - **RoBERTa** 모델 기반 (논문 : [https://arxiv.org/abs/1907.11692](https://arxiv.org/abs/1907.11692))
        
        [RoBERTa 논문리뷰](https://aboutnlp.tistory.com/27?category=876186)
        
        BERT의 후속모델 →  BERT의 몇 가지 한계점을 개선한 모델
        
        기존 BERT가 underfitting 되어있음을 지적하면서 등장한 모델
        
        1) dynamic masking 방법 사용
        
        2) 더 많은 데이터와 더 많은 batch 사이즈를 사용
        
        3) NSP(Next Sentence Prediction) 제거
        
        위와 같은 3가지 방법으로 BERT 보다 성능을 높임.
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2017.png)
        
    - **dataset :** Dacon summarization corpus + AI Hub summarization corpus (1st release)
    
    - **metric :**  Rouge-1 (42.67), Rouge-2 (31.80), Rouge-L (43.12) [[공식문서]](https://kakaobrain.github.io/pororo/seq2seq/summary.html)
        
        **ROUGE F1 SCORE 평균값** : doc에 나와있는 metric 보다는 높게 나옴
        
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2018.png)
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2019.png)
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2020.png)
    
    - 1000개씩 한 묶음(평균)으로 그래프
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2021.png)
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2022.png)
    
    ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2023.png)
    
    ![75d96e8a-af6e-4d9e-8994-01014389fa10.png](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/75d96e8a-af6e-4d9e-8994-01014389fa10.png)
    
    - *pororo predict code*
        
        ```python
        # pororo\tasks\text_summarization.py
        
        def predict(self, text: str, return_list: bool = False):
                """
                Conduct extractive summarization
        
                Args:
                    text (str): input text
                    return_list (bool): whether to return as list
        
                Returns:
                    (str) summarized text
                    (List[str]) list of text if return_list is True
        
                """
                encoded = self._tokenizer.encode_batch(text, max_length=512)
                input_ids = encoded["input_ids"].to(self._device)
                segment_ids = encoded["segment_ids"].to(self._device)
                sentences = encoded["sentences"][0]  # list of str
                **summary_sentence_count = len(sentences) // 3 # 원문의 문장 길이를 3으로 나눈 몫 계산**
                cls_ids, mask_cls = self._make_class_ids(input_ids)
        
                output = self._model(
                    input_ids,
                    segment_labels=segment_ids,
                    last_state_only=True,
                )
        
                bert_representation = output[0][0].transpose(0, 1)
                batch_arange = (torch.arange(
                    bert_representation.size(0)).unsqueeze(1).to(self._device))
                sentence_vector = bert_representation[batch_arange, cls_ids]
                sentence_vector *= mask_cls[:, :, None].float().to(self._device)
        
                final_logits = self._classifier(sentence_vector).squeeze()
                final_logits = torch.sigmoid(final_logits)
                final_logits = final_logits.clone() * mask_cls.float()
        
                prediction = final_logits.argsort(descending=True)
                **prediction = sorted(prediction[:, :summary_sentence_count][0].tolist()) #3 -> 추출 요약 문장 개수 변경**
                prediction = [sentences[i] for i in prediction]
        
                if not return_list:
                    prediction = " ".join(prediction)
        
                return prediction
        ```
        
        ![Untitled](7%20KoBertSum%20V2%20%E1%84%92%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3%E1%86%B8%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20d80ad28354d144edab575a323f8e07dc/Untitled%2024.png)
        
    
    **최종 정리**
    
    |  | V1 | V2 | PORORO |
    | --- | --- | --- | --- |
    | ROUGE-1 | 59.29 | 39.81 | 61.00 |
    | ROUGE-2 | 38.71 | 37.43 | 43.98 |
    | ROUGE-L | 54.36 | 39.62 | 59.42 |
    
    → v2 모델의 데이터 불균형 문제를 해결하여 학습한다면, pororo와 성능이 비슷하거나 혹은 높게 나올 것으로 예상.
    

## 6. 발전 방향

1. ROUGE Metric이 그다지 높지 않다는 한계점 → **RDASS** 도 측정해보는 방법을 시도해도 좋을 듯.

⇒ 그러나 생성 요약에서 효과적이라는 의견이 있음.

[텍스트 요약 모델 성능 평가를 위한 새로운 척도, RDASS를 소개합니다.](https://kakaoenterprise.github.io/deepdive/210729)

1. 새로운 모델 고려?! ⇒ MatchSum

[MatchSum](https://velog.io/@howay96/MatchSum)

[GitHub - bagger3025/MatchSum_kor](https://github.com/bagger3025/MatchSum_kor)
