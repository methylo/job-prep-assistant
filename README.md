# 나만의 취업준비 비서 (job-prep-assistant)

구직자 개인의 목표·희망 조건 설정부터 공고 비교, 지원 서류 작성·수정, 포트폴리오, 면접 연습, 입사 제안 비교까지 돕는 스킬(Skill)입니다. 확인된 경험으로 작업하고, 없는 경력·자격·수치는 만들지 않습니다.

**세부 파일 보기:** [스킬 폴더](job-prep-assistant/) · [실행 지침 SKILL.md](job-prep-assistant/SKILL.md) · [작업별 기준](job-prep-assistant/references/) · [상태·플래너 양식](job-prep-assistant/assets/)

## 작업별 기능

| 단계 | 처리 내용 | 결과물 |
| --- | --- | --- |
| 목표·경험 | 필수·선호·제외 조건과 경험 근거 정리 | 임시 프로필·직무 후보 |
| 공고·회사 | 첨부 판독, 조건 추출, 회사 정보 확인 | 공고 분석·조건 비교 |
| 지원 판단 | 요건과 희망 조건을 따로 대조 | 지원 판단 근거·우선순위·보완 과제 |
| 이력서·경력기술서 | 전체 초안·기존 원고 수정 | 요청 범위의 본문과 변경 이유 |
| 자기소개서 | 소재 정리·전체 초안·기존 원고 수정 | 문항별 본문·사실 확인·분량 검산 |
| 작업물·포트폴리오 | 작업 선정·기여 설명·구성·검수 | 구성안·설명문·요청 시 파일 |
| 면접 | 준비 자료 또는 한 질문씩 연습 | 답변 피드백·후속 질문 |
| 지원 관리·회고 | 일정·지원 상태·결과 피드백 관리 | 플래너·다음 행동 |
| 입사 결정 | 제안 조건과 개인 기준 비교 | 미확인 조건·확인 질문·선택 근거 |

단계는 필수 순서가 아닙니다. 공고 분석·서류 수정·면접 연습 등 지금 필요한 작업에서 시작합니다. 실제 상담과 강의용 가상 시연은 분리해 관리합니다.

## 다운로드와 설치

[최신 릴리스(Releases)](https://github.com/methylo/job-prep-assistant/releases/latest)에서 설치용 파일을 내려받습니다.

- [job-prep-assistant.zip](https://github.com/methylo/job-prep-assistant/releases/latest/download/job-prep-assistant.zip): ZIP 업로드용
- [job-prep-assistant.skill](https://github.com/methylo/job-prep-assistant/releases/latest/download/job-prep-assistant.skill): 같은 내부 파일을 담은 스킬 배포용

두 파일에는 아래 스킬 파일 12개가 동일하게 들어 있습니다. 저장소 전체를 받는 `Code → Download ZIP`과 설치용 ZIP을 구분합니다.

### Claude 웹·데스크톱

1. 위의 `job-prep-assistant.zip`을 내려받습니다.
2. 클로드(Claude)의 사용자 지정 스킬 관리 화면에서 ZIP 파일을 업로드하고 활성화합니다.
3. 새 대화에서 아래 문장으로 설치를 확인합니다.

```text
job-prep-assistant 스킬이 설치되었는지 확인해줘.
하는 일과 첫 입력만 1줄로 알려주고, 아직 시작하지 마.
```

계정·조직별 업로드 권한과 요구 조건은 [Claude 공식 스킬 사용 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude)를 확인합니다.

### Claude Code

내려받은 내부의 `job-prep-assistant/` 폴더를 개인 스킬 경로 `~/.claude/skills/`에 복사합니다.

```text
~/.claude/skills/job-prep-assistant/SKILL.md
```

설치 후 다음 명령으로 호출합니다.

```text
/job-prep-assistant
```

경로와 호출 방식은 [Claude Code 공식 스킬 문서](https://code.claude.com/docs/en/skills)를 확인합니다. 다른 에이전트 스킬(Agent Skills) 호환 환경은 해당 환경의 설치 경로와 도구 지원을 확인해야 합니다.

## 호출 예시

```text
job-prep-assistant로 이 공고와 내 경험을 비교해줘.
공고 요건과 내 희망 조건을 따로 점검하고 확인 질문은 3개 이하로 해줘.

[채용공고 원문]
여기에 공고를 붙여넣습니다.

[내 경험·희망 조건]
희망 직무, 해 본 업무와 기간, 다뤄 본 도구, 보유 자격,
통근·급여·근무시간 등 확인된 조건을 적습니다.
```

```text
첨부한 이력서와 자기소개서를 이 공고에 맞춰 수정해줘.
전체 수정본, 주요 변경 이유, 확인할 사실을 나눠줘.
없는 경력과 숫자는 만들지 마.
```

```text
이 공고로 면접 연습해줘.
한 질문씩 묻고 내 답변을 받은 뒤 피드백과 후속 질문을 줘.
```

## 세부 파일 구성

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── job-prep-assistant.skill
└── job-prep-assistant/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   ├── icon.svg
    │   ├── 작업 카드.md
    │   ├── 진행 상황 요약.md
    │   └── 취업 준비 플래너.md
    ├── references/
    │   ├── 공고 분석 기준.md
    │   ├── 내 프로필 양식.md
    │   ├── 면접 연습과 입사 판단.md
    │   ├── 서류 작성과 검수.md
    │   └── 작업물과 포트폴리오.md
    └── scripts/
        └── count_text.py
```

`SKILL.md`는 공통 원칙과 작업별 참조 경로를 담습니다. 상세 기준은 `references/`, 출력 양식·아이콘은 `assets/`, 화면 표시 정보는 `agents/openai.yaml`에 분리되어 있습니다. `scripts/count_text.py`는 실제 제출 본문의 글자 수와 UTF-8 바이트 수를 계산합니다. 작업에 필요한 세부 파일만 읽는 구조입니다.

저장소의 개별 파일과 배포 패키지의 내부 파일은 일치합니다. 루트의 `.skill`은 기존 다운로드 주소를 유지하기 위한 패키지이며, 내용을 읽거나 수정할 때는 위 스킬 폴더를 사용합니다.

## 사용 범위와 확인 기준

구직자 본인의 취업 준비용이며 채용담당자의 지원자 평가에는 사용하지 않습니다. 자기소개서는 소재만 정리하거나 전체 초안·수정본을 작성하는 등 요청한 범위를 따릅니다. 회사 정보·공고 탐색·문서 제작에는 해당 환경의 검색·파일 도구가 필요합니다.

직무와 무관한 민감정보는 입력하지 않습니다. 사용자 진술·원문 대조·파일 검수를 구분하며 초안 작성과 제출 준비 완료, 서류 완성과 실제 접수 완료를 구별합니다. 지원서 제출·메일 발송·입사 수락은 별도 실행 지시가 필요합니다. 도구로 실제 등록하지 않은 자동 저장·알림은 약속하지 않습니다.

## 버전과 라이선스

현재 버전은 `v1.1.0`입니다. 이전 `.skill`의 파일 4개 대신 최신 `.zip`에 들어 있던 파일 12개를 개별 소스로 반영했습니다. 최신 원문의 기능은 새로 작성하거나 변경하지 않았습니다. 변경 사항은 [CHANGELOG.md](CHANGELOG.md)에 기록합니다.

Copyright © 2026 HONGS LAB (홍순성)

CC BY-NC 4.0 — 출처(HONGS LAB, 홍순성)를 표기하고 비영리 목적으로 사용·수정·공유할 수 있습니다. 자세한 조건은 [LICENSE](LICENSE)를 확인합니다.
