class Person:
    # Instance method: talk
    def talk(self):
        print("Hello World!")

    # Instance method: walk
    def walk(self):
        print("The person is walking.")


# Example usage
if __name__ == "__main__":
    alice = Person()
    alice.talk()  # Hello World!
    alice.walk()  # The person is walking.

    bob = Person()
    bob.talk()  # Hello World!
    bob.walk()  # The person is walking.
