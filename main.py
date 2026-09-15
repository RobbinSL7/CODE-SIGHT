from pathlib import Path

class SCAnalyzer:

    def __init__(self, fileName):
        # Baseline
        self.LINE_Count = 0
        self.reviewLines = []
        self.fileName = fileName

        # Function, Classes & Scope
        self.DEF_Count = 0
        self.CLASS_Count = 0

        # Imports & Control Flow
        self.IMPORT_Count = 0
        self.EXCEPT_Count = 0
        self.TRY_Count = 0
        self.COMMENT_Count = 0
        self.F_LOOP_Count = 0
        self.W_LOOP_Count = 0

        # Branching & Decision Logic
        self.IF_Count = 0
        self.ELSE_Count = 0
        self.ELIF_Count = 0

        # Execution Jumps & Loop Control
        self.RETURN_Count = 0
        self.BREAK_Count = 0
        self.CONTINUE_Count = 0
        self.PASS_Count = 0

        # Operations & Expressions 
        self.PRINT_Count = 0
        self.INCREM_Count = 0
        self.GLOBAL_Count = 0

        # Error Handling, Signals & Assertions
        self.RAISE_Count = 0
        self.ASSERT_Count = 0

    def analyze_logs(self):
        with open(self.fileName, "r") as file:

            for line in file:
                clean = line.strip()
                tokens = clean.split()
                self.LINE_Count += 1

                if not tokens:
                    continue

                self.LINE_Count += 1
                if tokens[0] == "def":
                    self.DEF_Count += 1
                if tokens[0] == "class":
                    self.CLASS_Count += 1
                if tokens[0] == "import":
                    self.IMPORT_Count += 1
                if tokens[0] == "except":
                    self.EXCEPT_Count += 1
                if tokens[0] == "try":
                    self.TRY_Count += 1
                if tokens[0] == "#":
                    self.COMMENT_Count += 1
                if tokens[0] == "for":
                    self.F_LOOP_Count += 1
                if tokens[0] == "while":
                    self.W_LOOP_Count += 1
                if tokens[0] == "print":
                    self.PRINT_Count += 1
                if tokens[0] == "if":
                    self.IF_Count += 1
                if tokens[0] == "else":
                    self.ELSE_Count += 1
                if tokens[0] == "elif":
                    self.ELIF_Count += 1
                if tokens[0] == "return":
                    self.RETURN_Count += 1
                if tokens[0] == "break":
                    self.BREAK_Count += 1
                if tokens[0] == "continue":
                    self.CONTINUE_Count += 1
                if "+=" in tokens:
                    self.INCREM_Count += 1
                if tokens[0] == "raise":
                    self.RAISE_Count += 1
                if tokens[0] == "global":
                    self.GLOBAL_Count += 1
                if tokens[0] == "pass":
                    self.PASS_Count += 1
                if tokens[0] == "assert":
                    self.ASSERT_Count += 1
                
                # if self.ERROR_Count > 5:
                   # print("WARNING: Too many errors in the log")
                   # break


    def print_summary(self):
        print("Scan Summary:")
        print("--------------\n")
      
        # Baseline
        print("Total Lines: ",self.LINE_Count)

        # Function, Classes & Scope
        print("DEF_Count: " ,self.DEF_Count)
        print("CLASS_Count: " ,self.CLASS_Count)

        # Imports & Control Flow
        print("IMPORT: " ,self.IMPORT_Count)
        print("EXCEPT: " ,self.EXCEPT_Count)
        print("TRY: " ,self.TRY_Count)
        print("COMMENT: " ,self.COMMENT_Count)
        print("FOR LOOP: " ,self.F_LOOP_Count)
        print("WHILE LOOP: " ,self.W_LOOP_Count)

        # Branching & Decision Logic
        print("IF: " ,self.IF_Count)
        print("ELSE: " ,self.ELSE_Count)
        print("ELIF: " ,self.ELIF_Count)

        # Execution Jumps & Loop Control
        print("RETURN: " ,self.RETURN_Count)
        print("BREAK: " ,self.BREAK_Count)
        print("CONTINUE: " ,self.CONTINUE_Count)
        print("PASS: " ,self.PASS_Count)

        # Operations & Expressions
        print("PRINT: " ,self.PRINT_Count)
        print("INCREMENT: " ,self.INCREM_Count)
        print("GLOBAL: " ,self.GLOBAL_Count)

        # Error Handling, Signals & Assertions
        print("RAISE: " ,self.RAISE_Count)
        print("ASSERT: " ,self.ASSERT_Count)


def main():

    while True:
        fileName = input("Enter the file name: ")
        fileCheck = Path(fileName)

        if fileCheck.is_file():
            print("Successfully opened file:")

            analyzer = SCAnalyzer(fileName)
            analyzer.analyze_logs()
            analyzer.print_summary()
            break
          
        else: 
            print("Error: File does not exist, please try again.")
             
           

if __name__ == "__main__":
    main()


