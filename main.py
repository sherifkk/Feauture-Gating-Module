from user import User
from featureGating import FeatureGating

def main():
    print("")
    print("...............Welcome to Feature Gating!.....................")
    print("Please input the user attributes! Keep empty on unknown value!")
    print("")

    while True:
        userAttributes = {};
        userAttributes["gender"] = input("Enter the gender of the user, (male/female): ")
        userAttributes["age"] = input("Enter the age of the user, (1..100): ")
        userAttributes["salary"] = input("Enter the salary of the user: ")
        userAttributes["height"] = input("Enter the height of the user in cm: ")
        userAttributes["city"] = input("Enter the city of the user: ")
        userAttributes["spends"] = input("Enter the total spend by the user per month: ")
        userAttributes["geo"] = input("Enter the latitute and longitude of the user with a space in between: ")
        
        try:
            user = User(userAttributes)
        except ValueError as err:
            print("Value error: {0}, try again!".format(err))
            continue;
        break;

    print("")
    print("User Created! Enter Feature Details!")
    print("")

    while True:
        featureName = input("Enter the featureName: ")
        conditionalExpression = input("Enter the Conditional Expression: ").lower()
        FeatureGating().isAllowed(featureName, conditionalExpression, user.userAttributes)
        break;
    

if __name__=="__main__":
    main()