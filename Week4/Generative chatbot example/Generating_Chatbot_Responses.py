import numpy as np
from seq2seq import encoder_model, decoder_model, num_decoder_tokens, target_features_dict, reverse_target_features_dict, max_decoder_seq_length

class ChatBot:
  
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
  
  def start_chat(self):
    user_response = input("Hi, I'm a chatbot trained on dialog from The Princess Bride. Would you like to chat with me?\n")
    
    if user_response in self.negative_responses:
      print("Ok, have a great day!")
      return
    
    self.chat(user_response)
  
  def chat(self, reply):
    while not self.make_exit(reply):
      reply = input(self.generate_response(reply))
    
  # update .generate_response():
  def generate_response(self, user_input):
    states_value = encoder_model.predict(user_input)
  target_seq = np.zeros((1, 1, num_decoder_tokens))
  target_seq[0, 0, target_features_dict['<START>']] = 1.

  chatbot_response = ''

  stop_condition = False
  while not stop_condition:
    output_tokens, hidden_state, cell_state = decoder_model.predict(
      [target_seq] + states_value)

    sampled_token_index = np.argmax(output_tokens[0, -1, :])
    sampled_token = reverse_target_features_dict[sampled_token_index]
    chatbot_response += " " + sampled_token

    if (sampled_token == '<END>' or len(chatbot_response) > max_decoder_seq_length):
      stop_condition = True

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, sampled_token_index] = 1.

    states_value = [hidden_state, cell_state]

  return chatbot_response
  
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a great day!")
        return True
      
    return False
  
chatty_mcchatface = ChatBot()
# call .generate_response():
chatty_mcchatface.generate_response("Hey!")

