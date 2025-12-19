
# Assignment for Research and Development / AI

## Basic Assignment Rules

### Academic Integrity

- **No Cheating**: Students must complete all assignments independently unless group work is explicitly permitted. Using unauthorized materials, devices, or assistance during examinations or assignments is strictly prohibited.
- **No Copying or Plagiarism**: All work submitted must be original. Copying from other students, textbooks, websites, or any other sources without proper citation constitutes plagiarism and will result in serious consequences.
- **Proper Citation**: When referencing external sources, ideas, or quotes, students must provide appropriate citations following the required citation style (APA, MLA, Chicago, etc.).

---

## Problem

Find the values of unknown variables in the given parametric equation of a curve:

\[
x = \left( t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t) \sin(\theta) + X \right)
\]

\[
y = \left( 42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t) \cos(\theta) \right)
\]

### Unknowns
\[
\theta, \; M, \; X
\]

### Given Ranges

- \(0^\circ < \theta < 50^\circ\)
- \(-0.05 < M < 0.05\)
- \(0 < X < 100\)

### Parameter Range

- \(6 < t < 60\)

### Given Data

A list of \((x, y)\) points that lie on the curve for \(6 < t < 60\) is provided in the file:

- `xy_data.csv`

---

## Assessment Criteria

Candidates will be judged on the following:

- **L1 distance** between uniformly sampled points between expected and predicted curve (max score: 100)
- **Explanation** of the complete process and steps followed (max score: 80)
- **Submitted code / GitHub repository** (max score: 50)

> **Note:** Even if the final answer is incorrect or incomplete, partial credit will be awarded for a clear explanation of the approach and reasoning.

---

## Submission Format

- The only required and necessary result is the **value of the unknown variables**.
- Submission can be made by writing and copying equations in **LaTeX format** or by using the following website and including the equations in the `README.md` of the submitted GitHub repository:

  https://www.desmos.com/calculator/rf9lryxob

### Example Submission

```
\left(
t\cdot\cos(0.826) - e^{0.0742|t|}\cdot\sin(0.3t)\sin(0.826) + 11.5793,
42 + t\cdot\sin(0.826) + e^{0.0742|t|}\cdot\sin(0.3t)\cos(0.826)
\right)
```

This translates to a parametric curve plotted for:

\[
6 \le t \le 60
\]

---

### Bonus

- Additional code or mathematical techniques used to estimate or extract the variables will be considered a plus.
