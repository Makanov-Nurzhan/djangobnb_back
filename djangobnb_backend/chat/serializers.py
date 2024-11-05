from rest_framework import serializers
from .models import ConversationMessage, Conversation
from useraccount.serializers import UserDetailsSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    users = UserDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id',
                  'users',
                  'modified_at',
                  )


class ConversationDetailSerializer(serializers.ModelSerializer):
    users = UserDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id',
                  'users',
                  'modified_at',
                  )


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserDetailsSerializer(many=False, read_only=True)
    created_by = UserDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = ConversationMessage
        fields = (
            'id',
            'body',
            'sent_to',
            'created_by',
        )