# Requirements for Programming Assignments

### 1. Directory Structure
Students are not permitted to change directory structures, which includes adding new files, removing existing files, and moving files into another directory.

### 2. Program Structure
Students are also not permitted to change types of predefined functions.
All the functions they implement must have the same type as described in the module or module signatures.
However, students can change `let` to `let rec`, or add new functions in existing files, if needed.

### 3. Basic Software Engineering Practices
All source code must be clearly written following basic software engineering practices.
Especially,
- Formatting: All source code must be properly formatted using `ocamlformat`. Students are required to format their source code by using `make fmt` or setting their editor. Ill-formatted source code will be automatically rejected for grading.
- Warning: All source code must not have any warning. Students are required to correct all warnings in their source code before the final submission. For convenience, `make` does not strictly check warnings. However, `make test` will reject any source code with warnings.
- Coverage: Your source code must be well-tested. By running `make coverage`, your code coverage must exceed the specified threshold for each assignment. If your code coverage is below the threshold, your code will not be graded. You can add more tests in the `test` directory and modify the `test/dune` file to enhance coverage. Note that `make coverage` runs for only a minute, so you should maximize your test coverage within this time constraint.

### 4. Value-oriented Programming
We encourage the practice of value-oriented programming.
If you use `ref`, `while`, and `for` in your source code, your code will not be graded.
Refer to the [class introduction](https://github.com/prosyslab-classroom/cs524-program-analysis?tab=readme-ov-file#%EC%88%99%EC%A0%9C-homework) for more details.

### 5. Checking the Requirements
To check the requirements, we provide a `Makefile` that includes the following commands:
- `make test`: Check the source code for formatting, warnings, and value-oriented programming.
- `make coverage`: Check the source code for code coverage.

# Requirements for Proof Assignments
### 1. Directory Structure & Program Structure
Same as programming assignments.

### 2. Basic Proof Engineering Practices

Proofs must treat definitions as encapsulated implementation details.
Do not rely on `rfl` to unfold a function implicitly in later proofs (so-called
definitional-equality abuse). Instead, expose the behavior of a function through
named simplification, or characterization, lemmas and use `rw`.

- For every branch of a `match` or recursive definition, prove a lemma describing
  that branch's behavior.
- For educational purposes, automatic simplification tactics such as `simp` and
  `dsimp` (and similar automation) are prohibited. Students must expose the
  rewriting steps explicitly using the required lemmas and `rw`.
- After the characterization lemmas have been proved, definitions may be marked
  `[irreducible]` when appropriate; later proofs must continue to use the lemmas
  rather than the implementation.
- Using `rfl` to prove the characterization lemmas themselves is acceptable: in
  that situation it verifies the definition's individual computation rule.

For example, suppose addition is defined by recursion on its second argument:

```lean
namespace ProofExample

def add (n m : Nat) : Nat :=
  match m with
  | 0 => n
  | Nat.succ m' => Nat.succ (add n m')

theorem add_zero (n : Nat) : add n 0 = n := by
  rfl

theorem add_succ (n m : Nat) :
    add n (Nat.succ m) = Nat.succ (add n m) := by
  rfl

attribute [irreducible] add

theorem add_zero_zero (n : Nat) : add (add n 0) 0 = n := by
  rw [add_zero, add_zero]

theorem add_one (n : Nat) : add n (Nat.succ 0) = Nat.succ n := by
  rw [add_succ, add_zero]

end ProofExample
```

Here `add_zero` and `add_succ` are the two rewrite rules corresponding to the
two branches of `add`. In `add_zero_zero`, the first `rw [add_zero]` changes
`add (add n 0) 0` to `add n 0`, and the second changes it to `n`; the goal is
then reflexive. In `add_one`, `add_succ` first changes the left side to
`Nat.succ (add n 0)`, and `add_zero` reduces the inner addition to `n`.
The proof therefore documents the function's interface instead of depending
on its hidden implementation.
