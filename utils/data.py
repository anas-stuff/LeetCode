class Data:
    def __init__(self, title: str, level: str, problem_path: str, solve_with: list = None):
        self.title = title
        self.level = level
        self.problem_path = problem_path
        self.solve_with = solve_with
    
    def __str__(self) -> str:
        return f"Title: {self.title} | Level: {self.level} | Path: {self.problem_path} | Solve with: {self.solve_with}"