from groq import Groq
import os
import language_tool_python


system_prompt = """Correct the following text and return the corrected version. Do not provide explanations, 
    just return the corrected text. If the text is already correct, return \"correct text\"."""


def LLM_correction(text,model_name = "llama3-8b-8192"):
    client = Groq(api_key = os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        #
        # Required parameters
        #
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": f"{text}",
            }
        ],

        # The language model which will generate the completion.
        model=model_name,

        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=0.01,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )
    return chat_completion.choices[0].message.content


def correct_grammar(input_text):
    
    # Initialize LanguageTool instance  
    tool = language_tool_python.LanguageTool('de-DE')  

    # Check for language errors in the input text  
    matches = tool.check(input_text)  

    # Initialize lists to store detected mistakes and their corrections  
    mistakes = []  
    corrections = []  
    start_positions = []  
    end_positions = []  

    # Iterate through the detected language errors  
    for rule in matches:  
        if len(rule.replacements) > 0:  
            start_positions.append(rule.offset)  
            end_positions.append(rule.errorLength + rule.offset)  
            mistakes.append(input_text[rule.offset : rule.errorLength + rule.offset])  
            corrections.append(rule.replacements[0])   

    return list(zip(mistakes,corrections))





if __name__ == "__main__":

    # llama3-70b-8192 this is a bigger model that can be used
    # llama3-8b-8192: smaller model
    txt = "Halo ich heisse Giannis und komme von Griechenland"
    txt = "Dies sind ein Beispielsatz mit eine Fehler"
#     txt = "Hallo, ich komme aus Griechenland"
    rsp = LLM_correction(txt,"llama3-70b-8192")
# # Print the completion returned by the LLM.
    print(rsp)
    
    #corrections = correct_grammar(txt)
    #print(corrections)




