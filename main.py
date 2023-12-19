import subprocess

def run_program_and_save_output(program_path, program_args, output_file):
    try:
        # Run the program and capture its stdout
        with open(output_file, 'w') as file:
            subprocess.run(['python3', program_path, program_args], stdout=file, text=True, check=True)
        
        print(f"Program output has been saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error running the program: {e}")

if __name__ == "__main__":
    # Example: Run "ls -l" and save the output to "student_output"
    program_path = 'api/0-gather_data_from_an_API.py'
    program_arguments = '2'
    output_filename = "student_output"

    run_program_and_save_output(program_path, program_arguments, output_filename)