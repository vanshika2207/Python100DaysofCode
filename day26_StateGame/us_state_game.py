import turtle
import pandas as pd

# Load data
data = pd.read_csv('50_states.csv')

# Set up Turtle graphics
screen = turtle.Screen()
screen.title('U.S State Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

state = turtle.Turtle()
state.penup()
state.hideturtle()

# Initialize variables
score = 0
is_game = True

# Main game loop
guess_state=[]
while is_game:
    # Get user input
    state_guess = screen.textinput(title=f'{score}/50 States Correct', prompt='What\'s another state name').title()

    # Check if the guessed state is correct
    if state_guess in data['state'].tolist():
        guess_state.append(state_guess)
        score += 1
        # Get the coordinates of the guessed state
        cor = data[data.state == state_guess]
        x_cor = cor['x'].values[0]
        y_cor = cor['y'].values[0]
        # Move to the coordinates and display the state name
        state.goto(x_cor, y_cor)
        state.write(state_guess, align='left', font=('Arial', 8, 'normal'))
    else:
        is_game = False

# Display final score
screen.textinput(title='Game Over', prompt=f'You got {score}/50 states correct. Press OK to exit.')
not_guessed=[]
for i in data['state'].tolist():
    if i not in state_guess:
        not_guessed.append(i)
state_csv=pd.DataFrame({'states':not_guessed})
state_csv.to_csv('state.csv')
# Keep the window open
turtle.mainloop()
