# Assignment Practice OOP: User

class User:
    def __init__(self, first_name, last_name, email, age, member, points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = member
        self.gold_card_points = points

    def display_info(self):     #indent (alighn) under class indenture to include in class
        print (f'')
        print (f'First Name: {self.first_name}')
        print (f'Last Name: {self.last_name}')
        print (f'Email Address: {self.email}')
        print (f'Age: {self.age}')
        print (f'Member Status: {self.is_rewards_member}')
        print (f'Gold Card Points: {self.gold_card_points}')
        print (f'')
        return self

    def enroll(self):
        if self.is_rewards_member ==True:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount <0:
            self.gold_card_points = self.gold_card_points
        else:    
            self.gold_card_points = self.gold_card_points - amount
        return self    


Axel = User("Axel", "Foley", "Axel_F@gmail.com", 61, False, 0)

Axel.enroll().spend_points(50).enroll().display_info()


Irwin = User("Irwin", "Fletch", "FletchLives@hotmail.com", 79, False, 0)

Irwin.enroll().spend_points(80).display_info()


Peter = User("Peter", "Venkmen", "Dr.ESP@SUNYCortland.edu", 72, False, 0)

Peter.spend_points(40).display_info()