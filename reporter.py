def report_sum(analyzer):
        print("Scan Summary:")
        print("--------------\n")
      
        # Baseline
        print("Total Lines: ",analyzer.LINE_Count)
        print("Long Lines (>79 Characters): ",analyzer.LONG_Lines)

        # Function, Classes & Scope
        print("DEF_Count: " ,analyzer.DEF_Count)
        print("CLASS_Count: " ,analyzer.CLASS_Count)

        # Imports & Control Flow
        print("IMPORT: " ,analyzer.IMPORT_Count)
        print("EXCEPT: " ,analyzer.EXCEPT_Count)
        print("TRY: " ,analyzer.TRY_Count)
        print("COMMENT: " ,analyzer.COMMENT_Count)
        print("FOR LOOP: " ,analyzer.F_LOOP_Count)
        print("WHILE LOOP: " ,analyzer.W_LOOP_Count)

        # Branching & Decision Logic
        print("IF: " ,analyzer.IF_Count)
        print("ELSE: " ,analyzer.ELSE_Count)
        print("ELIF: " ,analyzer.ELIF_Count)

        # Execution Jumps & Loop Control
        print("RETURN: " ,analyzer.RETURN_Count)
        print("BREAK: " ,analyzer.BREAK_Count)
        print("CONTINUE: " ,analyzer.CONTINUE_Count)
        print("PASS: " ,analyzer.PASS_Count)

        # Operations & Expressions
        print("PRINT: " ,analyzer.PRINT_Count)
        print("INCREMENT: " ,analyzer.INCREM_Count)
        print("GLOBAL: " ,analyzer.GLOBAL_Count)

        # Error Handling, Signals & Assertions
        print("RAISE: " ,analyzer.RAISE_Count)
        print("ASSERT: " ,analyzer.ASSERT_Count)

