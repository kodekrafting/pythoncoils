# beginning.py: kodekrafting 2016

class Personality:
    def __init__(self):
        self.happiness  = 10 # out of 10
        self.confidence = 0  # we can only move up from here
        self.knowledge  = 0  # because we all have to start somewhere

    def share_code(self, your_thing):
        print(your_thing)

    def admire_code(self):
        self.confidence += 1
        self.knowledge  += 1

    def write_code(self, emotional_state):
        code = "Poetry is"
        for energy in range(emotional_state):
            code += (" awesome")
        code += ("!")
        return code

    def celebrate(self):
        your_code = self.write_code(self.happiness)
        self.admire_code()          # believe in yourself
        self.share_code(your_code)  # because why not?

    def spread_the_word(self, this_thing_I_care_about):
        print("Could you help me make", this_thing_I_care_about, "a big thing?")

Me = Personality()
print("Hello, world!")
where_you_least_expect_it = "staring at our bright screens" \
                            "hearing familiar clicks of keys" \
                            "we delve into the world online" \
                            "and create new things" \
                            "beauty emerging from our web" \
                            "the distance between us will slowly ebb"

if "beauty" in where_you_least_expect_it:
    Me.celebrate()
    Me.spread_the_word("#codepoetry")
