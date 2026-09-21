from deepface import DeepFace

# ArcFace: the same model studied in several of our sources
MODEL = "ArcFace"

# The two comparisons we already validated
PAIRS = [
    ("faces/henry_1.jpg", "faces/henry_2.jpg", "Henry vs Henry (same person)"),
    ("faces/henry_1.jpg", "faces/brother_1.jpg", "Henry vs brother (different)"),
]

# Thresholds we want to test the decision at
THRESHOLDS = [0.30, 0.50, 0.68, 0.90]


def get_distance(img1, img2):
    result = DeepFace.verify(
        img1_path=img1,
        img2_path=img2,
        model_name=MODEL,
    )
    return result["distance"]


print("Computing distances with ArcFace...\n")

# First, compute each pair's distance once
distances = []
for img1, img2, label in PAIRS:
    d = get_distance(img1, img2)
    distances.append((label, d))

# Now show the decision at each threshold
print("=" * 70)
print(f"{'Comparison':<32}{'Distance':<12}{'Threshold':<12}{'Match?'}")
print("=" * 70)

for label, d in distances:
    for t in THRESHOLDS:
        match = "YES" if d < t else "NO"
        print(f"{label:<32}{round(d, 4):<12}{t:<12}{match}")
    print("-" * 70)