"""
Generate figures 1, 2, 3 for NanoGT dissertation.
Reads from output/SUMMARY.md. Saves to paper/.
"""

import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# ── Parse SUMMARY.md ──────────────────────────────────────────────────────────

SUMMARY = Path("output/SUMMARY.md")
rows = []
for line in SUMMARY.read_text().splitlines():
    if not line.startswith("| "):
        continue
    cols = [c.strip() for c in line.split("|")[1:-1]]
    if cols[0] == "Cohort role":
        continue
    if len(cols) < 11:
        continue
    rows.append({
        "cohort_role":    cols[0],
        "disease":        cols[1],
        "orpha":          cols[2],
        "gene":           cols[3],
        "mechanism":      cols[4],
        "fit":            cols[5],
        "cds":            cols[6],
        "precedent":      cols[7],
        "vector":         cols[8],
        "score_raw":      cols[9],
        "confidence":     cols[10],
    })

def parse_score(s):
    m = re.match(r"([\d.]+)/10", s)
    return float(m.group(1)) if m else None

for r in rows:
    r["score"] = parse_score(r["score_raw"])

# ── Colour scheme ─────────────────────────────────────────────────────────────

CONF_COLOR = {
    "high":                "#2d6a4f",   # dark green
    "medium":              "#f4a261",   # amber
    "packaging_hard_fail": "#e63946",   # red
}
CONF_LABEL = {
    "high":                "High confidence",
    "medium":              "Medium confidence",
    "packaging_hard_fail": "Packaging hard-fail (NF1)",
}

# ── Figure 1: Forty-disease score distribution ────────────────────────────────

fig1_rows = sorted(rows, key=lambda r: r["score"] if r["score"] is not None else -1, reverse=True)

names   = [r["disease"] for r in fig1_rows]
scores  = [r["score"]   if r["score"] is not None else 0 for r in fig1_rows]
colors  = [CONF_COLOR[r["confidence"]] for r in fig1_rows]

# Shorten long disease names for readability
short_names = []
for n in names:
    n2 = n.replace("Mucopolysaccharidosis", "MPS")
    n2 = n2.replace("Severe combined immunodeficiency due to adenosine deaminase deficiency", "ADA-SCID")
    n2 = n2.replace("Glycogen storage disease type Ia", "GSD type Ia")
    n2 = n2.replace("Leber hereditary optic neuropathy", "LHON")
    n2 = n2.replace("Leber congenital amaurosis", "LCA")
    n2 = n2.replace("X-linked myotubular myopathy", "XLMTM")
    n2 = n2.replace("X-linked adrenoleukodystrophy", "X-ALD")
    n2 = n2.replace("X-linked retinoschisis", "XLRS")
    n2 = n2.replace("Vitamin B12-unresponsive methylmalonic acidemia", "MMA (cblA/B)")
    n2 = n2.replace("Ornithine transcarbamylase deficiency", "OTC deficiency")
    n2 = n2.replace("Kohlschutter-Tonz syndrome", "KTS (ROGDI)")
    n2 = n2.replace("Fragile X syndrome", "Fragile X")
    n2 = n2.replace("Tuberous sclerosis complex", "TSC")
    n2 = n2.replace("Neurofibromatosis type 1", "NF1")
    n2 = n2.replace("Wiskott-Aldrich syndrome", "Wiskott-Aldrich")
    n2 = n2.replace("Friedreich ataxia", "FRDA")
    n2 = n2.replace("Duchenne muscular dystrophy", "DMD")
    n2 = n2.replace("Spinal Muscular Atrophy", "SMA")
    short_names.append(n2)

fig, ax = plt.subplots(figsize=(10, 12))
y = np.arange(len(short_names))
bars = ax.barh(y, scores, color=colors, edgecolor="white", linewidth=0.5, height=0.75)

ax.set_yticks(y)
ax.set_yticklabels(short_names, fontsize=8)
ax.set_xlabel("Composite NanoGT Score (/10)", fontsize=10)
ax.set_title("Figure 1: NanoGT Composite Scores — 40-Disease Cohort", fontsize=12, fontweight="bold", pad=12)
ax.set_xlim(0, 11)
ax.axvline(x=8.0, color="#999", linestyle="--", linewidth=0.8, alpha=0.7)
ax.text(8.05, len(y) - 0.5, "8.0", fontsize=7, color="#777")

# Score labels on bars
for bar, score in zip(bars, scores):
    if score > 0:
        ax.text(score + 0.1, bar.get_y() + bar.get_height()/2,
                f"{score:.1f}", va="center", fontsize=7, color="#333")

# Legend
patches = [mpatches.Patch(color=v, label=CONF_LABEL[k]) for k, v in CONF_COLOR.items()]
ax.legend(handles=patches, loc="lower right", fontsize=8)
ax.invert_yaxis()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
out1 = Path("paper/figure1_scores.pdf")
fig.savefig(out1, bbox_inches="tight", dpi=150)
plt.close(fig)
print(f"Saved {out1}")


# ── Figure 2: Top-precedent cluster map ──────────────────────────────────────

# Count diseases per precedent
precedent_counts = {}
for r in rows:
    p = r["precedent"]
    if p == "—":
        p = "NF1 (hard-fail)"
    v = r["vector"]
    key = f"{p}\n({v})" if p != "NF1 (hard-fail)" else p
    precedent_counts[key] = precedent_counts.get(key, 0) + 1

# Sort by count descending
sorted_prec = sorted(precedent_counts.items(), key=lambda x: x[1], reverse=True)
labels  = [p for p, _ in sorted_prec]
counts  = [c for _, c in sorted_prec]

# Color by vector type
VECTOR_COLOR = {
    "LV":  "#5e60ce",
    "AAV9": "#48cae4",
    "AAV5": "#0096c7",
    "AAV8": "#023e8a",
    "AAV2": "#90e0ef",
    "NF1 (hard-fail)": "#e63946",
}

def color_for_label(label):
    for vec, col in VECTOR_COLOR.items():
        if vec in label:
            return col
    return "#aaa"

bar_colors = [color_for_label(l) for l in labels]

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(labels))
ax.barh(y, counts, color=bar_colors, edgecolor="white", linewidth=0.5, height=0.7)
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=8)
ax.set_xlabel("Number of diseases", fontsize=10)
ax.set_title("Figure 2: Disease Clustering by Top Precedent Programme", fontsize=12, fontweight="bold", pad=12)
ax.set_xlim(0, max(counts) + 2)

# Count labels
for bar, count in zip(ax.patches, counts):
    ax.text(count + 0.1, bar.get_y() + bar.get_height()/2,
            str(count), va="center", fontsize=9, color="#333")

# Legend
vec_patches = [mpatches.Patch(color=col, label=f"{vec} vector") for vec, col in VECTOR_COLOR.items()
               if any(vec in l for l in labels)]
ax.legend(handles=vec_patches, loc="lower right", fontsize=8, ncol=2)
ax.invert_yaxis()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
out2 = Path("paper/figure2_radar.pdf")
fig.savefig(out2, bbox_inches="tight", dpi=150)
plt.close(fig)
print(f"Saved {out2}")


# ── Figure 3: Validation and stress-test examples ────────────────────────────

# Four panels: Hemophilia B, SMA, LCA, DMD
cases = {
    "Hemophilia B\n(positive control)":       "ORPHA:306",
    "SMA\n(positive control)":                "ORPHA:70",
    "LCA\n(calibration test)":                "ORPHA:65",
    "DMD\n(oversized cargo)":                 "ORPHA:98896",
}

# Pull top-5 precedents from individual match files
import os

def parse_match_file(orpha_id):
    """Return list of (rank, programme, vector, score) from match_ORPHA*.md."""
    orpha_num = orpha_id.replace("ORPHA:", "")
    matches = [f for f in Path("output").glob(f"match_{orpha_id.replace(':', '')}*.md")]
    if not matches:
        return []
    text = matches[0].read_text()
    results = []
    for line in text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*([\d.]+)/10", line)
        if m:
            results.append((int(m.group(1)), m.group(2), m.group(3), float(m.group(4))))
    return results[:5]

fig, axes = plt.subplots(1, 4, figsize=(14, 4), sharey=False)

for ax, (title, orpha) in zip(axes, cases.items()):
    data = parse_match_file(orpha)
    if not data:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        ax.set_title(title, fontsize=9, fontweight="bold")
        continue

    ranks, programmes, vectors, scores = zip(*data)
    # Colour top bar gold, rest grey
    bar_cols = ["#f4d03f"] + ["#adb5bd"] * (len(scores) - 1)
    y_pos = np.arange(len(programmes))

    ax.barh(y_pos, scores, color=bar_cols, edgecolor="white", linewidth=0.4)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(programmes, fontsize=7)
    ax.set_xlim(0, 10.5)
    ax.set_xlabel("Score", fontsize=8)
    ax.set_title(title, fontsize=9, fontweight="bold")
    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar, score in zip(ax.patches, scores):
        ax.text(score + 0.1, bar.get_y() + bar.get_height()/2,
                f"{score:.1f}", va="center", fontsize=7)

fig.suptitle("Figure 3: Validation Cases and Stress Tests", fontsize=12, fontweight="bold", y=1.01)
fig.tight_layout()
out3 = Path("paper/figure3_stacked.pdf")
fig.savefig(out3, bbox_inches="tight", dpi=150)
plt.close(fig)
print(f"Saved {out3}")

print("\nAll figures generated.")
