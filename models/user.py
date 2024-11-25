from tortoise.models import Model
from tortoise import fields
import uuid


class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=100, unique=True)
    balance = fields.IntField(default=0, null=True)
    referral_code = fields.CharField(max_length=36, unique=True)
    referral_count = fields.IntField(default=0)
    referred_by = fields.ForeignKeyField("models.User", related_name="referrals", null=True)

    class Meta:
        table = "users"

    @classmethod
    async def generate_unique_referral_code(cls):
        while True:
            referral_code = str(uuid.uuid4())
            if not await cls.filter(referral_code=referral_code).exists():
                return referral_code