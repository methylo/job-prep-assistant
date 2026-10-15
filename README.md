# 나만의 취업준비 비서 (job-prep-assistant)

구직자 본인의 경험과 채용공고를 대조해 지원 판단, 서류 보완, 면접 준비, 지원 현황 관리를 돕는 클로드(Claude) 스킬(Skill)입니다.

프로필을 미리 채우지 않아도 대화에 나온 정보로 임시 프로필을 만들고 요청한 작업부터 진행합니다. 말하지 않은 경력·수치·자격은 만들지 않으며, 빈 정보는 `[확인 필요]`로 표시합니다.

## 주요 기능과 결과물

| 작업 | 결과물 |
| --- | --- |
| 채용공고 분석 | 직무수행내용·필요지식·필요기술·자격요건·우대사항 정리 |
| 지원 적합도 점검 | 충족·부분충족·미충족·정보 없음 분류, 지원 판단 근거, 보완 과제 |
| 이력서·경력기술 문장 보완 | 원문·보완본 대조표와 사실 확인 질문 |
| 자기소개서 경험 소재 정리 | 문항별 경험 후보와 단락 순서 |
| 면접 질문·답변 준비 | 공고·프로필 근거 질문 8~12개, 답변 키워드, 역질문 후보 |
| 취업 준비 플래너 | 지원 현황, 마감, 다음 과업과 기한 |

## 다운로드

설치용 파일은 [최신 릴리스(Releases)](https://github.com/methylo/job-prep-assistant/releases/latest)에서 내려받습니다.

- [job-prep-assistant.skill](https://github.com/methylo/job-prep-assistant/releases/latest/download/job-prep-assistant.skill): 스킬 배포 파일
- [job-prep-assistant.zip](https://github.com/methylo/job-prep-assistant/releases/latest/download/job-prep-assistant.zip): ZIP 업로드용 파일

두 파일의 내부 구성은 같습니다. 저장소 전체를 받는 `Code → Download ZIP`과 설치용 스킬 ZIP을 구분해 주세요. 설치용 ZIP에는 `job-prep-assistant/` 폴더와 그 안의 `SKILL.md`가 들어 있습니다.

## 설치

### Claude 웹·데스크톱

1. 위 다운로드에서 `job-prep-assistant.zip`을 내려받습니다.
2. Claude의 사용자 지정 스킬 관리 화면에서 ZIP 파일을 업로드하고 활성화합니다.
3. 새 대화에서 아래 문장으로 설치를 확인합니다.

```text
job-prep-assistant 스킬이 설치되었는지 확인해줘.
하는 일과 첫 입력만 1줄로 알려주고, 아직 시작하지 마.
```

계정·조직 설정에 따라 스킬 업로드 권한이 다를 수 있습니다. 메뉴와 요구 조건은 [Claude 공식 스킬 사용 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude)를 확인합니다.

### Claude Code

저장소를 내려받은 뒤 내부의 `job-prep-assistant/` 폴더를 개인 스킬 경로 `~/.claude/skills/`에 복사합니다. 파일 위치는 다음과 같아야 합니다.

```text
~/.claude/skills/job-prep-assistant/SKILL.md
```

설치한 뒤 Claude Code에서 아래 명령으로 호출합니다.

```text
/job-prep-assistant
```

설치 경로와 호출 방식은 [Claude Code 공식 스킬 문서](https://code.claude.com/docs/en/skills)를 기준으로 작성했습니다. 다른 에이전트 스킬(Agent Skills) 호환 환경에서는 해당 환경의 설치 경로와 도구 지원을 확인해야 합니다.

## 시작 예시

채용공고 원문과 본인 경험을 붙여넣습니다. 전체 프로필 양식은 필요한 시점에 요청하면 됩니다.

```text
job-prep-assistant로 이 공고를 분석하고 지원 여부를 점검해줘.

[채용공고 원문]
여기에 공고를 붙여넣습니다.

[내 경험]
- 희망 직무:
- 해 본 업무와 기간:
- 다뤄 본 도구와 실제 작업:
- 보유 자격:

말하지 않은 경력이나 숫자는 만들지 말고,
판단에 필요한 확인 질문을 3개 이하로 물어봐줘.
```

## 작업별 호출 예시

| 원하는 작업 | 입력 예시 |
| --- | --- |
| 공고 분석 | 이 공고의 자격요건과 우대사항을 나눠줘. |
| 지원 판단 | 내 경력으로 이 공고에 지원할지 근거를 정리해줘. |
| 서류 보완 | 이력서의 이 문장을 공고에 맞춰 고쳐줘. 없는 경력은 넣지 마. |
| 자기소개서 소재 | 이 문항에 쓸 내 경험 후보와 단락 순서를 뽑아줘. |
| 면접 준비 | 이 공고와 내 프로필에서 예상 질문과 답변 골격을 만들어줘. |
| 지원 현황 관리 | 지원한 공고와 준비 과업을 마감일 순으로 정리해줘. |

## 사용 범위

구직자 본인의 취업 준비용입니다. 채용담당자의 공고 작성·지원자 평가에는 사용하지 않습니다. 자기소개서는 경험 소재와 단락 순서를 제공하고, 본문은 사용자가 작성하는 방식입니다. 새 채용공고를 자동으로 수집하지 않습니다.

주민등록번호·상세 주소·가족 정보·건강 정보 등 직무와 무관한 개인정보는 입력하지 않습니다. 공고에 없는 전형 일정과 자격 시험 일정은 확인 대상으로 남깁니다. 결과를 지원 서류에 반영하기 전에 경력·수치·자격·마감과 공고 원문을 본인이 대조합니다.

## 저장소 구성

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── job-prep-assistant.skill
└── job-prep-assistant/
    ├── SKILL.md
    ├── references/
    │   ├── 내 프로필 양식.md
    │   └── 공고 분석 기준.md
    └── assets/
        └── 취업 준비 플래너.md
```

`SKILL.md`에는 실행 흐름과 출력 기준이, `references/`에는 프로필·공고 분석 양식이, `assets/`에는 플래너 양식이 들어 있습니다. 원본 스킬 파일을 풀어 열람용 소스로 등록했으며 본문은 변경하지 않았습니다.

## 버전

현재 배포 버전은 `v1.0.0`입니다. 저장소 첫 릴리스의 버전이며, 기존 스킬 원문을 수정한 버전은 아닙니다. 이후 변경 사항은 [CHANGELOG.md](CHANGELOG.md)에 기록합니다.

## 라이선스

Copyright © 2026 HONGS LAB (홍순성)

CC BY-NC 4.0 — 출처(HONGS LAB, 홍순성)를 표기하고 비영리 목적으로 사용·수정·공유할 수 있습니다. 자세한 조건은 [LICENSE](LICENSE)를 확인합니다.
