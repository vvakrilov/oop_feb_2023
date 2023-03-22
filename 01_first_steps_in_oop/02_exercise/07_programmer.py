class Programmer:
    def __init__(self, name: str, language: str, skills: int, ):
        self.name = name
        self.language = language
        self.skills = skills

    @staticmethod
    def are_skills(got, need):
        return got >= need

    @staticmethod
    def is_lang_equal(current, new):
        return current == new

    def watch_course(self, course_name, language, skills_earned):
        if self.is_lang_equal(self.language, language):
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.are_skills(self.skills, skills_needed):
            if self.is_lang_equal(self.language, new_language):
                return f"{self.name} already knows {self.language}"
            else:
                previous_language = self.language
                self.language = new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
        else:
            return f"{self.name} needs {abs(self.skills - skills_needed)} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
