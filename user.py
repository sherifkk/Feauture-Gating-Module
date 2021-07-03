from geo import Geo

class User:
    def __init__(self, userAttributes):
        self.userAttributes = self._is_valid_attributes(userAttributes)

    def _is_valid_attributes(self, userAttributes):
        if(userAttributes.get("gender")):
            userAttributes["gender"] = userAttributes["gender"].lower()
            if(userAttributes["gender"] != "male" and userAttributes["gender"] != "female"):
                raise ValueError("Gender must be male, female or empty ")
        
        if(userAttributes.get("age")):
            userAttributes["age"] = int(userAttributes["age"])
            if(userAttributes["age"] < 1 or userAttributes["age"] > 100 ):
                raise ValueError("Age must be in between 1 to 100 ")

        if(userAttributes.get("salary")):
            userAttributes["salary"] = float(userAttributes["salary"])
            if(userAttributes["salary"] > 10000):
                userAttributes["is_affluent"] = True

        if(userAttributes.get("height")):
            userAttributes["height"] = float(userAttributes["height"])
        
        if(userAttributes.get("spends")):
            userAttributes["spends"] = float(userAttributes["spends"])
        
        if(userAttributes.get("geo")):
            latitude, longitude = map(float, userAttributes["geo"].split())
            userAttributes["geo"] = Geo(latitude, longitude)
        
        return userAttributes;
