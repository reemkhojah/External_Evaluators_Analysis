# External_Evaluators_Analysis
This repository provides a transparent, reproducible Python workflow for analyzing aggregated, de-identified external evaluator data used to assess professional and engineering design skills in undergraduate bioengineering capstone projects. The analysis is designed to support longitudinal program evaluation, continuous improvement, and dissemination aligned with FAIR data principles.

Overview

The code analyzes evaluator ratings collected annually using an ordered four-level proficiency scale:

Novice

Intermediate

Proficient

Expert

Ratings are stored as aggregated proportions per skill and year, ensuring that no individual student or evaluator data are retained. The script generates three complementary visualizations that together characterize skill performance, structure, and change over time.

Data Structure

The dataset is defined as a Python dictionary keyed by year. For each year, skills are mapped to a four-element tuple representing the proportion of responses at each proficiency level in the order:

(Novice, Intermediate, Proficient, Expert)


All values are normalized to sum to one per skill. This structure supports replication while preserving anonymity and institutional confidentiality.

Analysis Outputs

Running the script produces the following figures sequentially:

Clustered and Ranked Skill Heatmap (Figure 1)

Uses hierarchical clustering (average linkage, Euclidean distance) to group skills based on similarity in proficiency distributions for a selected year.

Skills are further ranked by their mean weighted proficiency score, placing higher-performing skills at the top.

This visualization highlights structural relationships among skills and relative performance patterns.

Radar Plot of Lowest-Performing Skills (Figure 2)

Tracks a subset of lower-performing skill indicators across multiple years.

Weighted proficiency scores are plotted on a polar axis to visualize stability, improvement, or divergence over time.

Grayscale encoding distinguishes years while emphasizing longitudinal trends rather than absolute magnitude.

Ranked Slope of Skill Change (Figure 3)

Computes linear slopes for each skill using weighted scores across years.

Skills are ranked by slope magnitude, with positive slopes indicating improvement and negative slopes indicating decline.

This figure provides a compact summary of longitudinal change across all evaluated skills.

Methods Summary

Weighted scoring converts proficiency distributions into continuous values using ordinal weights (1–4).

Hierarchical clustering identifies similarities in evaluator response patterns across skills.

Linear regression (polyfit) estimates the direction and magnitude of skill change over time.

All computations rely on standard scientific Python libraries.

Requirements

Python 3.8 or later

NumPy

Matplotlib

SciPy

All dependencies are widely available and require no specialized configuration.

Running the Code

Clone the repository and run the script in a Python environment with the required libraries installed:

python analysis.py


The script executes end-to-end without additional inputs and generates all figures automatically.

Reuse and Adaptation

Users may adapt this workflow by:

Replacing the example dataset with their own aggregated evaluator data

Selecting a different year for clustering

Modifying the set of skills included in the radar plot

Extending the analysis to additional years

The structure is intentionally modular to support cross-institutional replication and comparative studies.

Intended Use

This repository is intended for:

Engineering education research

Program-level assessment and continuous improvement

ABET-aligned documentation

Open, reproducible educational analytics

License

This repository is provided for academic and educational use. Users are encouraged to cite the associated publication when applying or adapting this workflow.
