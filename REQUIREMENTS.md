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

### 2. Disallowed Tactics

Automated proof tactics are not allowed in this assignment such as `simp`, `aesop`, `grind`, `omega` and their variants.
You are expected to write your own proofs using basic tactics such as `intro`, `apply`, `cases`, and `induction`.

The course environment provides a tactic checker to help you avoid using disallowed tactics.
The tactic checker will scan your Lean files for disallowed tactics and report any violations.
To scan the repository, run the following command in the root directory of this repository:
```console
make check
```

### 3. Basic Proof Engineering Practices (Excerpted from Software Foundation)

Lean, like any other programming language, has conventions and best practices for writing good software. 
Lean takes inspiration from object-oriented programming in favoring the use of encapsulation. 
In OOP, it is considered poor style to expose the fields of an object in its interface; 
instead, those fields should be accessible only by an object's methods (like getters and setters). 
Doing so hides the object's definition, so that, if its fields or implementation ever change, 
the interface it exposes to the outside world remains the same. 
In simple examples, such conventions may seem overly pedantic; 
in complex codebases, they are the only way to maintain crucial invariants that prevent a system from becoming unmaintainable.

The same principle applies to programs and proofs in Lean.
In your assignments, you will be proving facts about functions entirely through their _simplification rules_, also known as _characterization lemma_,
rather than using `rfl` to unfold their implementations invisibly. 
This makes every computation step visible and lets a proof rely on a function's interface rather than its definition.

For example, suppose addition is defined by recursion on its second argument:
```lean
def add (n m : Nat) : Nat :=
  match m with
  | 0 => n
  | Nat.succ m' => Nat.succ (add n m')
```

The following two theorems provide a characterization of the behavior of `add`:
```lean
theorem add_zero (n : Nat) : add n 0 = n := by
  rfl

theorem add_succ (n m : Nat) : add n (succ m) = succ (add n m) := by
  rfl
```
Note that the characterization lemmas make using `rfl` to simplify expressions unnecessary.
Instead, we can rewrite by these theorems anywhere we want to describe how `add` evaluates. 
In real-world Lean developments, the style of writing proofs using simplification rules is both standard and expected.

In assignments, we mark definitions with `attribute [irreducible]` to prevent this kind of unfolding.
This means that `rfl` cannot unfold these definitions behind the scenes: after rewriting by their simplification rules, 
it closes only the remaining straightforward equality. 
For example, using our simplification rules, we can carry out a simple proof about natural numbers:
```lean
attribute [irreducible] add

theorem add_zero_zero (n : Nat) : add (add n 0) 0 = n := by
  rw [add_zero, add_zero]

theorem add_one (n : Nat) : add n (Nat.succ 0) = Nat.succ n := by
  rw [add_succ, add_zero]
```

In assignments, students are required to follow such proof engineering practices:
- Do not change the location of `attribute [irreducible]`
- Define and prove simplification lemmas for definitions before `attribute [irreducible]`
- Prove provided theorems after `attribute [irreducible]` using the simplification lemmas
