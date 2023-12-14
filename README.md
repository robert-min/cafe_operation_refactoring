# Cafe Operation Refactoring


## 🎖️ Project Goal
- 이전에 작업한 카페 사장님 상품 등록 시스템 프로젝트 재진행(우선 로그인 부분만)
- 프로젝트 기획 단계부터 코드 작성까지 모든 과정을 실제 프로젝트 진행과 동일하게 작업
	- 기획 : 사용자 스토리 → 시나리오 → 필요한 구현 기술 리서치 및 공식 문서 색인
- 특히, 코드 작업 시 , TDD를 단계적으로 진행
	- TDD 개발 : 의사코드 작성 → 실 구현 코드 작성 → 단위테스트 → API구현 → 통합테스트
	- Layered Structure : Controller-Business-Service-Repository


## 🎈 Outputs
| Output_name         | Status  | Note | Link |
| ------------------- | ------- | ---- | ---- |
| 사용자 스토리       | #진행완료|      |   [링크](https://github.com/robert-min/cafe_operation_refactoring/issues/1#issuecomment-1842176502)   |
| 시나리오            | #진행완료 |      |  [링크](https://github.com/robert-min/cafe_operation_refactoring/issues/1#issuecomment-1842176683)    |
| 공식 문서 색인      | #진행완료  |      | [링크](https://github.com/robert-min/cafe_operation_refactoring/issues/1#issuecomment-1842176786)     |
| 시스템 설계 | #진행완료 |      |      |
| 단위기능구현+테스트      | #진행완료  |      |      |
|     API구현+테스트                | #진행완료          |      |      |


## 📝 Task
- 각 마일스톤을 달성하기 위해서 필요한 태스크들을 하나씩 열거
- 할당시간과 그에 따른 마감일 기록
- [x] #TODO 🛫 2023-12-05 📅 2023-12-05 : 사용자 스토리 작성 + 템플릿 작업 ✅ 2023-12-05
- [x] #TODO 🛫 2023-12-05 📅 2023-12-05 : 시나리오 작성 + 템플릿 작업 ✅ 2023-12-05
- [x] #TODO 🛫 2023-12-05 📅 2023-12-05 : 공식 문서 색인 ✅ 2023-12-05
- [x] #TODO 🛫 2023-12-05 📅 2023-12-05 : 시스템 설계 ✅ 2023-12-05
- [x] #TODO 🛫 2023-12-05 📅 2023-12-06  : 단위기능구현+테스트 ✅ 2023-12-08
- [x] #TODO 🛫 2023-12-05 📅 2023-12-06 : API구현+테스트 ✅ 2023-12-08


### 폴더 구조
```
- src
	- apps
		- users
			- __init__.py
			- controller.py
			- service.py
			- repository.py
			- schema.py
			- model.py
	- libs
		- __init__.py
		- db_manager.py
		- encrypt.py
		- error_handlers.py
		- exception.py
		- logging.py
		- util.py
	- tests
		- users
			- __init__.py
			- conftest.py
			- test_controller.py
			- test_service.py
			- test_repository.py
		- libs
			- __init__.py
			- test_encrypt.py
- app.py


```

