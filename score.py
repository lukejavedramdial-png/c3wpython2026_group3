class RiverGameScore:
    def __init__(self):
        self.score = 0
        self.health = 3

    def collect_food(self, food_type):
        """Add points based on the food item collected."""
        food_points = {
            "duck food": 5,
            "duck food": 5,
            "large_game": 50
        }
        points = food_points.get(food_type, 5)
        self.score += points
        print(f"Got {food_type}! +{points} points.")

    def hit_obstacle(self):
        """Subtract points and health when you hit a river hazard."""
        self.score = max(0, self.score - 15)
        self.health -= 1
        print("Oh no! Hit a rock in the river. -15 points and lost 1 health.")

    def finish_crossing(self):
        """Give a bonus if you cross the river alive."""
        if self.health > 0:
            bonus = 40
            self.score += bonus
            print(f"Safe across! Survival bonus: +{bonus} points.")
        else:
            print("You did not survive the river.")

# Example usage:
game = RiverGameScore()
game.collect_food("duck food")
game.hit_obstacle()
game.finish_crossing()
print(f"Final Score: {game.score}")
