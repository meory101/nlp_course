# Generates the LinkedIn visual for Paper A post.
# The "wrong ruler" idea: tiny per-step gains -> exponential task length.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# Neurix-style dark theme
BG     = "#030014"
PANEL  = "#0a0420"
PURPLE = "#a855f7"
PINK   = "#ec4899"
CYAN   = "#22d3ee"
TEXT   = "#f5f3ff"
MUTED  = "#9b8fc7"

plt.rcParams["font.family"] = "DejaVu Sans"

fig = plt.figure(figsize=(10.8, 10.8), dpi=100)
fig.patch.set_facecolor(BG)

# ---- title block ----
fig.text(0.5, 0.955, "THE WRONG RULER", ha="center", va="top",
         fontsize=31, fontweight="bold", color=TEXT)
fig.text(0.5, 0.90,
         "A tiny gain in per-step accuracy → an exponential jump\nin how long a task the model can actually finish.",
         ha="center", va="top", fontsize=14.5, color=MUTED, linespacing=1.5)

# ---- the curve ----
ax = fig.add_axes([0.13, 0.17, 0.78, 0.60])
ax.set_facecolor(PANEL)

p = np.linspace(0.80, 0.999, 500)          # per-step accuracy
L = np.log(0.5) / np.log(p)                # steps until P(success) drops to 50%

ax.plot(p * 100, L, color=CYAN, lw=3.5,
        path_effects=[pe.Stroke(linewidth=7, foreground=PURPLE, alpha=0.35), pe.Normal()])

ax.set_yscale("log")
ax.set_xlim(80, 100.5)
ax.set_ylim(2.5, 800)

# highlight two reference points with clean leader labels
pts = [
    (0.90, "90% per step\n≈ 10 steps", (16, -42), "left"),
    (0.99, "99% per step\n≈ 100 steps", (-150, 30), "left"),
]
for acc, label, off, ha in pts:
    steps = np.log(0.5) / np.log(acc)
    ax.scatter([acc * 100], [steps], s=170, color=PINK, zorder=6,
               edgecolor=TEXT, linewidth=1.6)
    ax.annotate(label, (acc * 100, steps),
                textcoords="offset points", xytext=off,
                fontsize=14.5, fontweight="bold", color=TEXT, ha=ha,
                linespacing=1.35, zorder=7)

ax.set_xlabel("Per-step accuracy  —  the number everyone reports", fontsize=13, color=MUTED, labelpad=12)
ax.set_ylabel("Task length the model can finish", fontsize=13, color=MUTED, labelpad=12)
ax.tick_params(colors=MUTED, labelsize=11)
for s in ax.spines.values():
    s.set_color("#2a1b4d")
ax.grid(True, which="both", color="#1a1033", lw=0.8, alpha=0.7)

# --- the "+9%" callout, parked in clear space top-left of the panel ---
box = dict(boxstyle="round,pad=0.55", fc="#1a0b33", ec=PINK, lw=1.6, alpha=0.95)
ax.text(81.2, 230,
        "+9% on paper.\n10× longer in reality.",
        fontsize=15, color=PINK, fontweight="bold", linespacing=1.45,
        va="center", ha="left", bbox=box, zorder=8)

# ---- footer line ----
fig.text(0.5, 0.072,
         "The gains aren't diminishing — they're hiding behind a ruler that's too short.",
         ha="center", fontsize=14.5, color=TEXT, style="italic")
fig.text(0.5, 0.033, "Paper:  The Illusion of Diminishing Returns   ·   arXiv 2509.09677",
         ha="center", fontsize=11, color=MUTED)

# subtle brand mark, bottom-right corner
fig.text(0.965, 0.018, "● neurix", ha="right", va="bottom",
         fontsize=10.5, color=CYAN, alpha=0.55, fontweight="bold")

fig.savefig("linkedin_post_paper_A_image.png", facecolor=BG, bbox_inches="tight", pad_inches=0.3)
print("saved linkedin_post_paper_A_image.png")
