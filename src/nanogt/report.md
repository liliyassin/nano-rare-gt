# Code Study Note: `src/nanogt/report.py`

File studied: `/Users/suzie/Projects/nano-rare-gt/src/nanogt/report.py`

Related files:
- `src/nanogt/scoring.py`
- `src/nanogt/disease.py`
- `src/nanogt/gene.py`
- `src/nanogt/cli.py`
- `src/nanogt/catalog.py`

Study goal:
Understand what `report.py` is, why it exists, how it turns NanoGT scoring results into a readable Markdown report, what each line-range does, and what assumptions/limitations are built into the report format.

---

## 1. Plain-English identity

`report.py` is the report writer for NanoGT.

It does not decide which gene therapy program is best. That decision has already been made by `scoring.py`.

Instead, `report.py` takes the ranked scoring results and turns them into a human-readable Markdown document.

The easiest mental model:

```text
scoring.py = calculates the scores
report.py  = writes the scores into a readable report
```

Or even more simply:

```text
report.py = the “print the results nicely” file
```

For a non-coder biomedical researcher, think of this file as the difference between:

```text
Raw spreadsheet values
```

and:

```text
A formatted mini-report with headings, tables, and explanations
```

---

## 2. Why this file exists

NanoGT produces a ranked list of gene therapy precedents. But a ranked Python object is not friendly to read.

The user needs to see:
- The disease being analysed.
- The primary gene.
- The gene coding sequence size.
- The inheritance pattern.
- The affected tissues.
- The top matching gene therapy programs.
- The score breakdown for each match.
- The plain-English rationale notes from the scoring system.
- Any programs excluded because the gene does not fit into the vector.

`report.py` exists to assemble all of that into one Markdown string, then save it as a `.md` file.

This matters because Markdown is easy to:
- Read in a text editor.
- Convert to PDF.
- Paste into notes.
- Use in dissertation/project documentation.
- Compare beside the code.

---

## 3. How this file fits into the project data flow

High-level NanoGT flow:

```text
1. User provides or selects a rare disease
2. disease.py gathers disease metadata
3. gene.py gathers gene/protein metadata
4. catalog.py provides known GT precedent data
5. db.py stores catalog data in SQLite
6. scoring.py scores each GT precedent against the query disease/gene
7. report.py turns those scores into a Markdown report
8. CLI shows/saves the output for the user
```

`report.py` is near the end of the pipeline.

It depends on earlier files doing their jobs correctly:
- If `disease.py` gives poor disease tissue data, the report will display poor tissue data.
- If `gene.py` gives missing CDS length, the report will show `unknown`.
- If `scoring.py` scores incorrectly, the report will faithfully display incorrect scores.

Important point:

```text
report.py formats results; it does not validate the science.
```

---

## 4. Inputs and outputs

### Inputs

`report.py` mainly receives one object:

```python
MatchResult
```

That object bundles together:
- A `DiseaseInfo` object.
- A `GeneInfo` object.
- A list of `ScoreBreakdown` objects from `scoring.py`.
- A number saying how many top matches to include.

### Outputs

There are two outputs depending on which function is called:

1. `generate_report(result)`
   - Returns Markdown text as a Python string.
   - It does not write a file by itself.

2. `save_report(result, output_dir)`
   - Creates the output folder if needed.
   - Generates the Markdown text.
   - Writes it to a `.md` file.
   - Returns the path to that file.

---

## 5. Top-level structure of the file

The file has four main pieces:

```text
Lines 1-19     Imports and file description
Lines 21-27    MatchResult dataclass
Lines 30-32    _confidence_emoji helper function
Lines 35-120   generate_report function
Lines 123-133  save_report function
```

The heart of the file is `generate_report()`.

---

## 6. Line-range walkthrough in code order

### Lines 1-9: File docstring and comments

The file begins with:

```python
"""Markdown report generator."""
```

That is the short identity of the file.

The comments explain the file in plain English:
- It takes scores from `scoring.py`.
- It turns them into a human-readable Markdown report.
- It has two main functions:
  - `generate_report()`
  - `save_report()`

This is useful because it tells you immediately that this file is not the algorithm. It is the reporting layer.

---

### Lines 11-14: Standard imports

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import pathlib
```

What each import means:

| Import | Plain-English meaning | Used? |
|---|---|---|
| `from __future__ import annotations` | Lets type hints be handled more flexibly/cleanly | Yes, harmless future-compatible typing support |
| `dataclass` | Makes simple data container classes easier to define | Yes, used for `MatchResult` |
| `Optional` | Means “this value may be a type or may be None” | Imported but not used in this file |
| `pathlib` | Modern Python library for file paths | Yes, used in `save_report()` |

Beginner note:

A `dataclass` is like a labelled container. It saves you from writing lots of repetitive class setup code.

`Optional` is currently unnecessary here and could be removed as a small cleanup.

---

### Lines 16-18: NanoGT internal imports

```python
from .disease import DiseaseInfo
from .gene import GeneInfo
from .scoring import ScoreBreakdown
```

These imports bring in the data shapes that the report expects.

| Imported object | Comes from | Meaning |
|---|---|---|
| `DiseaseInfo` | `disease.py` | The query disease metadata |
| `GeneInfo` | `gene.py` | The causal gene/protein metadata |
| `ScoreBreakdown` | `scoring.py` | One scored GT precedent match |

The leading dot in `.disease` means:

```text
Import from another file inside the same nanogt package.
```

---

## 7. `MatchResult` dataclass: lines 21-27

```python
@dataclass
class MatchResult:
    disease: DiseaseInfo
    gene: GeneInfo
    scores: list[ScoreBreakdown]
    top_n: int = 5
```

`MatchResult` bundles all the information needed to make a report.

Think of it as a report packet.

It contains:

| Field | Meaning |
|---|---|
| `disease` | The disease being analysed |
| `gene` | The main gene for that disease |
| `scores` | The full ranked list of GT program scores from `scoring.py` |
| `top_n` | How many top non-failed matches should be shown; default is 5 |

Important beginner concept:

The report function could have accepted many separate arguments:

```python
generate_report(disease, gene, scores, top_n)
```

Instead, the code wraps them into one object:

```python
generate_report(result)
```

This makes the function call cleaner.

---

## 8. `_confidence_emoji()`: lines 30-32

```python
def _confidence_emoji(c: str) -> str:
    return {"high": "🟢", "medium": "🟡", "low": "🔴", "fail": "⛔"}.get(c, "⬜")
```

This small helper converts a confidence label into an emoji.

| Confidence | Emoji | Meaning |
|---|---|---|
| `high` | 🟢 | Strong match |
| `medium` | 🟡 | Moderate match |
| `low` | 🔴 | Weak match |
| `fail` | ⛔ | Excluded, usually because packaging failed |
| Anything else | ⬜ | Unknown/unexpected label |

The function name starts with `_`.

In Python, a leading underscore usually means:

```text
This is an internal helper, not a main public function.
```

It does not enforce privacy, but it signals intent to readers.

---

## 9. `generate_report()`: lines 35-120

`generate_report()` is the main report generation function.

```python
def generate_report(result: MatchResult) -> str:
```

It takes a `MatchResult` and returns a Markdown string.

It does not save the file. It only builds the text.

### 9.1 Lines 37-40: Extract disease, gene, and top matches

```python
d = result.disease
g = result.gene
top = [s for s in result.scores if s.confidence != "fail"][:result.top_n]
```

This does three things:

1. Stores the disease object in a short variable `d`.
2. Stores the gene object in a short variable `g`.
3. Builds `top`, which means:
   - Take all scores.
   - Remove any score where `confidence == "fail"`.
   - Keep only the first `top_n` matches.

The list `result.scores` is expected to already be ranked by `scoring.py` / `rank_programs()`.

Important assumption:

```text
report.py assumes the scores list is already sorted correctly.
```

It does not sort the scores itself.

---

### 9.2 Lines 42-59: Start the Markdown report header and summary table

The code creates a list called `lines`:

```python
lines = [
    f"# NanoGT Match Report: {d.name}",
    ...
]
```

Each item in `lines` is one line of Markdown text.

Why use a list?

Because it is easier and cleaner to build a long report line by line, then join everything at the end.

The header includes:

| Report field | Comes from |
|---|---|
| Disease name | `d.name` |
| Orphanet ID | `d.orphanet_id` |
| Primary gene | `g.symbol` |
| Gene CDS length | `g.cds_length_bp` |
| Inheritance | `d.inheritance` |
| Target tissues | `d.affected_tissues` |

Beginner note:

The `f` before strings means “formatted string”. It lets Python insert variables inside `{}`.

Example:

```python
f"**Disease:** {d.name}"
```

If `d.name` is `Fabry disease`, the output becomes:

```text
**Disease:** Fabry disease
```

---

### 9.3 Missing data handling in the header

These lines show how missing values are handled:

```python
{g.cds_length_bp or 'unknown'}
{', '.join(d.inheritance) if d.inheritance else 'unknown'}
{', '.join(d.affected_tissues) if d.affected_tissues else 'unknown'}
```

Plain English:
- If the gene CDS length is missing, write `unknown`.
- If inheritance is missing, write `unknown`.
- If affected tissues are missing, write `unknown`.

This is beginner-friendly because the report does not crash just because some data is missing.

But scientifically, missing data is important. A more research-grade report might clearly flag missing data as a confidence limitation.

---

### 9.4 Lines 55-59: Markdown summary table setup

The summary table begins with:

```markdown
| Rank | Program | Vector | Score | Confidence | Approval |
|------|---------|--------|-------|-----------|----------|
```

This table gives a quick overview of the top matches.

It includes:
- Rank.
- Program name.
- Vector.
- Composite score out of 10.
- Confidence label and emoji.
- Approval status.

This is the “executive summary” of the report.

---

### 9.5 Lines 60-64: Fill the summary table

```python
for i, s in enumerate(top, 1):
    lines.append(...)
```

This loop goes through each top scored result.

`enumerate(top, 1)` means:
- Give each item a number.
- Start counting at 1, not 0.

So the first result is rank 1, the second result is rank 2, etc.

Each table row includes:

```text
rank | program name | vector | score/10 | confidence | approval status
```

The score is formatted with one decimal place:

```python
{s.composite_score:.1f}/10
```

So a score like `7.533` would display as:

```text
7.5/10
```

---

### Lines 66-67: Add a section divider

```python
lines += ["", "---", ""]
```

This adds:
- A blank line.
- A Markdown horizontal rule.
- Another blank line.

It separates the summary table from the detailed match breakdown.

---

## 10. Per-match detailed breakdown: lines 68-101

This section creates one detailed report section for each top match.

```python
for i, s in enumerate(top, 1):
```

For every top match, the report writes:
- Match number.
- Program name.
- Precedent disease.
- Vector.
- Tissue target.
- Composite score.
- A score breakdown table.
- Rationale notes.

---

### 10.1 Lines 70-77: Match heading and metadata

Example output:

```markdown
## Match #1: Zolgensma

**Precedent disease:** Spinal Muscular Atrophy  
**Vector:** AAV9  
**Tissue target:** CNS/motor neuron  
**Composite score:** 7.8 / 10
```

This tells the reader which previous gene therapy program is being used as a precedent.

Important distinction:

```text
Disease in the header = the query disease
Precedent disease = disease treated by the existing GT program
```

That distinction matters scientifically.

NanoGT is not saying the query disease is the same disease. It is saying the program may be a useful precedent.

---

### 10.2 Lines 78-94: Score breakdown table

This is the most important table in the report.

It shows every scoring dimension from `scoring.py`.

| Dimension | Max | Plain-English meaning |
|---|---:|---|
| Packaging fit | 2.0 | Does the query gene fit inside this vector? |
| Tissue tropism | 2.0 | Does the vector/predecessor target the disease tissue? |
| Protein class | 2.0 | Is the query protein similar in location/type to the precedent protein? |
| Pathway similarity | 2.0 | Is the disease biology/pathway similar? |
| Modality compatibility | 2.0 | Does source-linked disease mechanism support gene addition? |
| Inheritance compatibility | 1.0 | Is the inheritance pattern suitable for gene replacement in a similar way? |
| Approval precedent | 1.0 | Is the program approved or clinically advanced? |
| Immunogenicity | 2.0 | Are many patients likely to have antibodies against this vector? |
| Therapeutic window | 2.0 | Is there time to treat before irreversible damage? |
| Cross-correction | 1.0 | Can corrected cells help nearby uncorrected cells? |
| Immune privilege | 1.0 | Is the target tissue partly protected from immune attack? |
| Promoter availability | 1.0 | Are validated tissue-specific promoters available? |
| Route of administration | 1.0 | Is there a practical delivery route to the target tissue? |

Total raw maximum is 20.0.

The report labels the final score as:

```text
TOTAL (normalised) = Raw sum / 20 × 10
```

This matches `scoring.py`.

---

### 10.3 Why the report has both score and rationale

A numeric score alone can be misleading.

For example:

```text
Tissue tropism = 1.0
```

is less useful than:

```text
Tissue tropism = 1.0 because vector tropism overlaps CNS, but precedent target is liver.
```

That is why `report.py` includes the `notes` generated by `scoring.py`.

The score table gives the numbers.
The rationale section explains the numbers.

---

### 10.4 Lines 96-101: Rationale notes

```python
for note in s.notes:
    lines.append(f"- {note}")
```

Each `ScoreBreakdown` has a list of notes.

Those notes come from the scoring functions in `scoring.py`.

Examples of note types:
- Gene size/cargo capacity explanation.
- Tissue overlap explanation.
- Protein class match or mismatch.
- Inheritance match or mismatch.
- Pathway match or mismatch.
- Approval status.
- Immunogenicity estimate.
- Therapeutic window estimate.
- Cross-correction explanation.
- Immune privilege explanation.
- Promoter availability explanation.
- Route of administration explanation.

This section is essential for scientific interpretation because it shows why the software gave the score.

---

## 11. Packaging failures: lines 103-118

Some programs are excluded because the query gene is too large for the vector cargo limit.

This is handled separately at the bottom of the report.

```python
fails = [s for s in result.scores if s.confidence == "fail"]
```

This collects every score marked as `fail`.

If there are failures, the report adds:

```markdown
## Excluded Programs (Packaging Failure)
```

Then it shows a table with:
- Program.
- Vector.
- Gene CDS issue.

Important scientific concept:

Packaging failure is a hard physical constraint.

If the gene is larger than the vector can carry, the program is not merely a weak match. It is infeasible for that vector without redesign.

Possible redesigns might include:
- Dual AAV systems.
- Mini/microgene constructs.
- Lentiviral delivery.
- Non-viral delivery.
- Gene editing rather than full gene replacement.

But this file does not explore those options. It simply reports the failure.

---

### Line 115: Only first 5 failures are shown

```python
for s in fails[:5]:
```

The report shows up to 5 failed programs.

This keeps the report from becoming too long.

Limitation:

If many programs fail packaging, only the first 5 are visible. A more transparent report might state:

```text
Showing 5 of 12 packaging failures
```

Currently, it does not show that count.

---

## 12. Final string assembly: line 120

```python
return "\n".join(lines)
```

This joins all the individual lines into one large Markdown text block.

Beginner explanation:

Before line 120, the report is stored as a list:

```python
["line 1", "line 2", "line 3"]
```

After line 120, it becomes one text document:

```text
line 1
line 2
line 3
```

The `\n` means newline.

---

## 13. `save_report()`: lines 123-133

```python
def save_report(result: MatchResult, output_dir: pathlib.Path) -> pathlib.Path:
```

This function writes the generated Markdown report to disk.

It returns the file path.

---

### Lines 125: Create output directory

```python
output_dir.mkdir(parents=True, exist_ok=True)
```

Plain English:

```text
Create the output folder if it does not already exist.
```

The arguments mean:

| Argument | Meaning |
|---|---|
| `parents=True` | Also create missing parent folders |
| `exist_ok=True` | Do not crash if the folder already exists |

---

### Lines 127-130: Build the report filename

```python
slug = result.disease.orphanet_id.replace("ORPHA:", "ORPHA")
path = output_dir / f"match_{slug}_{result.disease.name.lower().replace(' ', '_')[:30]}.md"
```

This creates a safe-ish filename based on the disease.

Example:

```text
ORPHA:324
```

becomes:

```text
ORPHA324
```

A disease name like:

```text
Fabry Disease
```

becomes:

```text
fabry_disease
```

The disease name is truncated to 30 characters so filenames do not become too long.

Example output filename:

```text
match_ORPHA324_fabry_disease.md
```

Limitation:

The code only replaces spaces with underscores. It does not remove all punctuation or special filename characters.

---

### Lines 132-133: Write and return the file path

```python
path.write_text(generate_report(result))
return path
```

This does two things:

1. Calls `generate_report(result)` to create the Markdown text.
2. Writes that text into the file path.

Then it returns the path, so the CLI can tell the user where the report was saved.

---

## 14. Report generation in one flow

Here is the full flow inside `report.py`:

```text
MatchResult comes in
    ↓
Pull out disease and gene
    ↓
Filter out packaging failures
    ↓
Keep top N matches
    ↓
Create Markdown header
    ↓
Create top-match summary table
    ↓
Create detailed score table for each top match
    ↓
Add rationale notes for each match
    ↓
Add packaging-failure table if needed
    ↓
Join all lines into one Markdown string
    ↓
Optionally save the string to a .md file
```

---

## 15. What this file assumes

### 15.1 Scores are already ranked

`report.py` takes the first `top_n` non-failed scores.

It assumes `result.scores` is already sorted from best to worst.

If an unsorted list is passed in, the report will show the wrong top matches.

Improvement:
Add sorting inside `generate_report()` or document that `MatchResult.scores` must be pre-ranked.

---

### 15.2 `confidence == "fail"` means packaging failure

The report labels all failed scores as packaging failures.

This matches the current `scoring.py`, where hard fail happens when the gene CDS exceeds vector cargo.

But if future scoring adds other fail types, the report would need to distinguish them.

Improvement:
Add a structured failure reason field, such as:

```python
failure_reason: str | None
```

---

### 15.3 All fields are present

The report expects each `ScoreBreakdown` to have fields like:
- `program_name`
- `vector`
- `composite_score`
- `packaging_fit`
- `tropism_match`
- etc.

If `ScoreBreakdown` changes in `scoring.py`, this report may need updating too.

---

### 15.4 Markdown is the desired output format

This file writes Markdown only.

It does not create:
- PDF.
- HTML.
- Word document.
- CSV.
- JSON.

That is fine for a simple research tool, but a future version may need multiple export formats.

---

## 16. Weaknesses and limitations

### 16.1 No citations in the report

The report explains scores but does not cite evidence.

Example:
- Immunogenicity notes mention approximate seroprevalence.
- Promoter availability notes mention specific promoters.
- Route feasibility notes mention clinical precedent.

Those claims are useful, but the report does not provide formal citations.

Improvement:
Include source/citation fields from the catalog and scoring evidence layer.

---

### 16.2 No date/version metadata

The report does not state:
- NanoGT version.
- Catalog version.
- Scoring model version.
- Date generated.
- Data sources used.

For dissertation or reproducibility work, this is important.

Improvement:
Add a metadata block near the top:

```markdown
Generated: 2026-06-03
NanoGT version: ...
Catalog version: ...
Scoring model: 13-dimension v2
```

---

### 16.3 Packaging failures are truncated

Only up to 5 failures are shown.

Improvement:
Show the total number of failures and optionally write a full appendix.

---

### 16.4 No explanation of confidence thresholds

The summary table displays high/medium/low confidence, but the report does not explain:

```text
high = composite >= 7.5
medium = composite >= 5.0
low = composite < 5.0
```

Improvement:
Add a small legend after the summary table.

---

### 16.5 Missing data is shown as `unknown`, not discussed

The report shows missing values as `unknown`, but it does not explain how missing data affects confidence.

Improvement:
Add a “Missing data caveats” section if CDS, inheritance, or tissue data is absent.

---

### 16.6 Filename sanitisation is basic

The filename replaces spaces with underscores and truncates the disease name.

It may not handle all punctuation or unusual characters.

Improvement:
Use a robust slugify function.

---

## 17. Improvements that would make this report more research-grade

Recommended future improvements:

1. Add report metadata:
   - Date generated.
   - NanoGT version.
   - Catalog version.
   - Scoring model version.

2. Add confidence legend:
   - High, medium, low, fail thresholds.

3. Add citations:
   - Program sources.
   - Vector sources.
   - Seroprevalence sources.
   - Promoter/route evidence sources.

4. Add missing-data warnings:
   - Unknown CDS.
   - Unknown inheritance.
   - Unknown tissue target.

5. Add a methods section:
   - Explain raw score max = 18.
   - Explain normalisation to 10.
   - Explain each dimension.

6. Add appendix options:
   - Full ranked list.
   - Full packaging-failure list.
   - Raw JSON/CSV export.

7. Make filenames safer:
   - Remove punctuation.
   - Collapse repeated underscores.
   - Include stable disease ID.

8. Add tests for report output:
   - Header appears.
   - Tables appear.
   - Failures appear only when expected.
   - Top N filtering works.

---

## 18. Things to memorise

Core memory anchors:

1. `report.py` is the Markdown report generator.
2. It receives a `MatchResult` object.
3. `MatchResult` contains disease, gene, scores, and `top_n`.
4. `generate_report()` builds text but does not save it.
5. `save_report()` writes the generated text to disk.
6. Failed programs are excluded from the top table.
7. Failed programs are shown separately as packaging failures.
8. The report displays all 12 scoring dimensions from `scoring.py`.
9. The rationale notes come from the scoring functions.
10. The report is only as accurate as the disease/gene/scoring data it receives.

Short explanation to practise from memory:

`report.py` takes NanoGT's ranked scoring results and formats them into a Markdown report. It shows the query disease and gene, lists the top non-failed gene therapy precedent matches, displays a score breakdown for each match, includes the scoring rationale notes, and records packaging failures at the bottom. It is a formatting/reporting layer, not the scoring algorithm itself.

---

## 19. Final mini mental model

```text
DiseaseInfo + GeneInfo + ranked ScoreBreakdown list
              ↓
          MatchResult
              ↓
        generate_report()
              ↓
        Markdown text string
              ↓
          save_report()
              ↓
        .md report file
```

Simplest version:

```text
report.py turns scored matches into a readable Markdown report.
```

---

## 20. Active recall questions

Use these without looking at the code.

1. What is the main purpose of `report.py`?
2. Does `report.py` calculate scores itself?
3. What object does `generate_report()` receive?
4. What fields are stored in `MatchResult`?
5. What does `top_n` control?
6. Why does the code filter out `confidence == "fail"` before showing top matches?
7. Where are packaging failures shown?
8. What does `_confidence_emoji()` do?
9. What are the four possible confidence emojis?
10. What information appears in the report header?
11. What appears in the top matches summary table?
12. What appears in each detailed match section?
13. Why are rationale notes important?
14. Where do the rationale notes come from?
15. What does `"\n".join(lines)` do?
16. What is the difference between `generate_report()` and `save_report()`?
17. How is the output filename created?
18. What assumptions does `report.py` make about `result.scores`?
19. What metadata is missing from the current report?
20. How would you improve this report for dissertation/research-grade use?

---

## 21. Mini self-test

Close the code and try to say this out loud:

> `report.py` is NanoGT's Markdown report writer. It takes a `MatchResult`, which contains the query disease, gene, ranked scoring results, and the number of top matches to show. `generate_report()` builds the Markdown text with a header, summary table, detailed score breakdowns, rationale notes, and packaging failures. `save_report()` writes that text to a `.md` file. The file formats results; it does not decide the scores.

If you can say that from memory, you understand this file.
