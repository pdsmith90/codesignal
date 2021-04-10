def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents).issubset(scholarships) and set(scholarships).issubset(allStudents) and not set(scholarships) == set(allStudents)
