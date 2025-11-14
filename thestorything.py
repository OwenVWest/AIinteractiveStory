from transformers import pipeline

# Load pre-trained text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Create initial prompt
prompt = input("\nEnter the prompt for your story to start with: ")

# Initialize story string
story = ""

for _ in range(5): 
    continuation = generator(prompt, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
   
    # Add the generated text to the story
    story += " " + continuation[0]['generated_text']
    print(story)
    # Use last sentence and the user prompt the next prompt
    prompt = continuation[0]['generated_text'].split('.')[-2] + input("\n Enter a short phrase to continue the story based on: ")


