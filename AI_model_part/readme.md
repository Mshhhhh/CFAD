# 한성대학교 캡스톤 CFAD AI 파트

- 해당 파일 얼굴 데이터 경우 한국인 감정인식을 위한 복합 영상인
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=82
- AI hub에서 데이터를 다운로드 받아서 데이터셋을 활용했습니다. 

## 데이터셋 재구축
- AI Hub에서 다운로드한 데이터가 40만 개를 넘지만, 해당 사진에 문제가 있음 발견.
- 전처리를 위해 기본적인 `.json`에 담겨있는 box 좌표를 이용하려 했으나, 좌표가 제대로 찍히지 않는 문제 발생.
- 전처리를 위한 Face Detection 모델 후보군 선정:
  - **cvrib**: CPU/GPU 자원 소모가 적지만 정확성이 낮음.
  - **Mediapipe Face Detection**: 속도가 느리지만 정확성이 높으며, 90%의 정확도 기록.
  - **Human-Face-Crop-ONNX-TensorRT**: GPU 자원 소모가 많지만 얼굴 검출 정확도가 높음. 그러나 비얼굴 객체에서도 얼굴을 검출하는 경우가 많음.
- **Mediapipe 얼굴 검출 사용 결정**
  - Mediapipe 사용 결과: **16시간 소요**
    
  ![image](https://github.com/user-attachments/assets/ea9e8689-a0e0-4c89-9727-2ba6e4a3103d)

  - 그러나, Meta에서 개발한 **DeepFace**의 성능이 월등히 좋아 최종적으로 DeepFace 사용 결정.
  - Mediapipe는 컬러 사진에 적합했지만, DeepFace는 흑백·컬러 모두에서 우수한 성능을 보임.
  - 100% 정확도가 아니므로, 얼굴이 아닌 검출 결과를 제거하는 추가 작업 진행.
  - 추가적인 데이터 압축을 위해 모든 사진 흑백화, 그리고 검출된 얼굴 부분을 제외한 나머지 부분은 삭제

## 모델 선정
- CNN, DNN, ResNet-50을 Pre-train하여 비교한 결과, **CNN이 가장 적합**한 모델로 결정됨.
- Train Loss가 수렴하지 않는 문제 발생:
  - 회전된 사진을 삭제했으나 학습이 원활하지 않음.
  - 사람이 구분하기 어려운 사진을 제거한 후 학습 재진행.
- **60%의 정확도 기록 시작**

## 모델 학습
- 데이터셋을 아무리 줄여도 **200GB 이하로 줄이기 어려움**.
- Google Colab 유료 버전 사용을 제외하고 **로컬 GPU를 활용하여 모델 학습 진행**.
- 학습 속도가 예상보다 느려 **훈련 epoch를 낮추는 방법으로 진행**.

