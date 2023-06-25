class Market:
    def __init__(self):
        self.questions = {}
        self.users = {}

    def create_user(self, username):
        self.users[username] = 100  # initial voice credits

    def post_question(self, user, question):
        if user in self.users:
            if question not in self.questions:
                self.questions[question] = {"user": user, "votes": 0}

    def vote(self, user, question, votes):
        if user in self.users and question in self.questions:
            cost = votes ** 2  # cost of votes is square of votes
            if self.users[user] >= cost:  # checks if user has enough voice credits
                self.questions[question]["votes"] += votes
                self.users[user] -= cost  # decrease the user's voice credits

    def results(self):
        for question, info in self.questions.items():
            print(f"Question: {question}, Posted by: {info['user']}, Votes: {info['votes']}")

    def show_credits(self):
        for user, credits in self.users.items():
            print(f"User: {user}, Voice Credits: {credits}")


def main():
    market = Market()

    while True:
        print("\n1. Register user\n2. Post a question\n3. Vote on a question\n4. See results\n5. See user voice credits\n0. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            user = input("Enter a username to register: ")
            market.create_user(user)
        elif choice == '2':
            user = input("Enter your username: ")
            question = input("Enter your question: ")
            market.post_question(user, question)
        elif choice == '3':
            user = input("Enter your username: ")
            question = input("Enter the question you want to vote on: ")
            votes = int(input("Enter number of votes (cost will be square of votes): "))
            market.vote(user, question, votes)
        elif choice == '4':
            market.results()
        elif choice == '5':
            market.show_credits()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please choose a number between 0-5.")


if __name__ == "__main__":
    main()
