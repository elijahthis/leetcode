from typing import List
from collections import deque

def deferred_acceptance(n: int, doctors: List[str], hospitals: List[str], doctorPreferences: List[List[str]], hospitalPreferences: List[List[str]]):
    # Gale–Shapley Deferred Acceptance algorithm
    # for the stable-matching problem (doctor-optimal)
    # Time: O(n^2)
    # Space: O(n^2)
    # Assumes equal number of doctors and hospitals
    # Assumes every preference list is complete, with no duplicates

    if len(doctors) != len(hospitals) or len(hospitals) != n:
        return {}

    unmatched_doctors = deque(doctors)

    doc_preference_hashMap = {}
    hospital_doc_rank = {}
    res = {}    # h -> doc

    for h_idx in range(len(hospitalPreferences)):
        obj = {}
        for i, d in enumerate(hospitalPreferences[h_idx]):
            obj[d]= i+1
        hospital_doc_rank[hospitals[h_idx]] = obj
    for d_idx in range(len(doctorPreferences)):
        doc_preference_hashMap[doctors[d_idx]] = deque(doctorPreferences[d_idx])

    print(hospital_doc_rank)

    while len(unmatched_doctors) > 0:
        curr_doctor = unmatched_doctors.popleft()
        top_hospital = doc_preference_hashMap[curr_doctor].popleft()
        if top_hospital not in res:     # hospital is unmatched
            # match them
            res[top_hospital] = curr_doctor
        else:
            matched_doctor = res[top_hospital]
            if hospital_doc_rank[top_hospital][curr_doctor] < hospital_doc_rank[top_hospital][matched_doctor]:  # curr_doctor is preferred
                unmatched_doctors.append(matched_doctor)
                res[top_hospital] = curr_doctor
            else:
                unmatched_doctors.append(curr_doctor)

    return res

doctors = ["A", "B", "C", "D", "E"]
hospitals = ["L", "M", "N", "O", "P"]
doctorPreferences = [
    ["O", "M", "N", "L", "P"],
    ["P", "N", "M", "L", "O"],
    ["M", "P", "L", "O", "N"],
    ["P", "M", "O", "N", "L"],
    ["O", "L", "M", "N", "P"],
]
hospitalPreferences = [
    ["D", "B", "E", "C", "A"],
    ["B", "A", "D", "C", "E"],
    ["A", "C", "E", "D", "B"],
    ["D", "A", "C", "B", "E"],
    ["B", "E", "A", "C", "D"],
]

print(deferred_acceptance(5, doctors, hospitals, doctorPreferences, hospitalPreferences, ))

