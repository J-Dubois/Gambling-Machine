import random

MAX_LINES = 3
MAX_COLUMNS = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 5,
  "B": 7,
  "C": 9,
  "D": 11
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  for line in range(lines):
    symbol = columns[0][line]
  for column in columns:
    symbol_to_check = column[line]
    if symbol != symbol_to_check:
      break
  else:
    winnings += values[symbol] * bet

  return winnings

def get_slot_machin_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []                                                                                                 # we define our columns list
  for _ in range(cols):                                                                                        # we generate a column for every single column we have
    column = []                                                                                           # Here we will be picking randoms values for each rows of our columns
    current_symbols = all_symbols[:]    # [:] allow you to copy a list (here all_symbols)                      # we loop throught 
    for _ in range(rows):                                                                                      # we loop throught the number of value that we need to generate (= to number of rows in our slot machine)
      value = random.choice(current_symbols)                                                                   # the first value we get is random from current_symbols list (= copy of all_symbols list)
      current_symbols.remove(value)     # find first instance of this value in the list and remove it          # we remove the random value so that we don't pick it again
      column.append(value)                                                                                # we adde this value to our column

    columns.append(column)                                                                                # once we have all our rows, we add our column to our column list

  return columns

# to print the column vertically we need to do a "transposing"
def print_slot_machine(columns):                          # we loop through every single row that we have
  for row in range(len(columns[0])):                      # we every single row we loop through every single column
    for i, column in enumerate(columns):                  # and for every column we only print the current row that we're on, this will basically flips our columns for begin horizontal to vertical100
      if i != len(columns) - 1:
        print(column[row], end=" | ")                     # end=  is the new line statement (normally end="\n")
      else:
        print(column[row], end=" | ")
    print()                                               # we print an empty spot to launch the next line

# USER DEPOSIT
def deposit():  #Here we create the function "deposit" which will be the user deposit to play the game
  while True:   #we create a loop so that until a valid amount is put in, the system will ask again
    amount = input("How much do you want to deposit ? $")   #Here the user will put an amount of his choice
    if amount.isdigit():   # For it to work we need the amount to be valid digit (no strings or negative numbers) is.digit is used for that
      amount = int(amount)   # By default, the amount will be in string, but to work we need to put it in int
      if amount > 0:    
        break    # if amount is more than 0 the loop will stop
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")

  return amount   # it will indiquate us the amount and stop this function


def getLineNumber():
  while True:
    lines = input("How many line do you cant to bet on (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a correct number of lines do you want to bet on.")

  return lines


#def getColumnNumber():
  while True:
    column = input("How many columns do you want to bet on (1-" + str(MAX_COLUMNS) + ")? ")
    if column.isdigit():
      column = int(column)
      if 1 <= column <= MAX_COLUMNS:
        break
      else:
        print("Enter a correct number of columns you want to bet on.")
    else:
      print("Please enter a number.")

  return column
            

def getBet():
  while True:
    bet = input("What would you like to bet on each line ? ")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print(f"Enter a correct amount for the bet. It must be between ${MIN_BET} - ${MAX_BET}.")
    else:
      print("Please enter a number.")

  return bet

def spin(balance):
  lines = getLineNumber()
  #column = getColumnNumber()
  while True:
    bet = getBet()
    total_bet = bet * lines
    if total_bet > balance:
      print("You do not have the sufficient balance to bet.")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}.")

  slots = get_slot_machin_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)

  winnings = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won ${winnings}")
  
  return winnings - total_bet


def main():
  balance = deposit()
  while True:
    print(f"Current balance is: ${balance}")
    answer = input("Press enter to play (q to quit).")
    if answer == "q":
      break
    balance += spin(balance)

main()