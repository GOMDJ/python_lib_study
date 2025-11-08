# Git & GitHub 사용법 완벽 가이드

## 목차
- [Git 기본 개념](#git-기본-개념)
- [.gitignore 작성 규칙](#gitignore-작성-규칙)
- [기본 워크플로우](#기본-워크플로우)
- [브랜치 관리](#브랜치-관리)
- [충돌 해결](#충돌-해결)
- [고급 기능](#고급-기능)
- [유용한 명령어 모음](#유용한-명령어-모음)

---

## Git 기본 개념

### Git의 3단계 구조

```
Working Directory  →  Staging Area  →  Local Repository  →  Remote Repository
   (작업 폴더)         (git add)        (git commit)         (git push)
```

### 주요 명령어 설명

#### `git init`
현재 폴더를 Git 저장소로 초기화
- `.git` 폴더 생성 (Git 데이터 저장)

```bash
git init
```

#### `git add`
Working Directory → Staging Area
- 변경된 파일을 "커밋 대기 목록"에 올림

```bash
git add file.txt          # 특정 파일만
git add .                 # 현재 폴더 전체
git add *.py              # 패턴 매칭
```

#### `git commit`
Staging Area → Local Repository
- 변경사항을 로컬 저장소에 확정 저장
- 네 컴퓨터에만 저장됨 (GitHub에는 아직 안 올라감)

```bash
git commit -m "커밋 메시지"
```

#### `git push`
Local Repository → Remote Repository
- 로컬 커밋을 GitHub에 업로드

```bash
git push origin main      # main 브랜치를 origin(GitHub)에 푸시
git push -u origin main   # -u: 추적 관계 설정, 이후 git push만 쳐도 됨
git push                  # -u 설정 후 간단하게
```

#### `git pull`
Remote Repository → Local Repository + Working Directory
- GitHub의 최신 내용을 가져와서 로컬에 병합

```bash
git pull origin main
git pull                  # 추적 설정 후
```

---

## .gitignore 작성 규칙

### 기본 규칙

```gitignore
# 특정 파일 무시
filename.txt

# 특정 확장자 무시
*.log
*.pyc

# 디렉토리 무시
__pycache__/              # 모든 경로의 __pycache__ 폴더
node_modules/

# 특정 경로만 무시
/debug.log                # 루트의 debug.log만
logs/debug.log            # logs 폴더의 debug.log만

# 패턴 매칭
*.py[cod]                 # .pyc, .pyo, .pyd 파일
test?.py                  # test1.py, test2.py 등
test[0-9].py              # test0.py ~ test9.py

# 재귀 패턴
**/logs                   # 모든 위치의 logs 폴더
**/*.log                  # 모든 위치의 .log 파일

# 예외 처리
*.log
!important.log            # important.log는 추적

# 주석
# 이건 주석
*.tmp                     # 라인 끝 주석
```

### Python 프로젝트 추천 .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# 환경 변수
.env

# 로그
*.log
logs/
!logs/.gitkeep
```

### 주의사항

1. **이미 추적 중인 파일 제거**
```bash
git rm --cached 파일명
git rm -r --cached __pycache__
git commit -m "Remove ignored files"
```

2. **슬래시 위치의 의미**
```gitignore
build             # 모든 경로의 build
build/            # 모든 경로의 build 폴더만
/build            # 루트의 build만
/build/           # 루트의 build 폴더만
```

3. **패턴 테스트**
```bash
git check-ignore -v 파일명
```

---

## 기본 워크플로우

### 처음 시작 (로컬 → GitHub)

```bash
# 1. Git 저장소 초기화
git init

# 2. .gitignore 작성
# (파일 생성 후 내용 작성)

# 3. 파일 추가 및 커밋
git add .
git commit -m "Initial commit"

# 4. GitHub 저장소 생성 후 연결
git remote add origin https://github.com/유저명/저장소명.git

# 5. 브랜치 이름 확인/변경
git branch                    # 현재 브랜치 확인
git branch -m master main     # master → main으로 변경

# 6. 푸시
git push -u origin main
```

### 일상적인 작업

```bash
# 1. 파일 수정

# 2. 변경사항 확인
git status
git diff

# 3. 스테이징
git add .

# 4. 커밋
git commit -m "작업 내용 설명"

# 5. 푸시
git push
```

### 다른 컴퓨터에서 작업

```bash
# 처음 한 번만: Clone
git clone https://github.com/유저명/저장소명.git
cd 저장소명

# 작업 시작 전: Pull
git pull

# 작업 후: Push
git add .
git commit -m "메시지"
git push
```

---

## 브랜치 관리

### 브랜치 기본 명령어

```bash
# 브랜치 만들고 이동
git checkout -b 브랜치이름

# 브랜치 목록 확인
git branch                    # 로컬 브랜치
git branch -r                 # 원격 브랜치
git branch -a                 # 전체

# 브랜치 전환
git checkout 브랜치이름

# 브랜치 푸시 (첫 푸시)
git push -u origin 브랜치이름

# 브랜치 병합
git checkout main
git merge 브랜치이름

# 브랜치 삭제
git branch -d 브랜치이름              # 로컬
git push origin --delete 브랜치이름   # 원격
```

### 백업 브랜치 전략

```bash
# 날짜별 백업
git checkout -b backup-2025-01-08
git push -u origin backup-2025-01-08

# 기능별 브랜치
git checkout -b feature-json-parser
git checkout -b feature-error-handling

# 버전별 백업
git checkout -b v1.0-stable
git checkout -b v2.0-dev
```

### VSCode에서 브랜치 관리

1. 좌측 하단 브랜치 이름 클릭
2. "Create new branch..." 선택
3. 브랜치 이름 입력
4. 전환: 좌측 하단 클릭 → 브랜치 선택

---

## 충돌 해결

### 충돌이 발생하는 경우

```bash
git push
# ! [rejected]        main -> main (fetch first)

git pull
# CONFLICT (content): Merge conflict in test.py
```

### 충돌 해결 과정

#### 1. VSCode에서 충돌 확인

파일에 이렇게 표시됨:

```python
<<<<<<< HEAD (Current Change)
name = "Bob"           # 내가 수정한 내용
=======
name = "Alice"         # GitHub에 있던 내용
>>>>>>> origin/main (Incoming Change)
```

#### 2. VSCode 버튼으로 해결

```
Accept Current Change    # 내 거 선택
Accept Incoming Change   # GitHub 거 선택
Accept Both Changes      # 둘 다 선택
```

#### 3. 또는 수동 수정

```python
name = "Charlie"      # 직접 수정
```

#### 4. 충돌 해결 후 커밋

```bash
git add .
git commit -m "Resolve conflict"
git push
```

### 충돌 유형별 대처

**Case 1: 다른 파일 수정**
→ 자동 병합, 충돌 없음

**Case 2: 같은 파일, 다른 부분 수정**
→ 자동 병합, 충돌 없음

**Case 3: 같은 파일, 같은 줄 수정**
→ 충돌 발생, 수동 해결 필요

---

## 고급 기능

### 이전 커밋으로 되돌리기

```bash
# 커밋 이력 확인
git log
git log --oneline

# 특정 커밋 취소 (안전)
git revert 커밋해시

# 특정 커밋으로 되돌림 (위험 - 이후 커밋 삭제됨)
git reset --hard 커밋해시
git push --force
```

### Stash (임시 저장)

```bash
# 현재 작업 임시 저장
git stash

# 브랜치 전환
git checkout other-branch

# 작업 다시 불러오기
git stash pop

# Stash 목록
git stash list

# 특정 stash 불러오기
git stash apply stash@{0}
```

### 커밋 수정

```bash
# 마지막 커밋 메시지 수정
git commit --amend -m "새 메시지"

# 마지막 커밋에 파일 추가
git add 빠뜨린파일.txt
git commit --amend --no-edit
```

### 특정 파일 작업

```bash
# add 취소
git reset 파일명
git reset                     # 전체 취소

# 특정 파일 변경 이력
git log -- 파일명
git log -p 파일명             # 변경 내용까지

# 특정 커밋의 파일만 가져오기
git checkout 커밋해시 -- 파일명
```

### 차이점 비교

```bash
# 현재 작업 vs 마지막 커밋
git diff

# Staging Area vs 마지막 커밋
git diff --staged

# 브랜치 간 비교
git diff main feature-new

# 커밋 간 비교
git diff 커밋1 커밋2
```

### 태그 (버전 관리)

```bash
# 태그 만들기
git tag v1.0.0
git tag -a v1.0.0 -m "버전 1.0.0 릴리즈"

# 태그 푸시
git push origin v1.0.0
git push --tags               # 모든 태그

# 태그 목록
git tag

# 태그로 체크아웃
git checkout v1.0.0
```

---

## 유용한 명령어 모음

### 상태 확인

```bash
git status                    # 현재 상태
git log                       # 커밋 이력
git log --oneline             # 간단한 이력
git log --graph               # 그래프 형태
git remote -v                 # 원격 저장소 확인
git branch                    # 브랜치 목록
```

### 계정 설정

```bash
# 사용자 정보 설정
git config --global user.name "이름"
git config --global user.email "이메일"

# 프로젝트별 설정
git config user.name "이름"
git config user.email "이메일"

# 설정 확인
git config --list
git config user.name
git config user.email

# 설정 삭제
git config --global --unset user.name
git config --global --unset user.email
```

### 자격증명 관리 (macOS)

```bash
# 저장된 자격증명 삭제
git credential-osxkeychain erase
host=github.com
protocol=https

# (엔터 두 번)
```

### 원격 저장소 관리

```bash
# 원격 저장소 추가
git remote add origin URL

# 원격 저장소 확인
git remote -v

# 원격 저장소 변경
git remote set-url origin 새URL

# 원격 저장소 삭제
git remote remove origin

# 원격 브랜치 최신화
git fetch
git fetch --prune             # 삭제된 원격 브랜치 정리
```

### 기본 브랜치 설정

```bash
# Git 기본 브랜치를 main으로 설정
git config --global init.defaultBranch main

# 기존 브랜치 이름 변경
git branch -m master main
```

---

## 위험한 명령어 (주의!)

```bash
git reset --hard              # 작업 내용 완전 삭제
git push --force              # 원격 강제 덮어쓰기
git clean -fd                 # 추적 안 된 파일 삭제
```

**복구 불가능하니 정말 필요할 때만 사용!**

---

## 실전 팁

### 1. 커밋 메시지 작성 규칙

```bash
# 좋은 예
git commit -m "Add user authentication feature"
git commit -m "Fix login validation bug"
git commit -m "Update README with installation guide"

# 나쁜 예
git commit -m "수정"
git commit -m "aaa"
git commit -m "..."
```

### 2. 자주 커밋하기

작은 단위로 자주 커밋하는 게 좋음
- 문제 발생 시 되돌리기 쉬움
- 변경 이력 추적 용이

### 3. Push 전에 확인

```bash
git status
git diff
git log --oneline
```

### 4. Pull 먼저, Push 나중에

다른 사람과 협업할 때:
```bash
git pull                      # 작업 시작 전
# 작업...
git add .
git commit -m "메시지"
git pull                      # 혹시 모를 충돌 대비
git push
```

### 5. .gitignore는 처음부터

프로젝트 시작할 때 `.gitignore` 먼저 작성
- 불필요한 파일 커밋 방지
- 민감한 정보 유출 방지

---

## 문제 해결

### Push 안 될 때

```bash
# 원격이 최신인 경우
git pull
git push

# 충돌 발생 시
git pull
# 충돌 해결
git add .
git commit -m "Resolve conflict"
git push
```

### "invalid user name or token" 에러

1. VSCode에서 GitHub 로그인
2. 또는 키체인 삭제 후 재로그인

```bash
git credential-osxkeychain erase
host=github.com
protocol=https

git push  # 로그인 창 뜸
```

### 브랜치 이름 불일치

```bash
# master → main 변경
git branch -m master main
git push -u origin main
```

### 실수로 잘못 커밋한 경우

```bash
# 마지막 커밋 취소 (파일은 유지)
git reset HEAD~1

# 파일 수정 후 다시 커밋
git add .
git commit -m "올바른 커밋"
```

---

## 참고 자료

- [Git 공식 문서](https://git-scm.com/doc)
- [GitHub 가이드](https://docs.github.com)
- `.gitignore` 템플릿: https://github.com/github/gitignore
