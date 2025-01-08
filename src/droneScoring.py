whatMission = str(input("What Mission did you do Piloting, Teamwork, or Auto"))
if whatMission == "Piloting" :
    takeOf = int(input("How many times did you take of: "))
    figure8 = int(input("How many times did you do the figure 8: "))
    bigHole = int(input("How many times did you fly through the big hole: "))
    smallHole = int(input("How many times did you fly through the small hole: "))
    yellowHoop = int(input("How many times did you fly through the yellow hoop: "))
    greenHoop = int(input("How many times did you fly through the green hoop: "))
    box = int(input("What box did you land on (1 for big, 2 for small, 0 for none):"))
    totalScore = str(takeOf*10 + figure8*40 + bigHole*20 + smallHole*40 + yellowHoop*15 + greenHoop*15 + box*20)

if whatMission == "Auto" :
    colorMatch = int(input("How many times you get color match: "))
    takeOfAuto = int(input("How many times did you take of:  "))
    figure8Auto = int(input("How many times did you do the figure 8:  "))
    underArch = int(input("How many times did you fly through the under arch gates: "))
    bigHoleAuto = int(input("How many times did you fly through the big hole:  "))
    smallHoleAuto = int(input("How many times did you fly through the small hole:  "))
    yellowHoopAuto = int(input("How many times did you fly through the yellow hoop:  "))
    greenHoopAuto = int(input("How many times did you fly through the green hoop:  "))
    boxAuto = int(input("What box did you land on (1 for big, 2 for small, 0 for none): "))
    if boxAuto == 1 :
        totalScore = str(colorMatch * 15 + takeOfAuto * 10 + figure8Auto * 40 + underArch * 5 + bigHoleAuto * 20 + smallHoleAuto * 40 + yellowHoopAuto * 15 + greenHoopAuto * 15 + boxAuto * 25)
    else:
        totalScore = str(colorMatch*15 + takeOfAuto*10 + figure8Auto*40 + underArch*5 + bigHoleAuto*20 + smallHoleAuto*40 + yellowHoopAuto*15 + greenHoopAuto*15 + boxAuto*20)

if whatMission == "Teamwork" :
    whatColor = int(input("What color did you go for color match(0 blue, 1 green): "))
    greenBags = int(input("How many green beanbags: "))
    blueBags = int(input("How many blue beanbags: "))
    greenBall = int(input("How many green balls: "))
    blueBall = int(input("How many green balls: "))
    landing = int(input("Did person 1 land on (0 no landing, 1 big cube, 2 small cube, 3 landing pad, 4 bullseye): "))
    landing2 = int(input("Did person 1 land on (0 no landing, 1 big cube, 2 small cube, 3 landing pad, 4 bullseye): "))
    if landing == 0 :
        landingScore = 0
    elif landing % 2 == 1 :
        landingScore = 15
    else:
        landingScore = 25

    if landing2 == 0 :
        landing2Score = 0
    elif landing2 % 2 == 1 :
        landing2Score = 15
    else:
        landing2Score = 25

    if whatColor == 1 :
        totalScore = str( 2*(greenBags*greenBall) + blueBall + blueBall + landingScore + landingScore)
    else:
        totalScore = str( 2*(blueBags*blueBall) + greenBall + greenBags + landingScore + landingScore)

print(totalScore)