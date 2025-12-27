import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from matplotlib import gridspec

# ============================================================
# SHARED DATA
# ============================================================

data_full = {
    2022: {
        "Poster: Pleasing Visual Appearance": (0.000, 0.000, 0.250, 0.750),
        "Poster: Graphical Display": (0.000, 0.000, 0.245, 0.755),
        "Poster: Organization of Content": (0.000, 0.050, 0.150, 0.800),
        "Oral: Good Explanations": (0.000, 0.050, 0.200, 0.750),
        "Oral: Fluent Speech": (0.000, 0.050, 0.150, 0.800),
        "Oral: Respectful Behavior": (0.000, 0.000, 0.050, 0.950),
        "Eng Work: Challenging Experimentation": (0.050, 0.150, 0.350, 0.450),
        "Eng Work: Implementation": (0.100, 0.100, 0.450, 0.350),
        "Eng Work: Basic Science": (0.050, 0.100, 0.450, 0.400),
        "Eng Work: Engineering Principles": (0.050, 0.000, 0.550, 0.400),
        "Eng Work: Factual Evidence + Reference": (0.100, 0.050, 0.450, 0.400),
        "Eng Work: Limitations": (0.100, 0.200, 0.350, 0.350)
    },
    2023: {
        "Poster: Pleasing Visual Appearance": (0.000, 0.000, 0.512, 0.488),
        "Poster: Graphical Display": (0.000, 0.024, 0.317, 0.659),
        "Poster: Organization of Content": (0.000, 0.098, 0.317, 0.585),
        "Oral: Good Explanations": (0.000, 0.073, 0.317, 0.610),
        "Oral: Fluent Speech": (0.000, 0.024, 0.244, 0.732),
        "Oral: Respectful Behavior": (0.000, 0.000, 0.146, 0.854),
        "Eng Work: Challenging Experimentation": (0.024, 0.220, 0.415, 0.341),
        "Eng Work: Implementation": (0.024, 0.098, 0.463, 0.415),
        "Eng Work: Basic Science": (0.000, 0.122, 0.463, 0.415),
        "Eng Work: Engineering Principles": (0.049, 0.098, 0.415, 0.439),
        "Eng Work: Factual Evidence + Reference": (0.024, 0.146, 0.390, 0.439),
        "Eng Work: Limitations": (0.049, 0.171, 0.488, 0.293)
    },
    2024: {
        "Poster: Pleasing Visual Appearance": (0.00, 0.13, 0.17, 0.69),
        "Poster: Graphical Display": (0.00, 0.12, 0.27, 0.62),
        "Poster: Organization of Content": (0.00, 0.19, 0.21, 0.60),
        "Oral: Good Explanations": (0.00, 0.10, 0.23, 0.67),
        "Oral: Fluent Speech": (0.00, 0.08, 0.21, 0.71),
        "Oral: Respectful Behavior": (0.02, 0.02, 0.17, 0.79),
        "Eng Work: Challenging Experimentation": (0.04, 0.13, 0.21, 0.62),
        "Eng Work: Implementation": (0.02, 0.23, 0.17, 0.58),
        "Eng Work: Basic Science": (0.04, 0.19, 0.23, 0.54),
        "Eng Work: Engineering Principles": (0.04, 0.19, 0.29, 0.48),
        "Eng Work: Factual Evidence + Reference": (0.04, 0.15, 0.23, 0.58),
        "Eng Work: Limitations": (0.08, 0.21, 0.29, 0.42)
    },
    2025: {
        "Poster: Pleasing Visual Appearance": (0.00, 0.04, 0.33, 0.63),
        "Poster: Graphical Display": (0.00, 0.08, 0.19, 0.73),
        "Poster: Organization of Content": (0.00, 0.04, 0.37, 0.60),
        "Oral: Good Explanations": (0.02, 0.06, 0.27, 0.65),
        "Oral: Fluent Speech": (0.00, 0.04, 0.10, 0.87),
        "Oral: Respectful Behavior": (0.00, 0.02, 0.08, 0.90),
        "Eng Work: Challenging Experimentation": (0.06, 0.12, 0.48, 0.35),
        "Eng Work: Implementation": (0.02, 0.19, 0.46, 0.33),
        "Eng Work: Basic Science": (0.02, 0.27, 0.33, 0.38),
        "Eng Work: Engineering Principles": (0.02, 0.19, 0.35, 0.44),
        "Eng Work: Factual Evidence + Reference": (0.02, 0.23, 0.35, 0.40),
        "Eng Work: Limitations": (0.02, 0.15, 0.52, 0.31)
    }
}

skills = list(data_full[2025].keys())
years = np.array([2022, 2023, 2024, 2025])

# ============================================================
# SHARED FUNCTIONS
# ============================================================

def weighted_score(v):
    return v[0]*1 + v[1]*2 + v[2]*3 + v[3]*4

def build_matrix(year):
    return np.array([data_full[year][s] for s in skills])

# ============================================================
# FIGURE 1 — CLUSTERED + RANKED HEATMAP (ALL YEARS AGGREGATED)
# ============================================================

data_all = build_matrix(2025)

Z = linkage(data_all, method="average", metric="euclidean")
order = dendrogram(Z, no_plot=True)["leaves"]

data_clustered = data_all[order]
skills_clustered = [skills[i] for i in order]

mean_scores = data_clustered @ np.array([1, 2, 3, 4])
flip = np.argsort(mean_scores)[::-1]

data_final = data_clustered[flip]
skills_final = [skills_clustered[i] for i in flip]

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 4])

ax_d = plt.subplot(gs[0])
dendrogram(Z, orientation="left", labels=np.array(skills)[order])
ax_d.axis("off")

ax_h = plt.subplot(gs[1])
im = ax_h.imshow(data_final, cmap="cividis", vmin=0, vmax=1)
ax_h.set_yticks(range(len(skills_final)))
ax_h.set_yticklabels(skills_final)
ax_h.set_xticks(range(4))
ax_h.set_xticklabels(["Novice", "Intermediate", "Proficient", "Expert"])
plt.colorbar(im, ax=ax_h, label="Percentage")
plt.title("Clustered and Ranked Skill Heatmap (2025)")
plt.tight_layout()
plt.show()

# ============================================================
# FIGURE 2 — RADAR (LOWEST-PERFORMING SKILLS)
# ============================================================

low_skills = [
    "Eng Work: Limitations",
    "Eng Work: Challenging Experimentation",
    "Eng Work: Implementation",
    "Eng Work: Basic Science",
    "Eng Work: Engineering Principles"
]

angles = np.linspace(0, 2*np.pi, len(low_skills), endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(9, 9))
for y, c in zip(years, ["#E0E0E0", "#B0B0B0", "#808080", "#404040"]):
    vals = [weighted_score(data_full[y][s]) for s in low_skills]
    plt.polar(angles, vals + [vals[0]], marker="o", linewidth=2, label=str(y), color=c)

plt.xticks(angles[:-1], low_skills)
plt.ylim(2.8, 3.4)
plt.title("Radar Plot of Lowest-Performing Skills (2022–2025)")
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# FIGURE 3 — RANKED SLOPES (2022–2025)
# ============================================================

slopes = {}
for s in skills:
    vals = [weighted_score(data_full[y][s]) for y in years]
    slopes[s] = np.polyfit(years, vals, 1)[0]

items = sorted(slopes.items(), key=lambda x: x[1])
labels, vals = zip(*items)
colors = ["green" if v > 0 else "red" for v in vals]

plt.figure(figsize=(12, 7))
plt.barh(labels, vals, color=colors)
plt.axvline(0, color="black")
plt.title("Ranked Slope of Skill Change (2022–2025)")
plt.xlabel("Slope")
plt.tight_layout()
plt.show()
