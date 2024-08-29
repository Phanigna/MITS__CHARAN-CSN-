def jaccard_coefficient(set1, set2):
    # Calculate the intersection and union of two sets
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    # Calculate the Jaccard Coefficient
    jaccard = intersection / union
    return jaccard


# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Compute Jaccard Coefficient
result = jaccard_coefficient(set1, set2)
print(f"Jaccard Coefficient: {result:.4f}")