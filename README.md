# 🚀파이썬 슈팅게임🔫

2025-1학기 오픈소스SW개론 1분반 10조의 <Python으로 만든 간단한 아케이드 슈팅 게임>

----------------

## 👥 팀원 역할 (가나다 순)

| 👤 이름     | 🛠️ 역할 설명                                  |
|------------|-----------------------------------------------|
| 😎 고다경   | 프로젝트 세팅 및 Merge 관리 |
| 🎮 김연준   | 스테이지(Stage) 구현 담당                         |
| 🤖 조민정   | 적(Enemy) 구현 담당                        |
| 🕹️ 허서윤  | 플레이어(Player) 구현 담당                      |

## 👩🏻‍💻 기술 스택

- **Python** (사용 언어)
- **Pygame** (라이브러리)

## 🚀 기능 요약

- 플레이어 조작하여 총알 쏘기
- 적 랜덤 생성
- 목숨 3개, 모두 잃으면 Game Over

## 📸 게임 화면
**➡️ 게임 화면 사진**
<img width="998" alt="스크린샷 2025-06-04 오후 6 32 02" src="https://github.com/user-attachments/assets/feeabdec-8acf-4e25-a07b-7f844b18b79d" />

**➡️ 게임 플레이 영상 <br>**
https://github.com/user-attachments/assets/5383106f-8a2d-4590-8bc5-2e87dbc7ece0

-----

## 🔀 브랜치 전략: GitHub Flow
- `master` 브랜치 : 팀장이 PR 확인 후 merge
- 각 역할 담당마다 `담당명/기능명` 브랜치 생성 (ex. 플레이어 이동 기능 구현시, `player-move`)
- 기능 구현 완료 후 `Pull Request` 생성  
- 코드 리뷰 후 `master` 브랜치로 `Merge`함 
- `Merge`는 팀장만 진행

## 📄 이슈 및 PR 템플릿 사용
### 🎯 Issue Label
| 태그        | 설명                          |
|-------------|-------------------------------|
| `feat`      | 새로운 기능 구현               |
| `fix`       | 기능 버그 및 오류 수정         |
| `asset`     | 이미지 및 에셋 수정            |
| `setting`   | 프로젝트 세팅 관련             |
| `docs`      | 문서 관련                      |
| `discussion`| 논의용 이슈                    |
| `style`     | 코드 주석 등 스타일 변경        |

### 🧾 Issue 템플릿

- 제목: `[라벨] 구현할 기능명`
```markdown
## 📔 Description
간단한 이슈 설명 작성

## 🐈 Todo
- [ ] 해야 할 작업 1
- [ ] 해야 할 작업 2
```

### 🧾 PR 템플릿
```markdown
## 🚀 Background
- 해당 PR의 간단한 배경 설명

## 🥥 Contents
- 구현한 기능 목록 나열

## 🧪 Testing
- 기능 정상 작동 여부 및 테스트 방식

## 📸 Screenshot
- 이미지 또는 영상 첨부

## ⚓ Related Issue
- close #1
```

## 🔑 Commit & Branch 컨벤션
### 🧾 Commit 컨벤션
- 이슈 라벨과 동일한 태그를 커밋 메시지 앞에 붙여 통일성 있는 커밋 작성
- `라벨: 작업 내용 및 구현 기능` 형태로 작성하여, 이슈와 커밋의 연관성을 쉽게 파악 가능
  
**예시**
- `feat: 적 클래스 3가지 유형 구현`
- `fix: 점프 높이 수정`
- `asset: 플레이어 캐릭터, 총알 이미지 구현`

### 🧾 Branch 컨벤션
- 브랜치명만으로도 작업 목적을 파악할 수 있도록 **기능 단위로 브랜치명 설정** 
- 각자 맡은 역할 기반으로 브랜치명을 작성해 **의도를 명확히 표현**
  
- 브랜치명 형식: `<담당기능>-<세부내용>`
- 하이픈(`-`)으로 단어 구분

**예시**
| 기능 영역 | 브랜치명 예시             | 설명                         |
|------------|---------------------------|------------------------------|
| 플레이어   | `player-move`             | 플레이어 이동 기능 구현      |
| 적       | `enemy-character`    | 적 클래스 구현          |
| 스테이지   | `stage-life_system` | 스테이지 목숨 설정       |

----

## 📂 프로젝트 구조
```
📦shooting-game
 ┣ 📂assets
 ┃ ┣ 📜bullet.png
 ┃ ┣ 📜enemy_p.png
 ┃ ┣ 📜enemy_s.png
 ┃ ┣ 📜enemy_t.png
 ┃ ┣ 📜player.png
 ┃ ┗ 📜stageBackground.png
 ┣ 📂docs
 ┃ ┗ 📜-브랜치명--구현할-기능명.md
 ┗ 📂src
 ┃ ┣ 📂enemy
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜enemy.cpython-312.pyc
 ┃ ┃ ┗ 📜enemy.py
 ┃ ┣ 📂player
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜bullet.cpython-312.pyc
 ┃ ┃ ┃ ┗ 📜player.cpython-312.pyc
 ┃ ┃ ┣ 📜bullet.py
 ┃ ┃ ┗ 📜player.py
 ┃ ┣ 📂stage
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜stage.cpython-312.pyc
 ┃ ┃ ┗ 📜stage.py
 ```
