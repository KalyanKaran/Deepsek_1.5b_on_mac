import os
import subprocess

def test_model(prompt):
    """
    Call the MLX model generate command via subprocess.
    Make sure that the model path is correct.
    """
    # Construct the command
    model_path = os.path.join("..", "models", "DeepSeek-R1-Distill-Qwen-1.5B-4bit")
    command = [
        "python3", "-m", "mlx_lm.generate",
        "--model", model_path,
        "--prompt", prompt,
        "--max-tokens", "800"  # Using the recognized flag for maximum tokens
    ]
    
    print("Running command:", " ".join(command))
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Subprocess finished successfully.")
        print("STDOUT:\n", result.stdout)
        if result.stderr:
            print("STDERR:\n", result.stderr)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error during model inference:")
        print("Return Code:", e.returncode)
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        return None

def main():
    print("Starting test_model.py")
    prompt = ("what is pydantic AI")
    print(f"Testing model with prompt: {prompt}")
    
    output = test_model(prompt)
    if output:
        print("Model Output:")
        print(output)
        # Optionally, write the output to a file in the outputs directory.
        output_dir = os.path.join("..", "outputs")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "predictions.txt")
        with open(output_path, "w") as f:
            f.write(output)
        print(f"Output saved to {output_path}")
    else:
        print("No output generated.")

if __name__ == "__main__":
    main()