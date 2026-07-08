# CS520: Theory of Programming Languages [🇰🇷](README.md)[🇬🇧](README.en.md)

## Logistics
- Instructor: Kihong Heo [🏠](https://kihongheo.kaist.ac.kr) [📧](mailto:kihong.heo@prosys.kaist.ac.kr)
- TAs [📧](mailto:cs520.ta@prosys.kaist.ac.kr)
  - Dongjae Lee [🏠](https://duncan020313.github.io/blog/)
- Lecture time: Tue/Thu 09:00 - 10:15
- Office hours (appointment required in advance):
  - Instructor: Tue 10:15 - 11:00
  - TAs: TBA
- Location: N1 102

## Course Description
> A strange story in a mirror where one side also sees the other side

> A true story not to forget when everyone chases glittering fakes

This course introduces the theoretical foundations of programming languages, centered on types, one of the core concepts of programming languages.
In particular, it aims to explore the following three aspects in depth:
- **Programming language**: Understand that types are not merely auxiliary tools for software development, but a core part of programming language design.
- **Logic**: Realize that types and propositions are the same concept, and further understand that programming languages and logic are two sides of the same mirror.
- **AI**: Discover the connection between programming languages and AI, and understand that AI that combines logic and intuition (neurosymbolic AI) is possible.

## Grades
#### Weight
- Homework: 30%
- Final exam: 50%
- Participation: 20%
  - This is a reward for students who actively participate and [spontaneously express in diverse ways what they have learned](hof.md).
  - I hope to see you at every class. [Attendance is not graded quantitatively](https://prosys.kaist.ac.kr/attendance/). That is because its value is not low enough to be quantified.

#### Grading Criteria
- Absolute grading: A >= 70, B >= 50, C >= 30, D >= 20, F < 20

## Textbooks
- Lecture materials will be provided.
- [Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/tapl/) (TAPL)
- [Advanced Topics in Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/attapl/) (ATAPL)
- [Proofs and Types](https://www.paultaylor.eu/stable/prot.pdf) (PAT)
- [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl.html) (PFPL)

## Commitment to Engagement
For a class where everyone is engaged, let us agree not to place any electronic devices (laptops, tablets, phones) on top of our desks.
The harmful effects of using electronic devices during class are already widely known([1](https://www.sciencedirect.com/science/article/pii/S0360131512002254?via%3Dihub),[2](https://www.nytimes.com/2025/08/21/opinion/mobile-phones-college-classrooms.html)).
Not only do they distract you, but they also greatly interfere with the people around you concentrating on the class.
Rather than everyone looking at their own separate monitor, I hope this will be a class where we all look at the same place together and have lively, freewheeling discussions.
The materials you need are in this repository, so if you want, please print them out in advance.

For more details, see the [article](https://prosys.kaist.ac.kr/engagement/).

## Homework
In this course, students learn how to prove theoretical facts and realize them in practice through programming homework.
In particular, we will mainly use the tools [here](TOOL.md).

All homework submissions are made through Github and Gradescope.
For each homework, the GitHub Classroom invitation URL for submission will be announced on the [board](https://github.com/prosyslab-classroom/cs424-program-reasoning/discussions).
Once you accept the invitation, a private personal repository for your homework will be created.
You may submit to that repository as many times as you want before the deadline, and
you can submit this repository to Gradescope to check the grading results.

If you submit after the deadline, it will be graded according to the following rules:
- One day late: 80% of the score
- Two days late: 50% of the score
- Three or more days late: 0%

## Academic Integrity
Students who violate academic integrity will receive an F. For details, please refer to the [KAIST School of Computing Honor Code](https://cs.kaist.ac.kr/content?menu=309).

Submitting materials found all over the world, such as Google search results or ChatGPT, as if they were your own creations is a violation of academic integrity.
All assignments in this course are, in principle, to be completed with your own ability.
Submitted assignments are automatically compared with existing works (other students' work, past students' work, AI-generated outputs, etc.), and if they are similar, they are judged as plagiarism.
This is a long-standing principle in academia, and it has not changed just because internet search or AI tools have appeared.

AI tools can reduce your effort, but they cannot cultivate deep thinking.
This is repeatedly discussed in several experiments ([1](https://cacm.acm.org/news/the-impact-of-ai-on-computer-science-education/),
[2](https://product.kyobobook.co.kr/detail/S000000600543)
[3](https://www.washingtonpost.com/technology/2026/07/07/how-stop-chatgpt-ruining-how-you-think/)).
Regardless of the type of AI model, [similar questions often receive similarly ordinary answers](https://arxiv.org/pdf/2510.22954).
Please do not easily throw away your precious learning opportunities.

## Course Schedule
|Week|Topic|Reading|Homework|
|-|------|-------|--------|
|0|[Functional Programming in OCaml](slides/lecture0.pdf)||HW0: Hello-world, OCaml Programming, Lean Game|
|1|[Introduction](slides/lecture1.pdf)|||
|2|[Lambda Calculus](slides/lecture2.pdf)|TAPL Part I|HW1. Sim|
|3|Simply Typed Lambda Calculus|TAPL Part II|HW2. SimPL|
|4|Natural Deduction|PAT Chap. 2||
|5|Curry-Howard Correspondence|PAT Chap. 3|HW3. Mini-Lean|
|6|Subtype|TAPL Part III|HW4: SimPLUS|
|7|Inductive Type|PAT Chap. 7||
|8|Recursive Type|TAPL Part IV||
|9|Polymorphic Type|TAPL Part V|HW4. Mini-Lean F|
|10|Type Operator|TAPL Part VI|HW5. Mini-Lean $\omega$|
|11|Dependent Type|ATAPL Part I||
|12|Calculus of Construction||HW6. Mini-Lean $\Pi$|
|13|Proof Automation (1)||HW7. Search-based Proof Automation|
|14|Proof Automation (2)||HW8. Agentic Proof Automation|
|-|Final Exam|||

## Related Courses
- [CS424: Program Reasoning](https://github.com/prosyslab-classroom/cs424-program-reasoning), KAIST
- [CS524: Program Analysis](https://github.com/prosyslab-classroom/cs524-program-analysis), KAIST

## Acknowledgments
The materials for this course were prepared with reference to the courses below.

- [Topics in Programming Language Theories](https://kwangkeunyi.snu.ac.kr/4190.510/25/), Seoul National Univ.
- [Constructive Logic](https://www.cs.cmu.edu/~fp/courses/15317-f00), CMU

## References
#### Basics
- [PL Wiki](https://github.com/prosyslab/pl-wiki/wiki)
- [Curry-Howard Correspondence](https://cs3110.github.io/textbook/chapters/adv/curry-howard.html)
- [Propositions as Types](https://dl.acm.org/doi/10.1145/2699407), CACM 2015
- [Software Foundations](https://softwarefoundations.cis.upenn.edu)

#### Lean
- [Logic and Proof](https://leanprover-community.github.io/logic_and_proof/index.html)
- [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/)
- [Functional Programming in Lean](https://lean-lang.org/functional_programming_in_lean/)
- [MathLib](https://github.com/leanprover-community/mathlib4)
- [CSLib](https://github.com/leanprover/cslib/)

#### Neurosymbolic AI
- [Formal Reasoning Meets LLMs](https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/)
- [Artificial Intelligence for Software Engineering: From Probable to Provable](https://cacm.acm.org/opinion/artificial-intelligence-for-software-engineering-from-probable-to-provable/)
- [AlphaProof and AlphaGeometry](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)
- [The End of the Coder](https://cacm.acm.org/news/the-end-of-the-coder/)
- [VeriSafe Agent](https://github.com/prosyslab/pl-wiki/wiki/VeriSafe-Agent)
- [Expecto](https://github.com/prosyslab/pl-wiki/wiki/Expecto)
