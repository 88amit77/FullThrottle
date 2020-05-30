from rest_framework import serializers
from .models import Members, InOut


class MenmbersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class InOutSerializers(serializers.ModelSerializer):
    class Meta:
        model = InOut
        fields = '__all__'

class InOutSpecificSerializers(serializers.ModelSerializer):
    class Meta:
        model = InOut
        fields = ('start_time', 'end_time')


class ReportSerializer(serializers.ModelSerializer):
    activity_periods = InOutSpecificSerializers(many=True)

    class Meta:
        model = Members
        fields = ('id', 'real_name', 'tz', 'activity_periods')
