"""
Alternative way to get the count of the words in a dictionary
using Counter from collections
"""

from collections import Counter

# text to use
cruel_summer = """
Fever dream high
In the quiet of the night
You know that I caught it (oh yeah, you're right, I want it)
Bad, bad boys
Shiny toy with a price
You know that I bought it (oh yeah, you're right, I want it)
Killing me slow, out the window
I'm always waiting for you to be waiting below
Devils roll the dice, angels roll their eyes
What doesn't kill me makes me want you more
And it's new
The shape of your body, it's blue
The feeling I've got
And it's ooh, whoa oh
It's a cruel summer
It's cool
That's what I tell 'em, no rules
In breakable heaven but
Ooh, whoa oh
It's a cruel summer
With you
Hang your head low
In the glow of the vending machine
I'm not dying (oh yeah, you're right, I want it)
We say that we'll just screw it up in these trying times
We're not trying (oh yeah, you're right, I want it)
So cut the headlights
Summer's a knife
I'm always waiting for you
Just to cut to the bone
Devils roll the dice
Angels roll their eyes
And if I bleed
You'll be the last to know
Oh, it's new
The shape of your body, it's blue
The feeling I've got
And it's ooh, whoa oh
It's a cruel summer
It's cool
That's what I tell 'em, no rules
In breakable heaven but
Ooh, whoa oh
It's a cruel summer
With you
I'm drunk in the back of the car
And I cried like a baby coming home from the bar (oh)
Said "I'm fine", but it wasn't true
I don't wanna keep secrets just to keep you
And I, snuck in through the garden gate
Every night that summer just to seal my fate (oh)
And I screamed for whatever it's worth
I love you, ain't that the worst thing you ever heard?
He looks up, grinning like a devil
It's new
The shape of your body, it's blue
The feeling I've got
And it's ooh, whoa oh
It's a cruel summer
It's cool
That's what I tell 'em, no rules
In breakable heaven but
Ooh, whoa oh
It's a cruel summer
With you
I'm drunk in the back of the car
And I cried like a baby coming home from the bar (oh)
Said "I'm fine", but it wasn't true
I don't wanna keep secrets just to keep you
And I, snuck in through the garden gate
Every night that summer just to seal my fate (oh)
And I screamed for whatever it's worth
I love you, ain't that the worst thing you ever heard?
"""

# use split() method to create list of words
cruel_summer_word_list = cruel_summer.split()

# user Counter from collections to get the count of the words, will return list of tuples
word_counts = Counter(cruel_summer_word_list)


# convert list of tuples to dict
cruel_summer_word_dict = {}
cruel_summer_word_dict = dict(word_counts)


print(cruel_summer_word_dict)
print(type(cruel_summer_word_dict))

# sort dictionary
sorted_lyrics = sorted(cruel_summer_word_dict.items(), reverse=True)
# view word counts
# need to use .items() at the end of the dictionary!
for word, word_count in sorted_lyrics:
    print(word)
    print(word_count)