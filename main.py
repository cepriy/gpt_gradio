# This is a sample Python script.


import openai
import  gradio as gr
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
openai.api_key = "YOUR API KEY"
prompt = "The following is an application with an assistant"




def get_output(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature = 0.9,
        prompt = prompt,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        stop = ["AI", "Human"]

    )
    return response.choices[0].text


def gpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = get_output(inp)
    history.append((input, output))
    return history, history


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = "\nAI"
    restart = "\nHuman"
    block = gr.Blocks()
    # while(True):
    #     query = input("Ask a question to AI:\n")
    #
    #     print("OpenAI response", get_output(query))
    with block:
       gr.Markdown("<h1><center>GPT Application</center></h1>"),
       chatbot = gr.Chatbot()
       message = gr.Textbox(placeholed = prompt)
       state = gr.State()
       button = gr.Button("Send")
       button.click(gpt_clone, inputs=[message, state], outputs=[chatbot, state])

    block.launch(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
