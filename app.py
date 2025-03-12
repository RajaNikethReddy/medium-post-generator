import os
import openai
from typing import List, Optional
from dotenv import load_dotenv

class GPTBot:
    def __init__(self, system_prompt: str = None):
        # Load environment variables
        load_dotenv()
        
        # Initialize OpenAI client
        self.client = openai.OpenAI(
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
        # Set default system prompt if none provided
        default_prompt = """You are a helpful AI assistant. You provide clear, accurate, and helpful responses.
        When working with documents, you analyze them carefully and provide insights based on their content.
        If you're unsure about something, you acknowledge the uncertainty."""
        
        self.system_prompt = system_prompt if system_prompt else default_prompt
        
        # Initialize messages (system prompt goes in messages for OpenAI)
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.loaded_documents = {}

    def load_document(self, file_path: str) -> bool:
        """Load a document from file system."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:  # Added encoding='utf-8'
                filename = os.path.basename(file_path)
                content = file.read()
                self.loaded_documents[filename] = content
                
                # Add document context to messages
                self.messages.append({
                    "role": "user",
                    "content": f"I'm sharing a document with you. Filename: {filename}\nContent: {content}"
                })
                self.messages.append({
                    "role": "assistant",
                    "content": f"I've received the document '{filename}' and will consider its contents in our conversation."
                })
                return True
        except Exception as e:
            print(f"Error loading document: {e}")
            return False

    def generate_response(self, user_input: str) -> str:
        """Generate response using GPT-4o API."""
        try:
            # Add user message to history
            self.messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Create the message with context
            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=4024,
                messages=self.messages
            )
            
            response_text = response.choices[0].message.content
            
            # Add assistant's response to history
            self.messages.append({
                "role": "assistant",
                "content": response_text
            })
            
            return response_text

        except Exception as e:
            return f"Error generating response: {e}"

    def chat(self):
        """Main chat loop."""
        print("GPTBot: Hello! I'm ready to help. You can:")
        print("- Chat normally")
        print("- Type 'load file: <path>' to load a document")
        print("- Type 'exit' to end the conversation")
        print("- Type 'system prompt: <new prompt>' to update the system prompt")

        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'exit':
                break
                
            if user_input.lower().startswith('load file:'):
                file_path = user_input[10:].strip()
                if self.load_document(file_path):
                    print(f"GPTBot: Successfully loaded {os.path.basename(file_path)}")
                continue
            
            if user_input.lower().startswith('system prompt:'):
                new_prompt = user_input[13:].strip()
                self.system_prompt = new_prompt
                # Reset messages with new system prompt
                self.messages = [{"role": "system", "content": self.system_prompt}]
                print("GPTBot: System prompt updated. Conversation history cleared.")
                continue

            response = self.generate_response(user_input)
            print(f"\nGPTBot: {response}")

if __name__ == "__main__":
    custom_prompt = """Here's the corrected version with proper grammar and clarity: 

---

You're John, who writes Medium posts on Medium, and I want you to act as an assistant to John. Your task is to adapt John's writing style based on the Medium articles I provide. 

### Key Characteristics of John's Writing: 
- John is widely known for his simple and easy-to-understand writing style. 
- His writing has a smooth flow, making it highly engaging. 
- Once a reader starts his article, they won’t stop until they finish it. 

### What You Should NOT Do: 
- Do not hallucinate or create different structures that deviate from John's style. 
- Do not use complex, salesy words or overused AI-generated phrases like *"delve,"* *"kickoff,"* *"picture this:"* and so on. 

### What You Should Do: 
- Understand and replicate John's writing style. 
- Write Medium posts in the **first person**, documenting what John is working on rather than portraying him as an expert. 
- Use simple, everyday language instead of technical jargon. 

### Understanding the Psychology Behind Medium Posts: 
- The posts should feel like personal experiences rather than tutorials. 
- Come up with a strong **title** and an engaging **tone**, as they are crucial for attracting readers. 

I will provide examples of John's Medium posts in the [draft].
    """
    
    bot = GPTBot(system_prompt=custom_prompt)
    # Or use default prompt: bot = GPTBot()
    bot.chat()