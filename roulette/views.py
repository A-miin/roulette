from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from roulette.models import Roulette, Round
from roulette.serializers import RoundStat


class Spin(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        round_obj, created = Round.objects.get_or_create(finish=False)
        number = round_obj.get_roulette_number()
        round_obj.users.add(request.user)
        if number.value == -1:
            round_obj.finish = True
            round_obj.save()
            return Response(
                {'Roulette': _('Вам выпал джекпот!')},
                status=status.HTTP_200_OK
            )
        else:
            round_obj.used_numbers.add(number)
            return Response(
                {'Roulette': _(f'Вам выпал номер: {number.value}')},
                status=status.HTTP_200_OK
            )


class Statistic(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Round.objects.all()
    serializer_class = RoundStat
