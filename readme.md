# Python Learning

My journey learning Python.

I'm a QA engineer with over five years in games with EA and Microsoft. 
That includes test design, feature ownership, and breaking things professionally. This repo is me
building the other half of the craft: writing the code instead of just
testing it. Everything here is built from scratch as I learn, bugs and all.

## Projects

### greeting.py
My first program! Asks your name and how many hours you game, then judges
you for it. Seemed easy enough, but it survived its own QA pass! 
Invalid input is handled with a `try/except` retry loop instead of crashing,
and the input-validation logic is separated from the response logic.

**Run it:**
python greeting.py

### the_number_guessing_game.py
The computer picks a secret number from 1 to 100 and you try to guess it,
with "too high" / "too low" hints (and some abuse) after each guess. Built
on the input-validation pattern from greeting.py, plus boundary checks that
reject guesses outside 1–100 and a random target via `random.randint`.

**Run it:**
`python the_number_guessing_game.py`


If you're reading this, you're a really cool person. Thank you, and if you need any help on your journey please don't hesitate to reach out! :)

More Coming.
