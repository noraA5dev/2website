def main():
    def Option1NC():
        Var1NC = input('\nWould You like to go forward or left. F/L: ')
        if Var1NC == 'F':
            print('')
        elif Var1NC == 'f':
            print('HYes')
        elif Var1NC == 'L':
            Option2NC()
        elif Var1NC == 'l':
            Option2NC()
        else:
            print('You most likely inputted your answer wrong: If your answer is forward, then input "F", or "f".')
            Option1NC()
            return

    def Option2NC():
        Var2NC = input('\nYou Find A Cave. Do You want to go in or find a different way in? Press "GI" to go in, '
                       'and press "DW": to go a different way.: ')
        if Var2NC == 'GI':
            print('Go In')
        elif Var2NC == 'DW':
            print('Different Way')
            return
        else:
            print('Try Again')
            Option2NC()
            return


    Option1NC()


if __name__ == '__main__':
    main()
