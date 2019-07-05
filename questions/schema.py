import graphene
from graphene_django.types import DjangoObjectType
from .models import *

class subject(graphene.InputObjectType):
    topics= graphene.String(slug=graphene.String())
    min_mark= graphene.Int()
    max_mark= graphene.Int()

class type(graphene.InputObjectType):
    types= graphene.String(required= False, slug=graphene.String())
    min_mark= graphene.Int(required= False)
    max_mark= graphene.Int(required= False)

class section(graphene.InputObjectType):
    title= graphene.String()
    marks= graphene.Int()
    types= graphene.String(slug=graphene.String())
    topics= graphene.String(slug= graphene.String())
    

class createquestion(graphene.Mutation):
  class Arguments:
     marks= graphene.Int(required= True)
     difficulty= graphene.String() 
     clubQuestions= graphene.Boolean()
     optionalQuestions= graphene.Boolean()
     savePreset= graphene.Boolean()
     topics= graphene.List(subject)
     types= graphene.List(type)
     sections= graphene.List(section)
  ok= graphene.Boolean()
  #question= graphene.Field()
   
  def mutate(self, info):
      question= quest(id=id)
      ok=true
      return createquestion(question=question, ok=ok)

class MyMutations(graphene.ObjectType):
    create_question= createquestion.Field()

class TypeNode(DjangoObjectType):
    class Meta:
       model= Type

class TopicNode(DjangoObjectType):
    class Meta:
       model= Topic 

# Writing an app level query
class Query(graphene.ObjectType):
    all_types= graphene.List(TypeNode)
    all_topics= graphene.List(TopicNode)
   
    def resolve_all_types(self, info):
       return Type.objects.all()

    
    def resolve_all_topic(self, info):
       return Topic.objectsall()          
