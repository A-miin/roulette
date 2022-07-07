from rest_framework import serializers
from roulette.models import Roulette, Round


class RoundStat(serializers.ModelSerializer):
    users_count = serializers.SerializerMethodField()

    class Meta:
        model = Round
        fields = (
            'id',
            'users_count'
        )

    def get_users_count(self, round):
        return round.users.all().count()



