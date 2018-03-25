num=10
to_guess=True
while to_guess:
  guess=int(input("Guess the number:"))
  if guess==num:
    print("You guessed it right!")
break
    '''to_guess=False'''
  elif guess<num:
    print("Your guess is lesser than the number.")
  else:
    print("Your guess is greater than the number.")
