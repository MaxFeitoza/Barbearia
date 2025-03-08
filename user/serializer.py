from rest_framework import serializers
from user.models import User
from user.constants import EMAIL_ALREDY_EXIST


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "name",
            "last_name",
            "email",
            "password",
            "admin_user",
            "phone_number",
            "created_at",
        )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError(EMAIL_ALREDY_EXIST)
        except:
            return value
