import sys, datetime, json
import os

try:
    import requests
except:
    print("\n\nThis example depends upon the 'requests' module. This exception is because ")
    print("it looks like you have not installed the 'requests' module. You should visit")
    print("     https://pypi.org/project/requests/")
    print("for instructions on installing 'requests'.\n\n")
    sys.exit()


#   CONSTANTS
#
#   This example will use an OpenAI service
OAI_HOST = "https://api.openai.com"
OAI_SERVICE_ENDPOINT = "/v1/chat/completions"
OAI_MODEL = "gpt-4-turbo-preview"
OAI_MODEL_TEMPERATURE = 0.9
OAI_MODEL_MAX_TOKENS = 100
#
#   One should never put their key right in the code like this
#   A later prototype will show an alternative that solves this problem
API_KEY = os.environ["OPENAI_API_KEY"]

#
#   Create a new chat turn.
#   Each chat turn is a dictionary with a 'role' and 'content'
def new_chat_turn(role="",content=""):
    turn = dict()
    turn['role'] = role
    turn['content'] = content
    return turn
#
#   The code needs to maintain the status of the chat. This status 
#   will include parameters that tell the model how it should respond
#   as well as all of the user questions and the responses.
def new_chat_context():
    chat_context = dict()
    chat_context['model'] = OAI_MODEL
    chat_context['messages'] = list()
    chat_context['temperature'] = OAI_MODEL_TEMPERATURE
    chat_context['max_completion_tokens'] = OAI_MODEL_MAX_TOKENS
    return chat_context
#
#   Making a request is about modifying the growing chat_context
#   setting up the HTTP request URL and request headers, and making
#   the request.
def make_chat_request(user_text="", chat_context=None, api_key=""):
    #   If no chat context is provided, then this is a new chat
    if not chat_context:
        # create and use a new chat context
        chat_context = new_chat_context()
    
    #   We use the text we got from the user to create a user turn
    user_turn = new_chat_turn("user",user_text)
    #   Add that user turn to the list of messages in the context
    chat_context['messages'].append(user_turn)
    
    #   The whole context is payload for the request - a request body
    payload = json.dumps(chat_context)
    
    #   Create header information for the request - this must include
    #   the 'Content-Type' key set to 'application/json' and the
    #   'Authorization' key set to include your API key
    header = dict()
    header['Content-Type'] = "application/json"
    header['Authorization'] = f"Bearer {api_key}"
    
    #   The service URL is the host and the service endpoint
    service_url = OAI_HOST + OAI_SERVICE_ENDPOINT
    
    #   Make this as a POST request
    response = requests.post(service_url,
                             headers=header,
                             data=payload)
    #   The response should be 'application/json' so extract the JSON
    resp_dict = response.json()
    #   There is a lot in the response - just extract the message
    # print(resp_dict)
    assistant_turn = resp_dict['choices'][0]['message']
    #   Add the response to our chat context
    chat_context['messages'].append(assistant_turn)
    return chat_context

#
#   The main is called from the command line and just loops asking
#   for user to input
def main():
    #   Initialize some variables
    chat_context = None
    assistant_name = sys.argv[0].rpartition('.')[0]
    print()
    
    #   A rather simple chat loop
    user_text = input(f"You > ").strip()
    print()
    #   While the user enters some text - not 'quit'
    while len(user_text)>0 and (user_text.lower() != "quit"):
        
        #   Use that user text to make the request
        chat_context = make_chat_request(user_text, chat_context, API_KEY)
        
        #   Get the last message - it should be the text response
        assistant_turn = chat_context['messages'][-1]
        
        #   Show that response
        print(f"{assistant_name} > {assistant_turn['content']}")
        print()
        
        #   Get the next user turn
        user_text = input(f"You > ").strip()
        print()
    
    return

if __name__ == '__main__':
    main()   



