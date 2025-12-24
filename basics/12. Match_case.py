# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execte some code if a valid matches a 'case'
#                                Benefits:cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednessday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _ :
            return f"{day} is not a valid day"
        
print(day_of_week(3))
# Output = It is Tuesday