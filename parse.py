from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define a prompt template that guides the model on how to extract specific information
# The template includes specific instructions for what information to extract from the DOM content
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama language model with a specific version (llama3.1 in this case)
model = OllamaLLM(model="llama3.1")

# Function to parse DOM content using the Ollama model
# Takes a list of DOM content chunks and a description of what data to extract
def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt using the template, which combines the DOM content and user-provided parse description
    prompt = ChatPromptTemplate.from_template(template)

    # Create a chain that combines the prompt and the model to process input and generate output
    chain = prompt | model

    # Initialize an empty list to store the results of the parsed content
    parsed_results = []

    # Loop through each chunk of the DOM content, sending it to the model for processing
    for i, chunk in enumerate(dom_chunks, start=1):
        # For each chunk, invoke the model and provide the 'dom_content' and 'parse_description' variables
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )

        # Print a message to track progress, indicating which batch is being processed
        print(f"Parsed batch {i} of {len(dom_chunks)}")

        # Append the parsed response to the results list
        parsed_results.append(response)

    # Join all the parsed results into a single string and return the result
    return "\n".join(parsed_results)
