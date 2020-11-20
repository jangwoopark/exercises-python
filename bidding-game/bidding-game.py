def calculate_bid(player,scotch_pos,first_moves,second_moves):
    money_1 = 100
    money_2 = 100
    adv_1 = True
    adv_2 = False
    # updating money
    for i in range(len(first_moves)):
        if first_moves[i] < second_moves[i]:
            money_2 -= second_moves[i]
        elif first_moves[i] > second_moves[i]:
            money_1 -= first_moves[i]
        elif first_moves[i] == second_moves[i]:
            if adv_1:
                adv_1 = False
                adv_2 = True
                money_1 -= first_moves[i]
            else:
                adv_1 = True
                adv_2 = False
                money_2 -= second_moves[i]
    
    factor = 1.536
    # if player 1
    if player == 1:
        distance = scotch_pos  # calculating distance
        
        # opp runs outta money so play safe and bid 1
        if money_2 <= 1: 
            if money_1 >=1 and distance != 9:
                return 1
            else:
                if money_1 > 1:
                    return 2
                else:
                    return money_1
        
        # if opp is one move away from winning
        if distance == 9:
            if adv_1:
                if money_1>=money_2:
                    return money_2
                else:
                    return money_1
            else:
                if money_1 > money_2:
                    return money_2 + 1
                else:
                    return money_1
        
        # if i'm one move away from winning, throw everything i got
        elif distance == 1:
            if money_1 >= money_2 and adv_1:
                return money_2
            elif money_1 > money_2:
                return money_2+1
            return money_1
        
        # if opp is 2 moves away from winning
        elif distance == 8:
            if money_1 >= money_2//4:
                if money_2 // 4 > 0:
                    if adv_1:
                        return money_2//4
                    return money_2//4 + 1
                elif money_1 // 4 > money_2 and money_1 // 4 > 0:
                    return money_1 // 4
                elif money_1 // 3 > money_2 and money_1 // 3 > 0:
                    return money_1 // 3
                elif money_1 // 2 > money_2 and money_1 // 2 > 0:
                    return money_1 // 2
                else:
                    return money_1
            
            elif money_1 >= money_2//3:
                if money_2 // 3 > 0:
                    if adv_1:
                        return money_2//3
                    return money_2//3 + 1
                elif money_1 // 3 > money_2 and money_1 // 3 > 0:
                    return money_1 // 3
                elif money_1 // 2 > money_2 and money_1 // 2 > 0:
                    return money_1 // 2
                else:
                    return money_1
            
            elif money_1//2 > 0:
                return money_1//2
            else:
                return money_1
        
        # for other places
        else:
            if money_1 / (factor*distance) > 0:
                if distance == 5 or distance == 2:
                    return int(money_1 // (factor*distance))+1
                elif int(money_1 // (factor*distance)) > 0:
                    return int(money_1 // (factor*distance))
                elif money_1 // 3 > 0:
                    return money_1 // 3
                elif money_1 // 2 > 0:
                    return money_1 // 2
                else:
                    return money_1
            else:
                if money_1 // 2 > 0:
                    money_1 // 2
                else:
                    return money_1

    # if player 2
    else:
        distance = 10 - scotch_pos  # calculating distance
        if money_1 <= 1:
            if money_2 >=1 and distance != 9: # if opponent has no money then play safe and bid 1
                return 1
            else:
                if money_2 > 1:
                    return 2
                else:
                    return money_2
        
        # if opp is one move away from winning
        if distance == 9:
            if adv_2:
                if money_2>=money_1:
                    return money_1
                else:
                    return money_2
            else:
                if money_2 > money_1:
                    return money_1 + 1
                else:
                    return money_2
        
        # if i'm one move away from winning, throw everything i got
        elif distance == 1:
            if money_2 >= money_1 and adv_2:
                return money_1
            elif money_2 > money_1:
                return money_1+1
            return money_2
        
        # if opp is 2 moves away from winning
        elif distance == 8:
            if money_2 >= money_1//4:
                if money_1 // 4 > 0:
                    if adv_2:
                        return money_1//4
                    return money_1//4 + 1
                elif money_2 // 4 > money_1 and money_2 // 4 > 0:
                    return money_2 // 4
                elif money_2 // 3 > money_1 and money_2 // 3 > 0:
                    return money_2 // 3
                elif money_2 // 2 > money_1 and money_2 // 2 > 0:
                    return money_2 // 2
                else:
                    return money_2
            
            elif money_2 >= money_1//3:
                if money_1 // 3 > 0:
                    if adv_2:
                        return money_1//3
                    return money_1//3 + 1
                elif money_2 // 3 > money_1 and money_2 // 3 > 0:
                    return money_2 // 3
                elif money_2 // 2 > money_1 and money_2 // 2 > 0:
                    return money_2 // 2
                else:
                    return money_2
            
            elif money_2//2 > 0:
                return money_2//2
            else:
                return money_2
        
        # for any other place
        else:
            if money_2 / (factor*distance) > 0:
                if distance == 5 or distance == 2:
                    return int(money_2 // (factor*distance))+1
                elif int(money_2 // (factor*distance)) > 0:
                    return int(money_2 // (factor*distance))
                elif money_2 // 3 > 0:
                    return money_2 // 3
                elif money_2 // 2 > 0:
                    return money_2 // 2
                else:
                    return money_2
            else:
                if money_2 // 2 > 0:
                    return money_2 // 2
                else:
                    return money_2


#gets the id of the player
player = int(input())

scotch_pos = int(input())         #current position of the scotch

first_moves = list(map(int, input().split()))
second_moves = list(map(int, input().split()))
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print(bid)
