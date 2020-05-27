from prep import input_features_dict, target_features_dict, reverse_input_features_dict, reverse_target_features_dict, max_decoder_seq_length, input_docs, target_docs, input_tokens, target_tokens, max_encoder_seq_length
from training_model import decoder_inputs, decoder_lstm, decoder_dense, encoder_input_data, num_decoder_tokens, num_encoder_tokens

from tensorflow import keras
from keras.layers import Input, LSTM, Dense
from keras.models import Model, load_model
import numpy as np
import re

training_model = load_model('training_model.h5')
###### because we're working with a saved model
encoder_inputs = training_model.input[0]
encoder_outputs, state_h_enc, state_c_enc = training_model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]
######
encoder_model = Model(encoder_inputs, encoder_states)

latent_dim = 256
decoder_state_input_hidden = Input(shape=(latent_dim,))
decoder_state_input_cell = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]
decoder_outputs, state_hidden, state_cell = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_hidden, state_cell]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)

def decode_sequence(user_input):
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