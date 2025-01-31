import sys
import os

def extract_logs(date):
    output_file = os.path.join(OUTPUT_DIR, f"output_{date}.txt")
    
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as log_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in log_file:
            if line.startswith(date):
                out_file.write(line)
    
    print(f"Logs for {date} saved in {output_file}")

if __name__ == "__main__":
    LOG_FILE = "C:\\Users\\SHIVAM\\Downloads\\logs_2024.log\\logs_2024.log"
    OUTPUT_DIR = "C:\\Users\\SHIVAM\\Downloads\\logs_2024.log"
    date_arg = sys.argv[1] 
    extract_logs(date_arg)
else:
    print("Error: No date argument provided. Usage: python script.py YYYY-MM-DD")

# i used a simple yet effective approach i just traveled from start for the file to end extracting all the logs of that particular date and 
# appended them in the ouput file and printed it , its simple yet effective
