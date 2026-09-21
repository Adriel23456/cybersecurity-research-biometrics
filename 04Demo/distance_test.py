from deepface import DeepFace

# We use ArcFace: the same model studied in several of our sources
MODEL = "ArcFace"

def compare(img1, img2, label):
    result = DeepFace.verify(
        img1_path=img1,
        img2_path=img2,
        model_name=MODEL,
    )
    print(f"-------- {label} --------")
    print("Distance:", round(result["distance"], 4))
    print("Default threshold:", result["threshold"])
    print("Same person?:", result["verified"])
    print()

# Case 1: same person (two photos of Henry)
compare("faces/henry_1.jpg", "faces/henry_2.jpg", "SAME PERSON")

# Case 2: different people (Henry vs brother)
compare("faces/henry_1.jpg", "faces/brother_1.jpg", "DIFFERENT PEOPLE")