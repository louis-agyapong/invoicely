from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ("created_at", "created_by")
        fields = (
            "id",
            "name",
            "email",
            "org_number",
            "address_1",
            "address_2",
            "zip_code",
            "place",
            "country",
            "contact_person",
            "contact_reference",
        )
