
# Introduction

인증 서버 역할을 수행하는 Flask 기반 웹 프로젝트

RobloxWindowMonitor 프로그램에서 비밀번호 인증 서버 역할을 수행하도록 하기 위해 생성된 프로젝트

프로그램에서 vercel에서 호스팅 되고 있는 서버로 비밀번호를 검증 요청함.

비밀번호가 일치하면 프로그램이 실행되도록 하고, 비밀번호가 일치하지 않으면 프로그램이 동작하지 않음

서버에서는 비밀번호가 맞는지 틀리는지만을 Response 로 주고 있기 때문에 비밀번호 노출의 우려가 없음

비밀번호 변경이 필요한 경우 app.py 소스 내의 비밀번호를 변경하면 잠시후 vercel 인증 서버에 자동으로 갱신되므로 간편하게 비밀번호 변경 처리가 가능


# Vercel 에 인증 서버 활성화 방법

1. Vercel 에서 Add New Project 후 Github 레파지토리 선택

![step 1](https://github.com/user-attachments/assets/5f8644c7-1ea3-45b3-9416-7ccd76040436)

2. 하단의 Deploy 버튼 클릭

![step 2](https://github.com/user-attachments/assets/658a56f1-0f0f-429b-b082-f4ce3514d042)

3. 생성된 결과 확인

![step 3](https://github.com/user-attachments/assets/772236ba-c938-48b5-ac30-156640d5dcfa)
