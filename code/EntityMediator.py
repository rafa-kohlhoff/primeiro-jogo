from code.Enemy import Enemy
from code.Entity import Entity

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Checks if an enemy is off-screen and sets its health to zero.
        # The 'pass' statement is removed as it's not needed.
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Iterates directly over the list, which is more Pythonic.
        for test_entity in entity_list:
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Creates and returns a new list containing only entities with health > 0.
        # This is the correct way to filter a list and avoids the common error of
        # modifying a list while iterating over it.
        return [ent for ent in entity_list if ent.health > 0]

