from tqdm import tqdm

# for i in tqdm(range(10000000)):
#     pass

# list1 = ["java","c","cpp"]
# list2 = ["c"]
# list1.extend(list2)
# print(set(list1))


skills_str = ["java,c,cpp,python"]
exist_skills = "".split(",")
exist_skills.extend(skills_str)
updated_skills = set(exist_skills)
print(updated_skills)
