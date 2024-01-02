# This is the text story
import Nothing_Cave
story_starter = 'You have a table in front of you. There are two items on the table, a match, and an axe. You can ' \
                'choose either, or you can travel on without picking up an item. To pick up the match press "M". To ' \
                'Pick up the Axe, press "A". To pick up nothing, press "N".: '
def main():
    def Option1main():
        firstVar1main = input(story_starter)
        if firstVar1main == 'N':
            Nothing_Cave.main()
    Option1main()

if __name__ == '__main__':
    main()