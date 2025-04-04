# Exercise completed

Exploration 1.3 (Hard)

# Modifications

## Set variables
OAI_MODEL_TEMPERATURE = 0.8
OAI_MODEL_MAX_TOKENS = 100

## Call variables in the function
def new_chat_context():
    chat_context = dict()
    chat_context['model'] = OAI_MODEL
    chat_context['messages'] = list()
    chat_context['temperature'] = OAI_MODEL_TEMPERATURE
    chat_context['max_completion_tokens'] = OAI_MODEL_MAX_TOKENS
    return chat_context


