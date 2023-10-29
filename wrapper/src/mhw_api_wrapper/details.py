class AilmentDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.recovery = data.get("recovery")
        self.protection = data.get("protection")

        # Si vous souhaitez accéder aux propriétés de récupération, vous pouvez le faire comme suit.
        if self.recovery:
            self.recovery_actions = self.recovery.get("actions")
            self.recovery_items = self.recovery.get("items")

        # Si vous souhaitez accéder aux propriétés de protection, vous pouvez le faire comme suit.
        if self.protection:
            self.protection_items = self.protection.get("items")
            self.protection_skills = self.protection.get("skills")

class ItemDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.rarity = data.get("rarity")
        self.carryLimit = data.get("carryLimit")
        self.value = data.get("value")

class ArmorDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.type = data.get("type")
        self.rank = data.get("rank")
        self.rarity = data.get("rarity")

        self.defense = data.get("defense")
        if self.defense:
            self.base_defense = self.defense.get("base")
            self.max_defense = self.defense.get("max")
            self.augmented_defense = self.defense.get("augmented")

        self.resistances = data.get("resistances")
        if self.resistances:
            self.fire_resistance = self.resistances.get("fire")
            self.water_resistance = self.resistances.get("water")
            self.ice_resistance = self.resistances.get("ice")
            self.thunder_resistance = self.resistances.get("thunder")
            self.dragon_resistance = self.resistances.get("dragon")

        self.slots = data.get("slots")

        self.attributes = data.get("attributes")

        self.skills = data.get("skills")

        self.armorSet = data.get("armorSet")
        if self.armorSet:
            self.armor_set_id = self.armorSet.get("id")
            self.armor_set_name = self.armorSet.get("name")
            self.armor_set_rank = self.armorSet.get("rank")
            self.armor_set_pieces = self.armorSet.get("pieces")

        self.assets = data.get("assets")
        if self.assets:
            self.image_male = self.assets.get("imageMale")
            self.image_female = self.assets.get("imageFemale")

        self.crafting = data.get("crafting")
        if self.crafting:
            self.crafting_materials = self.crafting.get("materials")

class ArmorSetDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.rank = data.get("rank")
        self.pieces = data.get("pieces")
        self.bonus = data.get("bonus")

        # Si vous souhaitez accéder aux propriétés des pièces, vous pouvez le faire comme suit.
        if self.pieces:
            # Accédez à la première pièce
            first_piece = self.pieces[0]
            self.piece_id = first_piece.get("id")
            self.piece_slug = first_piece.get("slug")
            self.piece_name = first_piece.get("name")
            self.piece_type = first_piece.get("type")
            self.piece_rank = first_piece.get("rank")
            self.piece_rarity = first_piece.get("rarity")
            self.piece_armorSet = first_piece.get("armorSet")
            self.piece_attributes = first_piece.get("attributes")
            self.piece_skills = first_piece.get("skills")
            self.piece_assets = first_piece.get("assets")

        # Si vous souhaitez accéder aux propriétés du bonus, vous pouvez le faire comme suit.
        if self.bonus:
            # Accédez au premier rang du bonus
            first_rank = self.bonus.get("ranks")[0]
            self.bonus_skill_level = first_rank.get("pieces")
            self.bonus_skill = first_rank.get("skill")

class LocationDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.zoneCount = data.get("zoneCount")
        self.camps = data.get("camps")

        # Si vous souhaitez accéder aux propriétés des camps, vous pouvez le faire comme suit.
        if self.camps:
            # Accédez au premier camp
            first_camp = self.camps[0]
            self.camp_id = first_camp.get("id")
            self.camp_name = first_camp.get("name")
            self.camp_zone = first_camp.get("zone")

class SkillDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.description = data.get("description")
        self.ranks = data.get("ranks")

        # Si vous souhaitez accéder aux propriétés des rangs, vous pouvez le faire comme suit.
        if self.ranks:
            # Accédez au premier rang
            first_rank = self.ranks[0]
            self.rank_id = first_rank.get("id")
            self.rank_slug = first_rank.get("slug")
            self.rank_skill = first_rank.get("skill")
            self.rank_level = first_rank.get("level")
            self.rank_description = first_rank.get("description")
            self.rank_modifiers = first_rank.get("modifiers")

class WeaponDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.type = data.get("type")
        self.rarity = data.get("rarity")
        self.attack = data.get("attack")
        self.elderseal = data.get("elderseal")
        self.attributes = data.get("attributes")
        self.damageType = data.get("damageType")
        self.durability = data.get("durability")
        self.slots = data.get("slots")
        self.elements = data.get("elements")
        self.crafting = data.get("crafting")
        self.assets = data.get("assets")

class MotionDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.weaponType = data.get("weaponType")
        self.damageType = data.get("damageType")
        self.stun = data.get("stun")
        self.exhaust = data.get("exhaust")
        self.values = data.get("values")

class CharmDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.ranks = data.get("ranks")

        # Si vous souhaitez accéder aux propriétés des rangs, vous pouvez le faire comme suit.
        if self.ranks:
            # Accédez au premier rang
            first_rank = self.ranks[0]
            self.rank_level = first_rank.get("level")
            self.rank_rarity = first_rank.get("rarity")
            self.rank_skills = first_rank.get("skills")
            self.rank_crafting = first_rank.get("crafting")

class DecorationDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.rarity = data.get("rarity")
        self.skills = data.get("skills")
        self.slot = data.get("slot")

        # Si vous souhaitez accéder aux propriétés des compétences, vous pouvez le faire comme suit.
        if self.skills:
            # Accédez à la première compétence
            first_skill = self.skills[0]
            self.skill_id = first_skill.get("id")
            self.skill_slug = first_skill.get("slug")
            self.skill_description = first_skill.get("description")
            self.skill_level = first_skill.get("level")
            self.skill_skill = first_skill.get("skill")
            self.skill_skillName = first_skill.get("skillName")
            self.skill_modifiers = first_skill.get("modifiers")

class EventDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.platform = data.get("platform")
        self.exclusive = data.get("exclusive")
        self.type = data.get("type")
        self.expansion = data.get("expansion")
        self.description = data.get("description")
        self.requirements = data.get("requirements")
        self.questRank = data.get("questRank")
        self.successConditions = data.get("successConditions")
        self.startTimestamp = data.get("startTimestamp")
        self.endTimestamp = data.get("endTimestamp")
        self.location = data.get("location")
