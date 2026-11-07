from pathlib import Path
from analyzer import SCAnalyzer
from reporter import report_sum

def main():

    while True:
        fileName = input("Enter the file name: ")
        fileCheck = Path(fileName)

        if fileCheck.is_file():
            print("Successfully opened file:")

            analyzer = SCAnalyzer(fileName)
            analyzer.token_analyzer()
            report_sum(analyzer)
            break
          
        else: 
            print("Error: File does not exist, please try again.")
             
           

if __name__ == "__main__":
    main()
