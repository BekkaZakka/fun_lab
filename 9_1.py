# def calculate_years_of_experience(resume):
#
#     total_experience = 0
#     for experience in resume['work_history']:
#         start_date = experience['start_date']
#         end_date = experience['end_date']
#         start_year, start_month, start_day = map(int, start_date.split('-'))
#         end_year, end_month, end_day = map(int, end_date.split('-'))
#         total_experience += (end_year - start_year) + (end_month - start_month) / 12 + (end_day - start_day) / 365
#     return round(total_experience, 2)
#
#
# my_resume = {
#     'name': 'Kosherbaev Abylai',
#     'email': 'qwerty@gmail.com',
#     'education': 'Computer Science',
#     'skills': ['Python', 'Java', 'C++', 'SQL', 'HTML/CSS'],
#     'work_history': [
#         {'position': 'Student', 'company': 'Satbayev', 'start_date': '2020-09-01', 'end_date': '2024-05-31'},
#         {'position': 'IT person', 'company': 'Mycar Digital', 'start_date': '2025-07-21', 'end_date': '2026-07-31'},
#         {'position': 'Teacher', 'company': 'Google', 'start_date': '2026-09-01', 'end_date': '2030-01-01'}
#     ]
# }
#
# years_of_experience = calculate_years_of_experience(my_resume)
# print("Опыт работы: " + str(years_of_experience))

# 1_2 нефункционал

def print_resume(resume):
    """
    This function prints out the resume information in a readable format.
    """
    print("Name: " + resume['name'])
    print("Email: " + resume['email'])
    print("Education: " + resume['education'])
    print("Skills: " + ", ".join(resume['skills']))
    print("Work History: ")
    for experience in resume['work_history']:
        print("- " + experience['position'] + " at " + experience['company'])

my_resume = {
    'name': 'Kosherbaev Abylai',
    'email': 'qwerty@gmail.com',
    'education': 'Computer Science',
    'skills': ['Python', 'Java', 'C++', 'SQL', 'HTML/CSS'],
    'work_history': [
        {'position': 'Student', 'company': 'Satbayev', 'year': '2020-2024'},
        {'position': 'It person', 'company': 'Mycar Digital', 'year': '2025'},
        {'position': 'Teacher', 'company': 'Google', 'year': '2026-r.n'}
    ]
}

print_resume(my_resume)