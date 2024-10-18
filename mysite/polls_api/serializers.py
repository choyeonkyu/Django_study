from rest_framework import serializers
from polls.models import Question, Vote
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from polls.models import Choice
from rest_framework.validators import UniqueTogetherValidator

class VoteSerializer(serializers.ModelSerializer):
    voter = serializers.ReadOnlyField(source='voter.username')
    def validate(self, attrs):
        if attrs['choice'].question.id != attrs['question'].id:
            raise serializers.ValidationError({'choice': 'Question문 ID가 일치하지 않습니다.'})
        return attrs
    
    class Meta:
        model = Vote
        fields = ('id', 'question', 'choice', 'voter')
        validators = [
            UniqueTogetherValidator(fields=('question', 'voter'), queryset=Vote.objects.all())
        ]

class Choiceserializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes_count')

    def get_votes_count(self, obj):
        return obj.vote_set.count() #별도의 이름을 안정해주면 역참조 기능으로 '모델명 + _set'으로 가져올 수 있음

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    choices = Choiceserializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'owner', 'choices')

class UserSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField는 User당 여러개의 questions를 가질수있고, User의 PK를 참고할 때 사용함.
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="question-detail")
    # questions = serializers.StringRelatedField(many=True, read_only=True)
    # questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'questions')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"비밀번호가 일치하지 않습니다."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        return user
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}