import subprocess
import glob
import os

def generate_winmerge_report(file1, file2, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
       # os.makedirs(output_dir)
        print(f"Output directory {output_dir} does not exist.")
    
    report_path = os.path.join(output_dir, "report.html")
    
    # Construct the command
    command = [
        "WinMergeU.exe", "-e", "-u",
        "-dl", "Original", "-dr", "Modified",
        file1, file2, "-o", report_path
    ]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Report generated successfully at {report_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate report: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file1 = os.path.abspath(glob.glob("C:\\Users\npotter\Testing\Redlines\Test1.txt"))
file2 = os.path.abspath(glob.glob("C:\\Users\npotter\Testing\Redlines\Test2.txt"))
output_dir = os.path.abspath(glob.glob("C:\\Users\npotter\Testing\Redlines"))

generate_winmerge_report(file1, file2, output_dir)


