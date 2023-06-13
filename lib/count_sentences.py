#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value = "string"):
    self.value = value


  def get_value(self):
    return self._value 
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print('The value must be a string.')

  value = property(get_value, set_value)

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')

  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    if self.is_exclamation() or self.is_question() or self.is_sentence():
      total_punctuations = self.value.count('. ')+self.value.count('? ')+self.value.count('! ') + 1
    else:
      total_punctuations = self.value.count('. ')+self.value.count('? ')+self.value.count('! ')
    return total_punctuations