# CS520: 프로그래밍 언어 이론 (Theory of Programming Languages)

## 수업정보 Logistics
- 교수 Instructor: [허기홍 Kihong Heo](https://kihongheo.kaist.ac.kr) (kihong.heo@prosys.kaist.ac.kr)
- 조교 TAs (mailing list: cs520.ta@prosys.kaist.ac.kr)
  - tba
- 강의 시간 (Time): 월/수 Mon/Wed 09:00 - 10:15
- 면담 시간 (Office hours) (사전 약속 필요 by appointment):
  - 교수 Instructor: Mon 10:15 - 11:00
  - 조교 TAs: Mon 10:15 - 11:00
- 강의실 Location: N1 102

## 강의 소개 Course Description
> 한 쪽을 보면 다른 쪽도 보이는 신기한 거울 속 이야기

> 모두가 빛나는 가짜를 쫓을 때 잊지 말아야할 진짜 이야기

본 강의에서는 프로그래밍 언어의 핵심 개념 중 하나인 타입을 중심으로 프로그래밍 언어의 이론적 토대를 소개한다.
특히, 아래 세 가지 측면을 깊이 탐구하는 것을 목표로 한다.
- **프로그래밍 언어**: 타입이 단순히 SW 개발의 보조 도구가 아니라 프로그래밍 언어 설계의 핵심임을 이해한다.
- **논리**: 타입과 명제가 같은 개념임을 깨닫고, 나아가 프로그래밍 언어와 논리가 거울의 양면임을 이해한다.
- **AI**: 프로그래밍 언어와 AI가 연결될 기회를 발견하고, 논리와 직관을 아우르는 AI(neurosymbolic AI)가 가능함을 이해한다.

본 강의에서는 [쉬운 전문 용어](https://easyword.kr)를 사용하여 [소박하게 지식을 전달한다](https://prosys.kaist.ac.kr/easy-word/).

## 성적 Grading
- 숙제 Homework: 50%
- 기말고사 Final Exam: 40%
- 참여 Participation: 10%
  - 적극적인 참여로 본인이 배운 바를 [스스로 다채롭게 내뿜는](hof.md) 학생들을 위한 보상입니다.
    - This is for students who actively participate and express what they have learned [in a diverse way](hof.md).
  - 매 수업 시간에 항상 여러분을 만날 수 있기를 기대합니다. [출석은 정량평가하지 않습니다](https://prosys.kaist.ac.kr/attendance/). 정량화할 만큼 가치가 낮지 않기 때문입니다.
    - I always look forward to seeing you in every class. [Attendance is not quantitatively assessed](https://prosys.kaist.ac.kr/attendance/) because it is too valuable to be reduced to a mere number.

## 교재 Textbook
- 강의자료가 제공됩니다. Lecture slides will be provided.
- [Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/tapl/) (TAPL)
- [Advanced Topics in Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/attapl/) (ATAPL)
- [Proofs and Types](https://www.paultaylor.eu/stable/prot.pdf) (PAT)
- [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl.html) (PFPL)

## 몰입을 위한 약속 Promises for Engagement
모두가 몰입하는 강의를 위해 모든 전자기기(노트북, 태블릿, 핸드폰)는 책상 위에 올려놓지 않기로 합시다.
수업 중 전자기기를 사용하는 것이 끼치는 악영향은 이미 널리 알려져 있습니다([참고1](https://www.sciencedirect.com/science/article/pii/S0360131512002254?via%3Dihub),[참고2](https://www.nytimes.com/2025/08/21/opinion/mobile-phones-college-classrooms.html)).
본인의 주의를 산만하게 할 뿐만 아니라 주변 사람들이 수업에 집중하는 데도 큰 방해가 됩니다.
모두가 각자 따로 모니터를 보기 보다는 함께 같은 곳을 보며 왁자지껄 난상토론하는 수업이 되길 바랍니다.
필요한 자료는 이 저장소에 있으니 원한다면 미리 인쇄해서 오세요.

자세한 이야기는 [기사](https://prosys.kaist.ac.kr/engagement/)를 참고하세요.

For a lecture where everyone can stay fully engaged, let’s agree not to keep any electronic devices (laptops, tablets, phones) on the desk.
The negative effects of using electronic devices during class are already well-documented ([Ref1](https://www.sciencedirect.com/science/article/pii/S0360131512002254?via%3Dihub), [Ref2](https://www.nytimes.com/2025/08/21/opinion/mobile-phones-college-classrooms.html)).
They not only distract you, but also seriously interfere with the ability of those around you to focus.

Instead of everyone looking at separate screens, I hope this will be a class where we look at the same place together and actively talk with one another.
All necessary materials are available in this repository, so please print them out in advance if you’d like.

## 숙제 Homework
이 강의에서 학생들은 프로그래밍 숙제를 통해 이론적 사실을 증명하고 실제로 실현하는 법을 배웁니다.
특히 [여기](TOOL.md)에 있는 도구를 주로 사용할 예정입니다.

모든 숙제 제출은 Github와 Gradescope를 통해서 이루어집니다.
매 숙제마다 제출을 위한 GitHub Classroom 초대 URL이 [게시판](https://github.com/prosyslab-classroom/cs424-program-reasoning/discussions)에 공지됩니다.
초대를 수락하면, 여러분의 숙제를 위한 비공개 개인 저장소가 만들어질 것입니다.
여러분은 제출 기한 이전에 원하는 만큼 해당 저장소에 제출할 수 있고,
이 저장소를 Gradescope에 제출하여 채점 결과를 확인할 수 있습니다.

기한을 넘겨서 제출할 시 아래와 같은 규정에 따라 채점합니다:
- 하루 늦을 시 점수의 80%
- 이틀 늦을 시 점수의 50%
- 사흘 이상 늦을 시 0%

All submissions will be managed using GitHub and Gradescope.
For each assignment, a unique invitation URL for GitHub Classroom will be posted in the [Discussion board](../../discussions).
Once you accept the invitation, a private repository for your assignment will be created.
You can push as many commits as you want before the deadline.
You can submit this repository to Gradescope to check your grading results.

The late homework policy is as follows:
- 80% credit for one day late
- 50% credit for two days late
- NO credit given after two days late

## 학문 윤리 Academic Integrity
학문 윤리를 어긴 수강생은 F를 받습니다. 자세한 사항은 [KAIST 전산학부 명예규정](https://cs.kaist.ac.kr/content?menu=309)을 참고하십시오.

세상에 널린 자료(예: 구글 검색, ChatGPT)를 참고하는 것은 좋지만, 그대로 베끼는 것은 윤리에 어긋납니다.
제출한 과제는 기존 저작물(다른 수강생, 과거 수강생, AI 생성물 등)과 자동으로 비교하여 표절물을 검사합니다.
완전히 본인의 것으로 재창조하지 않고 기존 저작물과 비슷한 경우는 표절로 판단합니다.
이는 학계의 오래된 원칙이며 AI 도구가 등장했다고 해서 달라진 것은 없습니다.

Students who violate academic integrity will get an F.
See [the KAIST CS honor code](https://cs.kaist.ac.kr/content?menu=309).

It’s fine to refer to readily available resources (e.g., Google searches, ChatGPT), but copying them directly is unethical. Submitted assignments will be automatically compared to existing works (other students’ work, past students’ work, AI-generated content, etc.) to check for plagiarism. If the work closely resembles existing material without being fully recreated as your own, it will be considered plagiarism. This principle remains unchanged even in the AI era.

## 강의 계획 Schedule
|Week|Topics|Reading|Homework|
|-|------|-------|--------|
|0|[Functional Programming in OCaml](slides/lecture0.pdf)||<img src="icons/github-classroom.png" width="16" />HW0: Hello-world, OCaml Programming, Lean Game|
|1|[Introduction](slides/lecture1.pdf)|||
|2|[Lambda Calculus](slides/lecture2.pdf)|TAPL Part I|HW1. Sim|
|3|Simply Typed Lambda Calculus|TAPL Part II|HW2. SimPL|
|4|Natural Deduction|PAT Chap. 2||
|5|Curry-Howard Correspondence|PAT Chap. 3|HW3. Mini-Lean|
|6|Subtype|TAPL Part III|HW4: SimPLUS |
|7|Inductive Type|PAT Chap. 7||
|8|Recursive Type|TAPL Part IV||
|9|Polymorphic Type|TAPL Part V||
|10|Type Operator|TAPL Part VI||
|11|Dependent Type|ATAPL Part I||
|12|Calculus of Construction|||
|13|Proof Automation|||
|-|Final Exam|||

## 관련 강의 Related & Advanced Course
- [CS424: 프로그램 논증 (Program Reasoning)](https://github.com/prosyslab-classroom/cs424-program-reasoning), KAIST
- [CS524: 프로그램 분석 (Program Analysis)](https://github.com/prosyslab-classroom/cs524-program-analysis), KAIST

## 감사 Acknowledgement
이 강의의 자료는 아래 강의의 자료를 참고하여 작성하였습니다.

Part of the material is based on lecture notes from similar courses.
- [Topics in Programming Language Theories](https://kwangkeunyi.snu.ac.kr/4190.510/25/), Seoul National Univ.
- [Constructive Logic](https://www.cs.cmu.edu/~fp/courses/15317-f00), CMU

## 참고 References
#### 기본 Preliminaries
- [PL Wiki](https://github.com/prosyslab/pl-wiki/wiki)
- [Curry-Howard Correspondence](https://cs3110.github.io/textbook/chapters/adv/curry-howard.html)
- [Propositions as Types](https://dl.acm.org/doi/10.1145/2699407), CACM 2015
- [Software Foundations](https://softwarefoundations.cis.upenn.edu)

#### Lean/Rocq
- [Logic and Proof](https://leanprover-community.github.io/logic_and_proof/index.html)
- [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/)
- [Functional Programming in Lean](https://lean-lang.org/functional_programming_in_lean/)
- [MathLib](https://github.com/leanprover-community/mathlib4)
- [CSLib](https://github.com/leanprover/cslib/)

#### 논리-직관 융합 AI(neurosymbolic AI)
- [Formal Reasoning Meets LLMs](https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/)
- [AlphaProof and AlphaGeometry](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)
- [VeriSafe Agent](https://github.com/prosyslab/pl-wiki/wiki/VeriSafe-Agent)
- [Expecto](https://github.com/prosyslab/pl-wiki/wiki/Expecto)
