from pathlib import Path

class SCAnalyzer:

    def __init__(self, fileName):
        # Baseline
        self.LINE_Count = 0
        self.LONG_Lines = 0
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

    def token_analyzer(self):
        with open(self.fileName, "r") as file:

            for line in file:
                if len(line.rstrip("\r\n")) > 90:
                    self.LONG_Lines += 1

            
                clean = line.strip()
                tokens = clean.split()
                

                if not tokens:
                    continue

                if "#" in line:
                    parts = line.split("#")
                    cumulative = ""
                    for i in range(len(parts) - 1):
                        cumulative += parts[i]
                        if cumulative.count('"') % 2 == 0 and cumulative.count("'") % 2 == 0:
                            self.COMMENT_Count += 1
                            break



                        in_quotes = False
                        quote_char = None
                        
                        for char in line:
                          if char in ('"', "'"):
                             if not in_quotes:
                                in_quotes = True
                                quote_char = char
                             elif char == quote_char:
                                in_quotes = False
                                quote_char = None
                        
                          elif char == "#" and not in_quotes:
                            self.COMMENT_Count += 1
                            break

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


    