def prerequisite_courses(courses, prereqs):
    for i in courses:
        if i not in prereqs:
            prereqs[i] = []

    order = []
    visited = set()
    path = set()
    
    def dfs(course):
        if course in visited or path: # already visited course
            return 
        
        visited.add(course)
        path.add(course)

        # visit all prereqs before adding curr course to order[]
        for i in prereqs[course]:
            dfs(i)
        
        order.append(course)
        path.remove(course)
        
    for i in courses:
        dfs(i)

    print(order)
    return order


if __name__ == "__main__":

    prerequisite_courses(["Intro to Programming", "Data Structures", 
                        "Advanced Algorithms", "Operating Systems", "Databases"], 
                        { "Data Structures": ["Intro to Programming"], 
                        "Advanced Algorithms": ["Data Structures"], 
                        "Operating Systems": ["Advanced Algorithms"], 
                        "Databases": ["Advanced Algorithms"] })
    # Output: ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']

    prerequisite_courses(["Intro to Writing", "Contemporary Literature", 
                        "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], 
                        { "Contemporary Literature": ["Intro to Writing"], 
                        "Ancient Literature": ["Intro to Writing"], 
                        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], 
                        "Plays & Screenplays": ["Intro to Writing"] })
    # Output: ['Intro to Writing', 'Contemporary Literature', 'Ancient Literature', 'Comparative Literature', 'Plays & Screenplays']
