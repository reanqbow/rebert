
# Exercise completed

Exploration 1.3 (Hard)

# Modifications

## Set variables
### 1
OAI_MODEL_TEMPERATURE = 0.9
OAI_MODEL_MAX_TOKENS = 500

### 2
OAI_MODEL_TEMPERATURE = 0.2
OAI_MODEL_MAX_TOKENS = 500

### 3
OAI_MODEL_TEMPERATURE = 0.2
OAI_MODEL_MAX_TOKENS = 100


## Call variables in the function
def new_chat_context():
    chat_context = dict()
    chat_context['model'] = OAI_MODEL
    chat_context['messages'] = list()
    chat_context['temperature'] = OAI_MODEL_TEMPERATURE
    chat_context['max_completion_tokens'] = OAI_MODEL_MAX_TOKENS
    return chat_context

# Results

## Temperature
This will change the randomness of the response. For the same "Recommend a movie that I should see this weekend" question

When I set it to 0.2, the response is more like a generic recommendation without any logical structure.
When I set it to 0.9, the response shows a structured opinion on why this movie should be recommended from different aspects lie "engaging story" or "masterful direction".

## Max token
This will change the maximum length of the response.

When I set it to 500, the response is roughly about 300 words and it's capped at about 70 words and not able to complete the message.