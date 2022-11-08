import random


def start():
  my_play= input("Lets play!,'r' for rock; 's' for scissors; and 'p' for paper: ").lower()
  computer= random.choice(['r','s','p'])
  if my_play == computer:
    return 'dats a tie! '
  
  if check_win(my_play,computer):
    return 'You won!'
  return 'You Lost!'  



def check_win(player,opponent):
  if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
    return True

print(start())    