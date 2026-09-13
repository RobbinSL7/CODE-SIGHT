from pathlib import Path

class SCAnalyzer:

    def __init__(self, fileName):
        # Baseline
        self.LINE_Count = 0
        self.INFO_Count = 0
        self.WARN_Count = 0
        self.ERROR_Count = 0
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
                self.LINE_Count += 1
                if "INFO" in clean:
                    self.INFO_Count += 1
                if "WARN" in clean:
                    self.WARN_Count += 1
                if "ERROR" in clean:
                    self.ERROR_Count += 1
                if clean.startswith("def ") and clean.endswith(":"):
                    self.DEF_Count += 1
                if clean.startswith("class ") and clean.endswith(":"):
                    self.CLASS_Count += 1
                if "import" in clean:
                    self.IMPORT_Count += 1
                if clean.startswith("except: ") and clean.endswith(":"):
                    self.EXCEPT_Count += 1
                if "try:" in clean:
                    self.TRY_Count += 1
                if clean.startswith("#") and clean.endswith("#"):
                    self.COMMENT_Count += 1
                if clean.startswith("for ") and clean.endswith(":"):
                    self.F_LOOP_Count += 1
                if clean.startswith("while: ") and clean.endswith(":"):
                    self.W_LOOP_Count += 1
                if clean.startswith("print(") or clean.startswith("print ("):
                    self.PRINT_Count += 1 
                if clean.startswith("if ") and clean.endswith(":"):
                    self.IF_Count += 1
                if clean.startswith("else ") and clean.endswith(":"):
                    self.ELSE_Count += 1
                if clean.startswith("elif ") and clean.endswith(":"):
                    self.ELIF_Count += 1
                if "RETURN" in clean:
                    self.RETURN_Count += 1
                if clean.startswith("break ") and clean.endswith(" "):
                    self.BREAK_Count += 1
                if clean.startswith("continue ") and clean.endswith(" "):
                    self.CONTINUE_Count += 1
                if "+=" in clean:
                    self.INCREM_Count += 1
                if clean.startswith("raise ") and clean.endswith(" "):
                    self.RAISE_Count += 1
                if clean.startswith("global") and clean.endswith(" "):
                    self.GLOBAL_Count += 1
                if clean.startswith("pass ") and clean.endswith(" "):
                    self.PASS_Count += 1
                if clean.startswith("assert") and clean.endswith(" ") or clean.endswith('"'):
                    self.ASSERT_Count += 1
                
                if self.ERROR_Count > 5:
                    print("WARNING: Too many errors in the log")
                    break


    def print_summary(self):
        print("Scan Summary:")
        print("--------------\n")
      
        # Baseline
        print("Total Lines: ",self.LINE_Count)
        print("INFO: " ,self.INFO_Count)
        print("WARN: " ,self.WARN_Count)
        print("ERROR: " ,self.ERROR_Count)

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


