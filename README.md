# todo-cli
TODO CLI . Test 1

![version](https://img.shields.io/badge/version-v1.0.0-blue)

![version](https://img.shields.io/badge/version-v1.0.0-blue?style=for-the-badge)


![GitHub release (latest by date)](https://img.shields.io/github/v/release/indylee/todo-cli)

![GitHub last commit](https://img.shields.io/github/last-commit/indylee/todo-cli)

간단한 명령어 기반 할 일 관리 앱입니다.  
Python으로 작성되었으며 Termux, Linux, macOS, Windows 어디서나 실행할 수 있습니다.

---

## 📦 설치

```bash
git clone https://github.com/inhyeok/todo-cli.git
cd todo-cli

python todo.py add "할 일 내용"

python todo.py list

python todo.py done 1

---

📁 데이터 저장 방식

할 일 목록은 todos.json 파일에 자동 저장됩니다.

---

📝 버전 정보

- v1.0 — add, list, done 기능 구현


🟢 2) GitHub에 커밋하기

Termux에서 프로젝트 폴더로 이동:

`
cd todo-cli
`

1) 변경된 파일 확인
`
git status
`

2) 변경 파일 스테이징
`
git add .
`

3) 커밋 메시지 작성
`
git commit -m "Add README usage guide and implement done feature"
`

---

🟢 3) GitHub에 푸시하기

`
git push origin main
`

처음 푸시라면:

- Username → GitHub 사용자명  
- Password → Personal Access Token(PAT)

---

🟢 4) 버전 태그 달기 (선택이지만 매우 추천)

이제 기능 3개가 완성됐으니 v1.0.0 태그를 달아보자.

`
git tag v1.0.0
git push origin v1.0.0
`

![version](https://img.shields.io/badge/version-v1.0.0-blue)
